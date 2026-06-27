import cv2

# img read

# img = cv2.imread("resources\profile.png")
# cv2.imshow("Output",img)
# cv2.waitKey(0)


# video read
# cap = cv2.VideoCapture("resources\song.mp4")

# while True:
#   success, img = cap.read()

#   # print(f"{success} {img.shape}")
#   cv2.imshow("Output" ,img)

#   if cv2.waitKey(1) & 0xFF == ord('q'):
#     break


# read webcame

cap = cv2.VideoCapture(0)

cap.set(3, 640)  # width
cap.set(4, 480)  # height

while True:
  success, img = cap.read()
  cv2.imshow("Output :", img)

  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

