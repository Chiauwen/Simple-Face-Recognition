import cv2
import face_recognition

image = cv2.imread("blackpink.jpeg")

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

face_locations = face_recognition.face_locations(rgb_image)

number = len(face_locations)

for face_location in face_locations:
    top, right, bottom, left = face_location
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 3)
    
text = f"Number of faces detected: {len(face_locations)}"
cv2.putText(image, text, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("Face Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
