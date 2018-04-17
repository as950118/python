'''
tensorboard를 이용해 코스트나 로쓰가 잘 이루어지는지 알 수 있음

name_scope를 이용하면 레이어 별로 나누어 시각화하기 좋음

ssh를 이용해 remote server를 이용할 수 있음
ssh -L local_port:127.0.0.1:remote_port username@server.com
tensorboard -logdir = ./logs/xor_logs

그리고 여러가지 그래프를 보고 싶을때는
./logs/ 에 여러가지 그래프를 생성한뒤에
tensorboard -logdir = ./logs/
하면됨

'''

import tensorflow as tf
import numpy as tf

#텐서보드
cost_summ = tf.summary.scalar("cost", cost)
W3_hist = tf.summary.histogram("weight2", W2)
hypothesis_hist = tf.summary.histogram("hypothesis", hypothesis)

summary = tf.summary.merge_all()

writer = tf.summary.FileWriter('./logs')
writer.add_graph(sess.graph)
