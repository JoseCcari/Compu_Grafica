
import cv2
import numpy as np
import math
# Leer la imagen
img1 = cv2.imread('raiz.PNG',0)
image_copy1 = np.copy(img1)
image_copy2 = np.copy(img1)
image_copy3 = np.copy(img1)



def logaritmo(image, c):
    for i in range(image.shape[1]):  # image width
        for j in range(image.shape[0]):  # image height

            # compute log transform

            image[j, i] = c *  (math.log10( 1+ image[j, i]))
    
    return image


def raiz(image, c):
    for i in range(image.shape[1]):  # image width
        for j in range( image.shape[0]):  # image height

            # compute raiz transform

            image[j, i] = (c * (math.sqrt(image[j, i])))
    return image


#logaritmo

#img_Salida1= logaritmo(image_copy1,70)
#img_Salida2= logaritmo(image_copy2,100)
#img_Salida3= logaritmo(image_copy3,120)


#raiz
img_Salida1= raiz(image_copy1,10)
img_Salida2= raiz(image_copy2,20)
img_Salida3= raiz(image_copy3,30)


res = np.hstack((img1,img_Salida1,img_Salida2,img_Salida3))
cv2.imshow('Raiz',res)
cv2.waitKey(0)



