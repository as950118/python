import tensorflow as tf
import numpy as np

data = np.loadtxt('./data_set.csv', delimiter=',', dtype = np.float32, encoding='UTF')
arr = [[0],[0],[0],[0]]*len(data)
for i in range(len(data)):
    arr[i] = data[i]
Dogs_temp = data[0:,0]
Out_temp = data[0:,1]
Dogs_BPM = data[0:,2]
Dogs_Step = data[0:,3]

Dogs_State = data[0:,:4]
TrueFalse = data[0:,4:5]
print(Dogs_State, TrueFalse)

X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 1])
W = tf.Variable(tf.random_normal([4,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.sigmoid(tf.matmul(X,W)+b)

cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

predicted = tf.cast(hypothesis>0.5, dtype = tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype = tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10001):
    cost_val, _ = sess.run([cost, train], feed_dict={X:Dogs_State, Y:TrueFalse})
    if step % 200 == 0:
        print(step, cost_val)

h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X:Dogs_State, Y:TrueFalse})
print("\nhypothesis : ", h, "\ncorrect : ", c, "\naccuracy : ", a);
