'''
Accuracy : 93%
'''
import tensorflow as tf
import numpy as np
import csv
from itertools import chain


data = np.loadtxt('./data_set_test.csv', delimiter=',', dtype = np.float32)
arr = [[0],[0],[0],[0]]*len(data)
for i in range(len(data)):
    arr[i] = data[i]
Dogs_bpm_temp = data[0:150,5:-1]
TrueFalse = data[0:150,[-1]]
Test_Dogs_bpm_temp = data[150:300,5:-1]
Test_TrueFalse = data[150:300,[-1]]

X = tf.placeholder(tf.float32, shape=[None, 2])
Y = tf.placeholder(tf.float32, shape=[None, 1])
W = tf.Variable(tf.random_normal([2,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.sigmoid(tf.matmul(X,W)+b)#relu

cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
learning_rate = 0.011
train = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)#adam
#train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
predicted = tf.cast(hypothesis>0.5, dtype = tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype = tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())
print("----------------\nLearning :\nStep   Cost")
for step in range(10001):
    cost_val, _ = sess.run([cost, train], feed_dict={X:Dogs_bpm_temp, Y:TrueFalse})
    if step % 500 == 0:
        print(step, "\t", cost_val)

h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X:Test_Dogs_bpm_temp, Y:Test_TrueFalse})
print("----------------\nHypothesis :\n", h[0:10], "\n----------------\nCorrect :\n", c[0:10], "\n----------------\nAccuracy : ", a);
