import cv2
face_cascade=cv2.CascadeClassifier("C:\\Users\\91630\\PycharmProjects\\hellosiri\\opencv_tutorial\\haarcascade_frontalface_default.xml")
img=cv2.imread("C:\\Users\\91630\\OneDrive\\Pictures\\Camera Roll\\WIN_20210818_14_13_52_Pro.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
print(type(faces))
print(faces)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()