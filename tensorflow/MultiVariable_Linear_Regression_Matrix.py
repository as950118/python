import tensorflow as tf

x_data = [[10, 20, 30], [40, 50, 15], [25, 35, 45], [55, 13, 23], [33, 43, 53]]
y_data = [[50], [60], [70], [80], [75]]

X = tf.placeholder(tf.float32, shape=[None, 3])#None = n, 즉 원하는 만큼 쓸수있음
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([3,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
hypothesis = tf.matmul(X,W) + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={X:x_data, Y:y_data})
    if step%10 == 0:
        print(step, "cost : ", cost_val, "\nPrediction : \n", hy_val)
