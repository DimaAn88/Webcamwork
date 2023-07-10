import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0) #create object
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  #size
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
ret, frame = cap.read()  #make photo
cv2.imwrite('../venv/bin/photo1.jpeg', frame)
cap.release()
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A)
image = plt.imread("photo1.jpeg")
plt.figure(figsize=(15,15))
plt.imshow(image)
print(image)
print(image[0][1])