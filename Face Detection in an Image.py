# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 08:09:17 2018

@author: S.A.P
"""

import cv2
import matplotlib.pyplot as plt
import time
%matplotlib inline
def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
image= cv2.imread("test.jpg")
plt.imshow(image)
gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
haar_face_cascade = cv2.CascadeClassifier('opencv-master\data\haarcascades\haarcascade_frontalface_alt.xml')
faces= haar_face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5);
print("Faces found: ", len(faces))
for (x, y, w, h) in faces:     
         cv2.rectangle(test1, (x, y), (x+w, y+h), (0, 255, 0), 2)

plt.imshow(convertToRGB(image))
