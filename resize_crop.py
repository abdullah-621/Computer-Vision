import cv2

### 1. resizing img

# img = cv2.imread("resources\seu.png")
# img_resize = cv2.resize(img, (100, 100))

# cv2.imshow("Original img : ", img)
# cv2.imshow("Crop img : ", img_resize)
# cv2.waitKey(0)


### 1. croping img

img = cv2.imread("resources\seu.png")
img_crop = img[0:100, 200:400]

cv2.imshow("Original img : ", img)
cv2.imshow("Crop img : ", img_crop)
cv2.waitKey(0)