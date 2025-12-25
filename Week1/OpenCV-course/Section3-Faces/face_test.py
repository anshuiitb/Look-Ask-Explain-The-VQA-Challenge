import cv2 as cv
import numpy as np

# Load people list (same order as training)
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

# Load Haar cascade
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Load trained LBPH model
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# Read test image
img = cv.imread(r'C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Faces\val\ben_afflek\3.jpg')
if img is None:
    raise IOError("Image not found")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect faces
faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=4
)

for (x, y, w, h) in faces_rect:
    # Crop face from GRAYSCALE
    face_roi = gray[y:y+h, x:x+w]

    # Resize exactly like training
    face_roi = cv.resize(face_roi, (200, 200))
    face_roi = np.ascontiguousarray(face_roi, dtype=np.uint8)

    # Predict
    label, confidence = face_recognizer.predict(face_roi)

    print(f"Predicted: {people[label]} | Confidence: {confidence:.2f}")

    # Draw rectangle and label
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.putText(
        img,
        f"{people[label]} ({confidence:.1f})",
        (x, y-10),
        cv.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

cv.imshow('Prediction', img)
cv.waitKey(0)
cv.destroyAllWindows()
