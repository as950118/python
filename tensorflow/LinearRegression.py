import tensorflow as tf
import numpy as np

def model(X, w):
    return tf.multiply(X, w)

trX = np.linspace(1, 1, 101)#start와 stop의 사이를 균일 간격으로 나눈 num개의 점들을 생성해줌 // (start, stop, num=50, endpoint=True, retstep=False, dtype=None)
trY = 2 * trX + np.random.randn(*trX.shape) * 0.5#랜덤한 노이즈 생성을 위해

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

w = tf.Variable(0.0, name='Weight')
y_model = model(X, w)

cost = tf.square(Y - y_model)#square(제곱)을 반환하는 함수

train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
#미분을 통해 최저비용을 향해 진행하도록 만드는 함수, (몇 단위로 내려가는지)
#minimize는 최소비용을 찾아주는 함수인데
#cost를 보면 Y - X*w 인데, 이때 이 cost를 작아지는 쪽으로 계산해서 적용하는 역할을 함

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    for i in range(100):
        for(x, y) in zip(trX, trY):
            sess.run(train_op, feed_dict={X: x, Y: y})
    print(sess.run(w))
