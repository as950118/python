import cv2
import numpy as np

img = cv2.imread('./teaching_result/Resize_1_Rotate_0.jpg')

img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thr = cv2.threshold(img_gray, 127,255,0)
_, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,0,255), 1)

cv2.imshow('thresh', thr)
cv2.imshow('contour', img)

cv2.waitKey(0)
