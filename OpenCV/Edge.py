import cv2

img = cv2.imread('./teaching_result/Resize_1_Rotate_0.jpg')

img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_edge = cv2.Canny(img_RGB, 200,600)

cv2.imshow('Origin', img_edge)

cv2.waitKey(0)
