'''
Input - Convolution - SubSampling -> FCN
          Feauture extraction       classification
'''
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#Session
sess = tf.InteractiveSession()

#Input
img = np.array([[[[1],[2],[3],[4],[5],[6]],
                    [[2],[3],[4],[5],[6],[1]],
                    [[3],[4],[5],[6],[2],[1]],
                    [[4],[5],[6],[3],[2],[1]],
                    [[5],[6],[4],[3],[2],[1]],
                    [[6],[5],[4],[3],[2],[1]]]], dtype = np.float32)
print(img.shape)
plt.imshow(image.reshape(6,6), cmap='Greys')#이미지 시각화

#Filter
filter = tf.constant([[[[1.]],[[0.]],[[1.]]],
                      [[[0.]],[[1.]],[[1.]]],
                      [[[1.]],[[1.]],[[0.]]]])
print(filter.shape)

#Session
sess = tf.InteractiveSession()

#Convolution
conv2d = tf.nn.conv2d(image, filter, strides=[1,1,1,1], padding='VALID')
conv2d_img = conv2d.eval()
print(conv2d_img.shape)
plt.imshow(conv2d_img.reshape(4,4), cmap='Greys')#이미지 시각화
for i, one_img in enumerate(conv2d_img):
    plt.subplot(1,i+1,2)

#Subsampling
maxpool = tf.nn.max_pool(conv2d_img, ksize=[1, 2, 2, 1],
                    strides=[1, 1, 1, 1], padding='VALID')
maxpool_img = maxpool.eval()
print(maxpool_img.shape)
for i, one_img in enumerate(maxpool_img):
    print(one_img.reshape(3,3))
plt.imshow(maxpool_img.reshape(3,3), cmap='Greys')#이미지 시각화
