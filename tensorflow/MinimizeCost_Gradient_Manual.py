import tensorflow as tf

print("\n*****Gradient*****\n")

x_data = [1,2,3]
y_data = [1,2,3]

W = tf.Variable(tf.random_normal([1]), name='weight')
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

hypothesis = X * W
cost = tf.reduce_mean(tf.square(hypothesis - Y))

learing_rate = 0.1
gradient = tf.reduce_mean((W*X-Y)*X) * 2#수식 그대로//W := W- a*(1/m)시그마(W-Y)*X
'''
gradient는 수동으로 이렇게 직접 미분하여 쓸수도있지만
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)
이런식으로 작성하는 것이 정석임
'''
descent = W - learing_rate * gradient
update = W.assign(descent)#assign함수는 W의 값을 변하게함

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(21):
    sess.run(update, feed_dict={X:x_data, Y:y_data})
    print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}), sess.run(W))
