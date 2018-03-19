import tensorflow as tf
import matplotlib.pyplot as plt

x_data = [1,2,3]
y_data = [1,2,3]

W = tf.placeholder(tf.float32)
hypothesis = x_data * W

cost = tf.reduce_mean(tf.square(hypothesis - y_data))
sess = tf.Session()
sess.run(tf.global_variables_initializer())

W_val = []
cost_val = []
for i in range(-30, 50):
    feed_W = i * 0.1 #0.1간격으로 표시됨
    curr_cost, curr_W = sess.run([cost, W], feed_dict={W:feed_W})
    W_val.append(curr_W)
    cost_val.append(curr_cost)

plt.plot(W_val, cost_val)
plt.show()
#여기까지는 그래프를 출력하는 것임
#최적화하는 점은 1임(==기울기가 0인 점)
#이 아래는 얼마나 잘 찾아가는지를 보는 과정임
#####
