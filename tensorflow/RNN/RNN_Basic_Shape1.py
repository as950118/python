import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn
import pprint

hideen_size = 2 #Output Shape = (?, ?, 2)

#One Hot Encoding

h = [1,0,0,0]
e = [0,1,0,0]
l = [0,0,1,0]
o = [0,0,0,1]

x_data = np.array([[h, e, l, l, o],
					[e, l, l, o, h]
                    [l, l, o, h, e]], dtype = np.float32) #Input Shape = (3, 5, 4)

cell = tf.contrib.rnn.BasicLSTMCell(num_units = hidden_size)

outputs, _states = tf.nn.dynamic_rnn(cell, x_data, dtype = tf.float32)

ses.run(tf.global_variables_initializer())
pp.pprint(outputs.eval())