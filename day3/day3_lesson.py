import cv2

img = cv2.imread('../day2/lena.png')

for b in range(img.shape[0]):
    for g in range(img.shape[1]):
        for r in range(img.shape[2]):
            img[b,g,r] = np.clip()