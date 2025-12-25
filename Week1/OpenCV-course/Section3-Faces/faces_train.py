import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek' , 'Elton John' , 'Jerry Seinfield' , 'Madonna' , 'Mindy Kaling']

# p=[]
# for i in os.listdir(r'C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Faces\train'):
#         p.append(i)
#
#
#
# print(p)

dir = r'C:\Users\anshu\Ask the image\Week1\OpenCV-course\Resources\Faces\train'

features =[]
labels=[]

haar_cascade = cv.CascadeClassifier('haar_face.xml')

def create_train():
    for person in people:
        path = os.path.join(dir, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray=cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                face_roi = gray[y:y+h, x:x+w]

                face_roi = cv.resize(face_roi, (200, 200))
                face_roi = np.ascontiguousarray(face_roi, dtype=np.uint8)
                features.append(face_roi)
                labels.append(label)




create_train()
print(type(features))
print(type(features[0]))
print(features[0].shape)
print(features[0].dtype)
print(features[0].ndim)
print('Training done ---------------')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
