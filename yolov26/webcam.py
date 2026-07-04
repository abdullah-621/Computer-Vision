from ultralytics import YOLO
import cv2

# Load trained model
model = YOLO("best.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Prediction
    results = model(frame)

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    # Show
    cv2.imshow("YOLO Detection", annotated_frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()