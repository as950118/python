import cv2
import numpy as np

img = cv2.imread('./teaching_result/Resize_1_Rotate_0.jpg')

img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_WB = np.float32(img_gray)
img_corner = cv2.cornerHarris(img_WB, 2,3, 0.2)
img_corner = cv2.dilate(img_corner, None, iterations=1)
img_RGB[img_corner>0.01*img_corner.max()] = [255, 0, 0]

cv2.imshow('Origin', img_RGB)

cv2.waitKey(0)
