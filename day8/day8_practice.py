import cv2
import numpy as np

img = cv2.imread('../day2/lena.png')
img_blur = cv2.GaussianBlur(img, (3,3), 1)

img_show = np.hstack((img, img_blur))
# while True:
#     cv2.imshow('blur', img_show)
#     k = cv2.waitKey(0)
#     if k == 27:
#         cv2.destroyAllWindows()
#         break

cv2.imshow('blur', img_show)
cv2.waitKey(0)    
cv2.destroyAllWindows()