import cv2
import numpy as np


for k in range(51):
    img = cv2.imread('./teaching/teaching'+str(k+1)+'.jpg')
    img2 = cv2.imread('./teaching/test.jpg')
    img3 = cv2.imread('./images_mapped/image'+str(k+1)+'.jpg')

    img = cv2.resize(img, (255, 255), interpolation=cv2.INTER_AREA)
    img2 = cv2.resize(img2, (255, 255), interpolation=cv2.INTER_AREA)
    img3 = cv2.resize(img3, (255, 255), interpolation=cv2.INTER_AREA)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j][2]>130 and img[i,j][1]<100 and img[i,j][0]<100:
                break
            else:
                img2[i,j] = [0,0,0]
    for j in range(img.shape[1]):
        for i in range(img.shape[0]):
            if img[i,j][2]>130 and img[i,j][1]<100 and img[i,j][0]<100:
                break
            else:
                img2[i,j] = [0,0,0]

    for i in range(img.shape[0]-1, 0, -1):
        for j in range(img.shape[1]-1, 0, -1):
            if img[i,j][2]>130 and img[i,j][1]<100 and img[i,j][0]<100:
                break
            else:
                img2[i,j] = [0,0,0]
    for j in range(img.shape[1]-1, 0, -1):
        for i in range(img.shape[0]-1, 0, -1):
            if img[i,j][2]>130 and img[i,j][1]<100 and img[i,j][0]<100:
                break
            else:
                img2[i,j] = [0,0,0]

    cv2.imwrite('./teaching_result/image'+str(k+1)+'.jpg', img2)
    cv2.imwrite('./teaching_result2/image'+str(k+1)+'.jpg', img3)

    '''
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    img_H = img_HSV.copy()
    img_H[:,:,0] = 0;
    img_S = img_HSV.copy()
    img_S[:,:,1] = 0;
    img_V = img_HSV.copy()
    img_V[:,:,2] = 0;
    max_x =0;
    min_x =0;
    max_y =0;
    min_y =0;
    '''
    '''
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x = img_V[i,j]
            if x[0]!=0 or x[1]!=0 or x[2]!=0:
                if max_x < i:
                    max_x = i
                if max_y < j:
                    max_y = j
                if min_x == 0:
                    min_x = i
                elif min_x > i:
                    min_x = i
                if min_y == 0:
                    min_y = j
                elif min_y > j:
                    min_y = j
    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            if i > max_x or i < min_x:
                img2[i,j] = [0,0,0]
            if j > max_y or j < min_y:
                img2[i,j] = [0,0,0]


    img_resize = cv2.resize(img2, (256, 256), interpolation=cv2.INTER_AREA)
    cv2.imwrite('./teaching_result/image'+str(k+1)+'.png', img_resize)

    '''
    '''
    cv2.imwrite('./teaching_result/Resize_'+str(k+1)+'_Rotate_0.jpg', img_resize)

    img_RGB = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)#BGR2LAB
    #Rotate
    W, H, C = img_resize.shape

    Rotate_Center = int(W/2), int(H/2)
    Rotate_Angle = 30

    img_rotate = cv2.getRotationMatrix2D(Rotate_Center, Rotate_Angle, 1)

    img_reverse_horizon = cv2.flip(img_resize, 1)
    cv2.imwrite('./teaching_result/Resize_'+str(k+1)+'_Rotate_0_Reverse.jpg', img_reverse_horizon)

    for j in range(10):
        img_rotate = cv2.getRotationMatrix2D(Rotate_Center, Rotate_Angle*(j+1), 1)
        img_rotate_result = cv2.warpAffine(img_resize, img_rotate, (W, H))
        cv2.imwrite('./teaching_result/Resize_'+str(k+1)+'_Rotate_'+str(30*(j+1))+'.jpg', img_rotate_result)

        img_reverse_horizon = cv2.flip(img_rotate_result, 1)
        cv2.imwrite('./teaching_result/Resize_'+str(k+1)+'_Rotate_'+str(30*(j+1))+'_Reverse.jpg', img_reverse_horizon)
    '''

'''
cv2.imshow('Origin', img_V)
cv2.waitKey(0)
'''

'''
img_gray = cv2.cvtColor(img_V, cv2.COLOR_BGR2GRAY)
img_edge = cv2.Canny(img_gray, 200,400)

img_WB = np.float32(img_edge)
img_corner = cv2.cornerHarris(img_WB, 2,3, 0.2)
img_corner = cv2.dilate(img_corner, None, iterations=1)
img_V[img_corner>0.01*img_corner.max()] = [255, 0, 0]


ret, thr = cv2.threshold(img_edge, 127,255,0)
_, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img2, contours, 2, (0,0,255), 5)
'''
