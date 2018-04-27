import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn
import pprint

hideen_size = 2 #Output_shape = (?,?,2)
cell = tf.contrib.rnn.BasicLSTMCell(num_units = hidden_size)

#One Hot Encoding
h = [1,0,0,0]
e = [0,1,0,0]
l = [0,0,1,0]
o = [0,0,0,1]

x_data = np.array([[h, e, l, l, o]], dtype = np.float32) #Input_shape = (1,5,4)

outputs, _states = tf.nn.dynamic_rnn(cell, x_data, dtype = tf.float32)

ses.run(tf.global_variables_initializer())
pp.pprint(outputs.eval())
