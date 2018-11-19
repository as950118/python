import tensorflow as tf
import numpy as np

data = np.loadtxt('./golden.csv', delimiter=',', dtype = np.float32)
arr = [[0],[0],[0],[0]]*len(data)
for i in range(len(data)):
    arr[i] = data[i]
Dogs_temp = data[0,1:3]
Out_temp = data[0:,2]

Dogs_BPM = data[0:20,[3]]
Dogs_Step = data[0:,4]

Dogs_State = data[0:10000,1:3]
#Dogs_State = Dogs_State.astype('list')
#Dogs_State = list(chain.from_iterable(data[0:,:4]))

TrueFalse = data[0:10000,[-1]]
#Dogs_State = tf.convert_to_tensor(data[:,:-1], np.float32)
#TrueFalse = tf.convert_to_tensor(data[:,[-1]], np.float32)

x_data = Dogs_State
y_data = Dogs_BPM
#print(x_data, y_data)
X = tf.placeholder(tf.float32, shape=[None, 2])#None = n, 즉 원하는 만큼 쓸수있음
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([2,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
hypothesis = tf.matmul(X,W) + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={X:x_data, Y:y_data})
    if step%200 == 0:
        print(step, "cost : ", cost_val, "\nPrediction : \n", hy_val)
