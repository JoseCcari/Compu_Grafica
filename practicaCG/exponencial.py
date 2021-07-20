
import cv2
import numpy as np
import math
# Leer la imagen
img1 = cv2.imread('loga3.PNG',0)
image_copy1 = np.copy(img1)
image_copy2 = np.copy(img1)
image_copy3 = np.copy(img1)


def exponencial(image, c, b):
    for i in range(0, image.shape[1]):  # image width
        for j in range(0, image.shape[0]):  # image height

            # compute exponential transform

            image[j, i] = c * (math.pow( b, image[j, i]) - 1)
    return image

def raiseToPower(image, c, r):
    for i in range(0, image.shape[1]):  # image width
        for j in range(0, image.shape[0]):  # image height

            # compute exponential transform

            image[j, i] = c * (math.pow( image[j, i],r))
    return image


def logaritmo(image, c):
    for i in range(image.shape[1]):  # image width
        for j in range(image.shape[0]):  # image height

            # compute exponential transform

            image[j, i] = c *  (math.log10( 1+ image[j, i]))
    
    return image

#exponencial

#img_Salida1=exponencial(image_copy1,20,1.01)
#img_Salida2=exponencial(image_copy2,10,1.01)
#img_Salida3=exponencial(image_copy3,5,1.01)


#Raise to power

img_Salida1=raiseToPower(image_copy1,0.1,1.5)
img_Salida2=raiseToPower(image_copy2,0.05,1.5)
img_Salida3=raiseToPower(image_copy3,0.01,1.5)

#img_Salida1=raiseToPower(image_copy1,0.2,1.25)
#img_Salida2=raiseToPower(image_copy2,0.05,1.25)
#img_Salida3=raiseToPower(image_copy3,0.01,1.25)

#logaritmo

#img_Salida1= logaritmo
#(image_copy1,70)
#img_Salida2= logaritmo
#(image_copy2,100)
#img_Salida3= logaritmo
#(image_copy3,120)

res = np.hstack((img1,img_Salida1,img_Salida2,img_Salida3))
cv2.imshow('Raise to Power',res)
cv2.waitKey(0)



