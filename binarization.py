import cv2
import numpy as np
img = cv2.imread('page.jpg',0)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,115,20)
th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 20)
cv2.imshow('original',img)
cv2.imshow('Adaptive thresh gaussian',th)
cv2.imshow('Adaptive thresh mean',th2)
cv2.waitKey(0)
cv2.destroyAllWindows()
