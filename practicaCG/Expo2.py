
import cv2
import numpy as np
import math
# Leer la imagen
img1 = cv2.imread('expon.PNG',cv2.IMREAD_COLOR)
image_copy1 = np.copy(img1)
image_copy2 = np.copy(img1)
image_copy3 = np.copy(img1)
image_copy4 = np.copy(img1)

def exponencial(img, c, b):
    h,w,d = img.shape[0],img.shape[1],img.shape[2]
    
    for i in range(h):
        for j in range(w):
            for k in range(d):
                img[i,j,k] = c*(math.pow( b, img[i, j,k]) - 1)
    
   
    return img


def raiseToPower(img, c, r):
    h,w,d = img.shape[0],img.shape[1],img.shape[2]
    
    for i in range(h):
        for j in range(w):
            for k in range(d):
                img[i,j,k] = c*(math.pow( img[i, j,k], r))
    
   
    return img



#exponencial

#img_Salida1=raiseToPower(image_copy1,20,1.01)
#img_Salida2=raiseToPower(image_copy2,10,1.01)
#img_Salida3=raiseToPower(image_copy3,5,1.01)



img_Salida1=raiseToPower(image_copy1,0.1,1.5)
img_Salida2=raiseToPower(image_copy2,0.05,1.5)
img_Salida3=raiseToPower(image_copy3,0.01,1.5)



res = np.hstack((img1,img_Salida1,img_Salida2,img_Salida3))
cv2.imshow('exponencial',res)
cv2.waitKey(0)



img_Salida1= logaritmico(image_copy1,50)
img_Salida2= logaritmico(image_copy2,75)
img_Salida3= logaritmico(image_copy3,100)