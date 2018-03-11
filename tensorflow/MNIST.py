#input_data 모듈 설치
#conda install -c anaconda wget
#간혹 위의 명령어에서 오류가 날때가 있음
#이 경우엔 기존의 root에 접근하지 못해서 일어나는 오류임
#conda create -n my_root --clone="C:\ProgramData\Anaconda3"
#위의 명렁어를 통해 원래 root에 있던 환경을 개발할 디렉터리로 복사해올수있음
#wget https://gist.githubusercontent.com/haje01/14b0e5d8bd5428df781e/raw/5b6d04c55f30191a0e32d0ae627716413c808c1c/input_data.py
#위의 명령어도 오류가 나는 경우가있음
#wget --no-check-certificate https://gist.githubusercontent.com/haje01/14b0e5d8bd5428df781e/raw/5b6d04c55f30191a0e32d0ae627716413c808c1c/input_data.py
#위의 명렁어를 이용함

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))#weight(가중치), 784차원의 이미지벡터를 곱하고, 10차원의 결과를 출력
b = tf.Variable(tf.zeros([10]))#bias(바이어스)==결과, 10차원
y = tf.nn.softmax(tf.matmul(x, W) + b)#모델링
y_ = tf.placeholder(tf.float32, [None, 10])#정답 레이블 변수

cross_entropy = -tf.reduce_sum(y_*tf.log(y))#손실에 대한 정보이론 함수, 하나의 batch(배치)내 모든 손실을 더한값

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)#학습 오퍼레이션

init = tf.global_variables_initializer()#모든 변수 초기화
sess = tf.Session()
sess.run(init)

#Stochastci Training(토캐스틱 트레이닝), 랜덤한 작은단위(100개..)로 학습하는 방식, 비용은 낮고 결과는 유사함
for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))



#예제를 보다보면 적용이 안되는 부분이나, 바뀐 부분이 많이 존재한다.
#예를들자면
#1. placeholder의 첫번째 인자에서 float이 아닌 tf.float32가 들어가야한다
#2. initialize_all_variables는 global_variables_initializer로 바뀌었다
#3. cross_entropy = -tf.reduce_sum(y_*tf.log(y))와
#cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
#는 같은 의미를 같는다.
#이처럼 많은 것들이 바뀐다.
#이런것들을 잘 메모해두어야 나중에 착오가 없을듯 싶다.
