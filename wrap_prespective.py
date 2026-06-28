import cv2
import numpy as np

width, height = 250, 350

img = cv2.imread("resources/cards.jpg")


pts1 = np.float32([
    [230, 61],   # Top Left
    [416, 134],   # Top Right
    [137, 310],   # Bottom Left
    [309 ,382]    # Bottom Right
])

pts2 = np.float32([
    [0,0],
    [width,0],
    [0,height],
    [width,height]
])

metrix = cv2.getPerspectiveTransform(pts1, pts2)
img_out = cv2.warpPerspective(img, metrix, (width, height))

cv2.imshow('cards', img)
cv2.imshow('cards_wrap', img_out)

cv2.waitKey(0)
cv2.destroyAllWindows()


# import cv2

# img = cv2.imread("resources/cards.jpg")

# def mousePoints(event, x, y, flags, params):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x, y)
#         cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)

# while True:
#     cv2.imshow("Image", img)
#     cv2.setMouseCallback("Image", mousePoints)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()