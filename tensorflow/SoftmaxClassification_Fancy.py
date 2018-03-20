#더 깔끔한 형태의 softmax임

import tensorflow as tf
import numpy as np

xy = np.loadtxt('zoo.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

X = tf.placeholder(tf.float32, shape=[None, 16])
Y = tf.placeholder(tf.int32, shape=[None, 1])#float과 int의 차이는?
nb_classes = 7#0~6까지의 숫자를 가지므로
Y_one_hot = tf.one_hot(Y, nb_classes)#one-hot-encoding을 해주는 함수임, 하지만 이 함수를 쓰면 3차원이 되어버림
Y_one_hot = tf.reshape(Y_one_hot, [-1, nb_classes])#그래서 reshape함수를 통해 다시 2차원으로 바꾸어줌
W = tf.Variable(tf.random_normal([16, nb_classes]), name='weight')#두개의 변수(X1,X2)가 나오고 Y로 출력됨 ==> 2,1
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')#나가는값(Y)가 1개 ==> 1

logits = tf.matmul(X,W)+b
hypothesis = tf.nn.softmax(logits)

cost_buf = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y_one_hot)#-tf.reduce_sum(Y*tf.log(hypothesis), axis=1)를 이렇게 수정 가능함
cost = tf.reduce_mean(cost_buf)

train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)



prediction = tf.argmax(hypothesis, 1)#확률을 0~6값으로 반환함
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10001):
    sess.run(train, feed_dict={X:x_data, Y:y_data})
    if step % 200 == 0:
        loss, acc = sess.run([cost, accuracy], feed_dict={X:x_data, Y:y_data})#loss==cost 임
        print("Step : {:5}\tLoss : {:.3f}\tAcc : {:.2%}".format(step, loss, acc))

#train 종료
Pred = sess.run(prediction, feed_dict={X:x_data})
for p, y in zip(Pred, y_data.flatten()):#y.data.flatten == y_data=[[0],[1]]을 [0,1]로 바꾸어주는것 // zip == pred와 flatten된 y_data를 배열로 묶어줌
    print("[{}]Prediction : {} Real Y : {}".format(p==int(y), p, int(y)))
