import cv2

img = cv2.imread('./teaching_result/Resize_1_Rotate_0.jpg')

img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Red
img_R = img_RGB.copy()
img_R[:,:,0] = 0
img_R[:,:,1] = 0

cv2.imshow('Origin', img_R)

cv2.waitKey(0)
