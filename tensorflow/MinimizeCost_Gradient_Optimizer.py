import tensorflow as tf

print("\n*****Optimizer 1 *****\n")
x_data = [1,2,3]
y_data = [1,2,3]

W = tf.Variable(5.0)#지나치게 틀린값을 주어도
hypothesis = x_data * W
cost = tf.reduce_mean(tf.square(hypothesis - y_data))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)#잘출력됨
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10):
    print(step, sess.run(W))
    sess.run(train)

#####
print("\n*****Optimizer 2 *****\n")
x_data = [1,2,3]
y_data = [1,2,3]

W = tf.Variable(-5.0)#지나치게 틀린값을 주어도
hypothesis = x_data * W
cost = tf.reduce_mean(tf.square(hypothesis - y_data))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)#잘출력됨
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10):
    print(step, sess.run(W))
    sess.run(train)
