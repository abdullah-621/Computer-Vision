import cv2

### 1. convert color img to gray scale

# img = cv2.imread("resources\profile.png")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# print(img.shape)
# print(img_gray.shape)

# cv2.imshow("Output rgb : ", img)
# cv2.imshow("Output gray : ", img_gray)
# cv2.waitKey(0)


### 2. convert color img to blur scale

# img = cv2.imread("resources\seu.png")
# # img = cv2.resize(img, (600, 400))
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_blur = cv2.GaussianBlur(img, (7,7), 0)

# print(img.shape)
# print(img_gray.shape)
# print(img_blur.shape)

# cv2.imshow("Originl img : ", img)
# cv2.imshow("gray img : ", img_gray)
# cv2.imshow("blur img : ", img_blur)

# cv2.waitKey(0)



### 3. convert color img to canny image

img = cv2.imread("resources\profile.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img, (7,7), 0)
img_canny = cv2.Canny(img_blur, 100, 100)

print(img.shape)
print(img_gray.shape)
print(img_blur.shape)
print(img_canny.shape)

cv2.imshow("Originl img : ", img)
cv2.imshow("gray img : ", img_gray)
cv2.imshow("blur img : ", img_blur)
cv2.imshow("Canny img : ", img_canny)

cv2.waitKey(0)