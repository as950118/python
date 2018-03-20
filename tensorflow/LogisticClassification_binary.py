#2가지(0,1)로 구분할때에
#평균을 내어서 구분하는데
#지나치게 크거나 작은 값이 들어올경우
#평균이 지나치게 달라짐
#그래서 H(X) = WX + b를
#0~1값을 가지게 해주어야
#그런데 이러한 함수는 구름모양처럼되어버림
#구름모양이되면 각각의 구름모양에서 최저점을 찾아버리므로 안됨
#그래서 log를 씌워서 곡선으로 만듬
#log(H(X))는 예측을 틀리면(H(X)값이 이상하면) cost가 극단으로감
#그래서 y=1, y=0일때 두가지로나누어서
#두 함수를 합침
#그러면 기존의 밥그릇 형태의 그래프가 탄생
#COST(W) = (1/m)시그마c(H(x),y)
#C(H(x),y) = -log(H(x))  :y=1
#            -log(1-H(x)):y=0
# == -ylog(H(x))-(1-y)log(1-H(x))
import tensorflow as tf

x_data = [[1,2],[2,3],[3,1],[4,3],[5,3],[6,2]]
y_data = [[0],[0],[0],[1],[1],[1]]

X = tf.placeholder(tf.float32, shape=[None, 2])
Y = tf.placeholder(tf.float32, shape=[None, 1])
W = tf.Variable(tf.random_normal([2,1]), name='weight')#두개의 변수(X1,X2)가 나오고 Y로 출력됨 ==> 2,1
b = tf.Variable(tf.random_normal([1]), name='bias')#나가는값(Y)가 1개 ==> 1

hypothesis = tf.sigmoid(tf.matmul(X,W)+b)

cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

predicted = tf.cast(hypothesis>0.5, dtype = tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype = tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10001):
    cost_val, _ = sess.run([cost, train], feed_dict={X:x_data, Y:y_data})
    if step % 200 == 0:
        print(step, cost_val)

h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X:x_data, Y:y_data})
print("\nhypothesis : ", h, "\ncorrect : ", c, "\naccuracy : ", a);
