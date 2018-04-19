'''
Restricted Boatman Machine(RBM)

어떠한 x1,x2,x3..입력이 있을때
w1,w2,w3..와 결과값 y1,y2,y3..가 있을것임(Frowarding)
그러면 반대로 y1,y2,y3와 w1,w2,w3를 통해 나온
x1,x2,x3..를 구할수있을것임(Backwarding)

이렇게 해서 구한 첫번째 x1,x2,x3..와 두번째 x1,x2,x3..의 차이가 가장 적도록 하는것임
이러한 작업은 근접한 두개의 layer간에 이루어짐

성능은 좋지만 구현하기에 조금 복잡함


Xavier/He Initilization

하나의 노드에 n개의 입력과 m개의 출력에 따라 맞게 초기값을 설정함
#Xavier
W = np.random.randn(fan_in, fan_out)/np.sqrt(fan_in)
#He
W = np.random.randn(fan_in, fan_out)/np.sqrt(fan_in/2)

이러면 간단하게 좋은 성능을 가짐

'''

import tensorflow as tf
import random
import numpy as np

#진리표 세팅
x_data = np.array([[0,0],[1,0],[0,1],[1,1]], dtype = np.float32)
y_data = np.array([[0],[1],[1],[0]], dtype = np.float32)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

#Input Layer
W1 = tf.get_variable("W1", shape=[2, 512],
                     initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([512]))
layer1 = tf.nn.relu(tf.matmul(X, W1) + b1)

#Hidden Layer
#random_normal = 0~1사이의 균등확률 분포 값을 생성, 이경우엔 -1~1 사이
#zeros = n*n 영행렬 생성
W2 = tf.get_variable("W2", shape=[512, 512],
                     initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([512]))
layer2 = tf.nn.relu(tf.matmul(layer1, W2) + b2)
W3 = tf.get_variable("W3", shape=[512, 512],
                     initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([512]))
layer3 = tf.nn.relu(tf.matmul(layer2, W3) + b3)
W4 = tf.get_variable("W4", shape=[512, 512],
                     initializer=tf.contrib.layers.xavier_initializer())
b4 = tf.Variable(tf.random_normal([512]))
layer4 = tf.nn.relu(tf.matmul(layer3, W4) + b4)
W5 = tf.get_variable("W5", shape=[512, 1],
                     initializer=tf.contrib.layers.xavier_initializer())
b5 = tf.Variable(tf.random_normal([1]))
hypothesis = tf.sigmoid(tf.matmul(layer4, W5) + b5)


#코스트 / 로쓰 함수
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate = 0.1).minimize(cost)

#정확도
predicted = tf.cast(hypothesis > 0.5, dtype = tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype = tf.float32))


#실행
sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(10001):
    sess.run(train, feed_dict = {X : x_data, Y : y_data})
    if step%100 == 0:
        print(step, sess.run(cost, feed_dict = {X : x_data, Y : y_data}), "\n",sess.run([W1, W2, W3]))

h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict = {X : x_data, Y : y_data})
print("\nhypothesis : \n", h, "\ncorrect : \n", c, "\naccuracy : \n", a)
