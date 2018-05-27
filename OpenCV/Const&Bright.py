#Const&Bright
import cv2
import numpy as np
from matplotlib import pyplot as plt

for i in range(51):
    img_str = './teaching_result2/teaching'+str(i+1)+'.jpg'

    img = cv2.imread(img_str);

    hist, bins = np.histogram(img.flatten(), 255,[0,255])

    cdf = hist.cumsum()

    cdf_m = np.ma.masked_equal(cdf,0)

    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())

    cdf = np.ma.filled(cdf_m,0).astype('unit8')

    img2 = cdf[img]
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.subplot(122),plt.imshow(img2),plt.title('Equalization')
    plt.show()
