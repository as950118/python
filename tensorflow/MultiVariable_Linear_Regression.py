#다수의 변수일 경우에 사용
#fx = w1x1 + w2x2 + w3x3
#cost = (1/m)시그마((w1x1 + w2x2 + w3x3) - y)^2
#           w1
#(x1 x2 x3)(w2) = (w1x1 + w2x2 + w3x3)
#           w3
#==> H(X) = WX = XW(대문자로 쓴것은 matrix를 의미함)
import tensorflow as tf

x1_data = [10, 20, 30, 40, 50]
x2_data = [15, 25, 35, 45, 55]
x3_data = [13, 23, 33, 43, 53]
y_data = [50, 60, 70, 80, 75]

x1 = tf.placeholder(tf.float32)
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

w1 = tf.Variable(tf.random_normal([1]), name='weight1')
w2 = tf.Variable(tf.random_normal([1]), name='weight2')
w3 = tf.Variable(tf.random_normal([1]), name='weight3')
b = tf.Variable(tf.random_normal([1]), name='bias')
hypothesis = x1*w1 + x2*w2 + x3*w3 + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={x1:x1_data, x2:x2_data, x3:x3_data, Y:y_data})
    if step%10 == 0:
        print(step, "cost : ", cost_val, "\nPrediction : \n", hy_val)

# 이코드는 굉장히 원시적이고 어려움
