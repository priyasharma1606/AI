import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("nn.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(img_gray,1.1,5)
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(img,"PERSON",(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
cv2.imshow("FACE DECTION",img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
