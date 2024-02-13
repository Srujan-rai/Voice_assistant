import cv2
import easyocr

cap=cv2.VideoCapture(0)
while True:
    Success,frame=cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(0) & ord('q')==0XFF:
        break
    
