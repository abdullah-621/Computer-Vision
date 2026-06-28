import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

img[:] = 255, 0, 0


### cretae a line
cv2.line(img, (0,0), (300, 400), (0, 255, 0), 5)


### Rectengle
cv2.rectangle(img, (100, 50), (300, 400), (0, 0, 255), 5)

### Circle
cv2.circle(img, (400, 300), 50, (0, 0, 255), 4)


### put texts
cv2.putText(img, "ABDULLAH", (200, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)


cv2.imshow("img",img)
cv2.waitKey(0)