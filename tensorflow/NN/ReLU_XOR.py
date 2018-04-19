'''
레이어의 숫자를 늘리는 것은 효과적일수도있지만
너무 심할경우 기울기가 사라지는 vanishing gradient의 문제가 생길수도 있음

non-linearity문제임
이것은 sigmoid를 잘못이해한 탓임

ReLU를 생각해냄
0보다 작으면 0, 0이상이면 계속 증가하는 형태( " _↗ " 형태)
L1 = tf.nn.relu(tf.matmul(X,W1)+b1)
처럼 사용함

그외에도 Leaky ReLU, ELU 같이 0 이하를 살려주는등 조금 다른형태로 만드는 방식도 있음

sigmoid를 수정한것은 tanh같은것도 있음

주로 ReLU나 Leaky ReLU를 많이 사용

ReLU에서도 문제점이있음
random값에 따라 gradient의 편차가 심함
그래서 weight를 잘 조절할 필요성이있음
그것은 다음 시간에
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
W1 = tf.Variable(tf.random_uniform([2, 3], -1.0, 1.0), name = 'weight1')
b1 = tf.Variable(tf.zeros([3]), name = 'bias1')
layer1 = tf.nn.relu(tf.matmul(X, W1) + b1)

#Hidden Layer
#random_normal = 0~1사이의 균등확률 분포 값을 생성, 이경우엔 -1~1 사이
#zeros = n*n 영행렬 생성
W2 = tf.Variable(tf.random_uniform([3, 4], -1.0, 1.0), name = 'weight2')
b2 = tf.Variable(tf.zeros([4]), name = 'bias2')
layer2 = tf.nn.relu(tf.matmul(layer1, W2) + b2)
W3 = tf.Variable(tf.random_uniform([4, 5], -1.0, 1.0), name = 'weight3')
b3 = tf.Variable(tf.zeros([5]), name = 'bias3')
layer3 = tf.nn.relu(tf.matmul(layer2, W3) + b3)
W4 = tf.Variable(tf.random_uniform([5, 6], -1.0, 1.0), name = 'weight4')
b4 = tf.Variable(tf.zeros([6]), name = 'bias4')
layer4 = tf.nn.relu(tf.matmul(layer3, W4) + b4)
W5 = tf.Variable(tf.random_uniform([6, 7], -1.0, 1.0), name = 'weight5')
b5 = tf.Variable(tf.zeros([7]), name = 'bias5')
layer5 = tf.nn.relu(tf.matmul(layer4, W5) + b5)
W6 = tf.Variable(tf.random_uniform([7, 8], -1.0, 1.0), name = 'weight6')
b6 = tf.Variable(tf.zeros([8]), name = 'bias6')
layer6 = tf.nn.relu(tf.matmul(layer5, W6) + b6)
W7 = tf.Variable(tf.random_uniform([8, 9], -1.0, 1.0), name = 'weight7')
b7 = tf.Variable(tf.zeros([9]), name = 'bias7')
layer7 = tf.nn.relu(tf.matmul(layer6, W7) + b7)
W8 = tf.Variable(tf.random_uniform([9, 10], -1.0, 1.0), name = 'weight8')
b8 = tf.Variable(tf.zeros([10]), name = 'bias8')
layer8 = tf.nn.relu(tf.matmul(layer7, W8) + b8)

#Output Layer
W9 = tf.Variable(tf.random_uniform([10, 1], -1.0, 1.0), name = 'weight9')
b9 = tf.Variable(tf.zeros([1]), name = 'bias9')
#출력결과가 0~1사이여야하므로 마지막단은 sigmoid를 사용함
hypothesis = tf.sigmoid(tf.matmul(layer8, W9) + b9)


#코스트 / 로쓰 함수
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate = 0.1).minimize(cost)

#정확도
predicted = tf.cast(hypothesis > 0.5, dtype = tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype = tf.float32))


#실행
sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(30001):
    sess.run(train, feed_dict = {X : x_data, Y : y_data})
    if step%2000 == 0:
        print(step, sess.run(cost, feed_dict = {X : x_data, Y : y_data}), "\n",sess.run([W1, W2, W3]))

h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict = {X : x_data, Y : y_data})
print("\nhypothesis : \n", h, "\ncorrect : \n", c, "\naccuracy : \n", a)
