import cv2
img=cv2.imread("C:\\Users\\91630\\OneDrive\\Pictures\\Camera Roll\\WIN_20210818_14_13_52_Pro.jpg",1)
#print(img)
#print(type(img))
#print(img.shape)
#for displaying image
resize_img=cv2.resize(img,(200,300))
cv2.imshow("Siri",resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()