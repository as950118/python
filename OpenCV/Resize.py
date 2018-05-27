#Resize
import cv2
import numpy as np

for i in range(55):
    img_str = './teaching/teaching'+str(i+1)+'.jpg'
    img = cv2.imread(img_str)

    #Resize(AREA = -, CUBIC = +)
    img_resize = cv2.resize(img, (256, 256), interpolation=cv2.INTER_AREA)
    cv2.imwrite('./teaching_result/Resize_'+str(i+1)+'_Rotate_0.jpg', img_resize)


    img_RGB = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)#BGR2LAB
    #Rotate
    W, H, C = img_resize.shape

    Rotate_Center = int(W/2), int(H/2)
    Rotate_Angle = 30

    img_rotate = cv2.getRotationMatrix2D(Rotate_Center, Rotate_Angle, 1)

    img_reverse_horizon = cv2.flip(img_resize, 1)
    cv2.imwrite('./teaching_result/Resize_'+str(i+1)+'_Rotate_0_Reverse.jpg', img_reverse_horizon)

    for j in range(10):
        img_rotate = cv2.getRotationMatrix2D(Rotate_Center, Rotate_Angle*(j+1), 1)
        img_rotate_result = cv2.warpAffine(img_resize, img_rotate, (W, H))
        cv2.imwrite('./teaching_result/Resize_'+str(i+1)+'_Rotate_'+str(30*(j+1))+'.jpg', img_rotate_result)

        img_reverse_horizon = cv2.flip(img_rotate_result, 1)
        cv2.imwrite('./teaching_result/Resize_'+str(i+1)+'_Rotate_'+str(30*(j+1))+'_Reverse.jpg', img_reverse_horizon)




    '''
    img_rotate_result = cv2.warpAffine(img_resize, img_rotate, (W, H))
    cv2.imwrite('./teaching_result/Resize_'+str(i+1)+'_Rotate_90.jpg', img_rotate_result)

    img_reverse_horizon = cv2.flip(img_rotate_result, 0)
    cv2.imwrite('./teaching_result/Resize_'+str(i+1)+'_Rotate_90_Reverse.jpg', img_reverse_horizon)


    img_rotate_result = cv2.warpAffine(img_rotate_result, img_rotate, (W, H))
    cv2.imwrite('./teaching_result/Resize_'+str(i+1)+'_Rotate_180.jpg', img_rotate_result)

    img_reverse_horizon = cv2.flip(img_rotate_result, 1)
    cv2.imwrite('./teaching_result/Resize_'+str(i+1)+'_Rotate_180_Reverse.jpg', img_reverse_horizon)

    img_rotate_result = cv2.warpAffine(img_rotate_result, img_rotate, (W, H))
    cv2.imwrite('./teaching_result/Resize_'+str(i+1)+'_Rotate_270.jpg', img_rotate_result)
    img_reverse_horizon = cv2.flip(img_rotate_result, 0)
    cv2.imwrite('./teaching_result/Resize_'+str(i+1)+'_Rotate_270_Reverse.jpg', img_reverse_horizon)
    '''



    #Contrast&Brightness
    '''
    hist, bins = np.histogram(img_resize.flatten(), 256,[0,256])

    cdf = hist.cumsum()

    cdf_m = np.ma.masked_equal(cdf,0)

    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())

    cdf = np.ma.filled(cdf_m,0).astype('uint8')

    img_result = cdf[img_resize]
    '''
    #CLAHE
    '''
    lab = cv2.cvtColor(img_resize, cv2.COLOR_BGR2LAB)
    lab_planes = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img_result = clahe.apply(lab_planes[0])
    '''
    #Reverse
    '''
    img_revers = cv2.cvtColor(img_resize, cv2.COLOR_BGR2LAB)
    img_revers_horizon = cv2.flip(img_revers, 1)
    img_revers_vertical = cv2.flip(img_revers, 0)
    '''
    #Rotate
    '''
    W, H = img_resize.shape

    Rotate_Center = int(W/2), int(H/2)
    Rotate_Angle = 90

    img_rotate = cv2.getRotaionMatrix2d(Rotate_Center, Rotate_Angle, 1)
    img_rotate = cv2.warpAffine(img_RGB, img_rotate, (W, H))
    '''
    #Ouput
    '''
    cv2.imshow('Origin', img)
    cv2.imshow('Resize', img_result)
    '''
    #Save
    '''
    cv2.imwrite('./teaching_result/teaching'+str(i+1)+'.jpg', img_result)
    '''


import cv2
import numpy as np

for i in range(51):
    img = cv2.imread('./teaching_result2/image'+str(i+1)+'.jpg')

    hist, bins = np.histogram(img.flatten(), 256,[0,256])

    cdf = hist.cumsum()
    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m,0).astype('uint8')
    img_result = cdf[img]
    cv2.imwrite('./teaching_result2/image'+str(i+1)+'.jpg', img_result)
