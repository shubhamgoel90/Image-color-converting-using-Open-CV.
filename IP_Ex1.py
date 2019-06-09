import cv2
#import numpy as np

img = cv2.imread("lena.jpg",0)

ret, th = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
ret, th1 = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Hello World1",img)
cv2.imshow("Hello World2",th)
cv2.imshow("Hello World3",th1)

cv2.waitKey(0)

cv2.destroyAllWindows()



