import tensorflow as tf
xData = [1,2,3,4,5,6]
yData = [100,210,320,410,560,610]
w = tf.Variable(tf.random_uniform([1], -100, 100))
b = tf.Variable(tf.random_uniform([1], -100, 100))
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
h = w * x + b
cost = tf.reduce_mean(tf.square(h-y))
a = tf.Variable(0.01)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(5001):
    sess.run(train, feed_dict={x:xData, y:yData})
    if i % 500 == 0:
        print(i, sess.run(cost, feed_dict={x:xData, y:yData}), sess.run(w), sess.run(b))
for i in xData:
    print(sess.run(h, feed_dict={x:i}))
