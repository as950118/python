#3개 이상의 결과를 나누는데 상요됨
# Wa1 Wa2 Wa3  X1
#(Wb1 Wb2 Wb3)(X2) 형식으로 계산함
# Wc1 Wc2 Wc3  X3
#그리고 이 연산의 결과로 나온 Y1 Y2 Y3를
#softmax를 통해 0~1사이의 값을 가지게함
#이렇게 classfication을 하고
#최적의 cost를 찾는것은
#먼저 cross_entropy를 통해 먼저 실제값(Y==Lable)을 찾아야함
#정리하자면,
#LogisticClassfication(2~5번째 줄)을 통해 나온 연산결과를
#softmax를 통해 0~1사이의 값(확률)을 가지게함
#


import tensorflow as tf

x_data = [[1,2,3,4],[2,3,2,6],[3,1,1,3],[4,3,6,7],[5,3,1,9],[6,2,1,2]]
y_data = [[0,1,0],[0,0,1],[0,1,0],[0,0,1],[1,0,0],[0,1,0]]#one-hot encoding, 원소중 하나만 1임

X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 3])
#
nb_classes = 3
#
W = tf.Variable(tf.random_normal([4, nb_classes]), name='weight')#두개의 변수(X1,X2)가 나오고 Y로 출력됨 ==> 2,1
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')#나가는값(Y)가 1개 ==> 1

hypothesis = tf.nn.softmax(tf.matmul(X,W)+b)

cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis = 1))
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10001):
    sess.run(train, feed_dict={X:x_data, Y:y_data})
    if step % 200 == 0:
        print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}))
#train 종료
a = sess.run(hypothesis, feed_dict={X:[[1,2,10,3]]})
print(a, sess.run(tf.argmax(a,1)))#argmax(one-hot-encoding된 배열, 차원수)는 적합한 argument가 무엇인지를 찾아서 반환하는것임
all = sess.run(hypothesis, feed_dict={X:[[1,2,10,3],[10,1,1,13],[1,2,1,0]]})
print(a, sess.run(tf.argmax(all,1)))#다수의 배열도 가능
