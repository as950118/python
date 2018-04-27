import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn
import pprint

hideen_size = 2 #Output Shape Dimention 결정

cell = tf.contrib.rnn.BasicLSTMCell(num_units = hidden_size)

x_data = np.array([[[1,0,0,0]]], dtype = np.float32)#Input Shape 결정

outputs, _states = tf.nn.dynamic_rnn(cell, x_data, dtype = tf.float32)

ses.run(tf.global_variables_initializer())
pp.pprint(outputs.eval())
