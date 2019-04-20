import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def test():
    #테스트 이미지 생성, 출력 / (1,3,3,1) 이미지 생성
    sess = tf.InteractiveSession()
    image = np.array([[[[1],[2],[3]],
                        [[4],[5],[6]],
                        [[7],[8],[9]]]], dtype = np.float32)
    print(image.shape)
    plt.imshow(image.reshape(3,3), cmap='Greys')#이미지 시각화
