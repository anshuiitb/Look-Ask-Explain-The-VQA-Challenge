import cv2 as cv

# Load Haar cascade
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Start webcam (0 = default camera)
capture = cv.VideoCapture(0)

if not capture.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces
    faces_rect = haar_cascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=6
    )

    # Draw rectangles around faces
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show webcam output
    cv.imshow('Webcam Face Detection', frame)

    # Press 'q' to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
capture.release()
cv.destroyAllWindows()
