import os
import numpy as np
import tensorflow as tf

IMAGE_SIZE =256

image = tf.placeholder(tf.float32, shape=[None, IMAGE_SIZE, IMAGE_SIZE, 3], name="input_image")
annotation = tf.placeholder(tf.int32, shape=[None, IMAGE_SIZE, IMAGE_SIZE, 1], name="annotation")

image = np.reshape(image, 1)

print(image)

'''
DATA_URL = 'http://data.csail.mit.edu/places/ADEchallenge/ADEChallengeData2016.zip'

SceneParsing_folder = os.path.splitext(DATA_URL.split("/")[-1])[0]
print(SceneParsing_folder)
'''
