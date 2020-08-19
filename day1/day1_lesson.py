import cv2

img = cv2.imread('RAA_dc.png')
# print(type(img))
cv2.imshow('', img)
cv2.waitKey(0) #& 0xFF
# if key==27:
cv2.destroyAllWindows()