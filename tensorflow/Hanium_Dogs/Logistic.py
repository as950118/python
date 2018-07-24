import tensorflow as tf
import numpy as np
import csv
from itertools import chain

data = np.loadtxt('./data_set.csv', delimiter=',', dtype = np.float32)
arr = [[0],[0],[0],[0]]*len(data)
for i in range(len(data)):
    arr[i] = data[i]
Dogs_temp = data[0:20,1:3]
'''
Out_temp = data[0:,2]
Dogs_BPM = data[0:,3]
Dogs_Step = data[0:,4]

Dogs_State = data[0:,1:-1]
#Dogs_State = Dogs_State.astype('list')
#Dogs_State = list(chain.from_iterable(data[0:,:4]))
'''
TrueFalse = data[0:20,[-1]]


X = tf.placeholder(tf.float32, shape=[None, 2])
Y = tf.placeholder(tf.float32, shape=[None, 1])
W = tf.Variable(tf.random_normal([2,1]), name='weight')#두개의 변수(X1,X2)가 나오고 Y로 출력됨 ==> 2,1
b = tf.Variable(tf.random_normal([1]), name='bias')#나가는값(Y)가 1개 ==> 1

hypothesis = tf.sigmoid(tf.matmul(X,W)+b)

cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.011).minimize(cost)

predicted = tf.cast(hypothesis>0.5, dtype = tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype = tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100001):
    cost_val, _ = sess.run([cost, train], feed_dict={X:Dogs_temp, Y:TrueFalse})
    if step % 200 == 0:
        print(step, cost_val)

h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X:Dogs_temp, Y:TrueFalse})
print("\nhypothesis : ", h, "\ncorrect : ", c, "\naccuracy : ", a);
