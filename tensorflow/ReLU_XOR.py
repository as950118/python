'''
레이어의 숫자를 늘리는 것은 효과적일수도있지만
너무 심할경우 기울기가 사라지는 vanishing gradient의 문제가 생길수도 있음

non-linearity문제임 / 이것은 sigmoid를 잘못이해한 탓임

ReLU를 생각해냄
0보다 작으면 0, 0이상이면 계속 증가하는 형태
L1 = tf.nn.relu(tf.matmul(X,W1)+b1)
처럼 사용함
'''


import tensorflow as tf
import numpy as np

#진리표 세팅
x_data = np.array([[0,0],[1,0],[0,1],[1,1]], dtype = np.float32)
y_data = np.array([[0],[1],[1],[0]], dtype = np.float32)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

'''
#모델링
W = tf.Variable(tf.random_normal([2,1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

#가설 모델링
hypothesis = tf.sigmoid(tf.matmul(X, W) + b)
#하지만 이렇게 하면 옳은 결과가 안나옴
'''

#이렇게하면 옳은결과가 나옴
W1 = tf.Variable(tf.random_normal([2, 3]), name = 'weight1')
b1 = tf.Variable(tf.random_normal([3]), name = 'bias1')
layer1 = tf.sigmoid(tf.matmul(X, W1) + b1)#레이어를 추가한다는 것은 단계를 나누는 것을 의미

#레이어의 숫자를 늘리는 방법으로 딥러닝을 수행 할 수 있음
W2 = tf.Variable(tf.random_normal([3, 4]), name = 'weight2')
b2 = tf.Variable(tf.random_normal([4]), name = 'bias2')
layer2 = tf.sigmoid(tf.matmul(layer1, W2) + b2)

W3 = tf.Variable(tf.random_normal([4, 1]), name = 'weight3')
b3 = tf.Variable(tf.random_normal([1]), name = 'bias3')
hypothesis = tf.sigmoid(tf.matmul(layer2, W3) + b3)


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
        print(step, sess.run(cost, feed_dict = {X : x_data, Y : y_data}), sess.run([W1, W2, W3]))

h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict = {X : x_data, Y : y_data})
print("\nhypothesis : \n", h, "\ncorrect : \n", c, "\naccuracy : \n", a)
