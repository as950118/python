import tensorflow as tf#텐서플로우 모듈을 불러와서 tf라는 변수에 저장함

a = tf.placeholder(tf.float16)#변수생성
b = tf.placeholder(tf.float16)
y = tf.multiply(a, b)#a와 b의 곱셈 결과

with tf.Session() as sess:#sess = tf.Session() 과 같은 의미임
    print("%f" % sess.run(y, feed_dict={a:10, b:10}))
    print("%f" % sess.run(y, feed_dict={a:15, b:15}))
