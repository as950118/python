import tensorflow as tf

print("\n*****Option*****\n")
x_data = [1,2,3]
y_data = [1,2,3]

W = tf.Variable(5.0)
hypothesis = x_data * W

gradient = tf.reduce_mean((W * x_data - y_data) * x_data) * 2#직접 계산한 함수

cost = tf.reduce_mean(tf.square(hypothesis - y_data))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)#러닝레이트를 더 줄였음

gvs = optimizer.compute_gradients(cost)#optimizer에 적합한 gradient를 계산함
apply_gradients = optimizer.apply_gradients(gvs)#적용함

#직접 계산한 함수(gradient)와 optimizer를 통해 찾은 함수(gsv)가 일치하는지 알아볼것임
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100):
    print(step, sess.run([gradient, W, gvs]))
    sess.run(apply_gradients)
