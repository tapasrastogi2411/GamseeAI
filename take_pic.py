import cv2
import numpy as np


cascade1 = cv2.CascadeClassifier('xcascade.xml')
cascade2 = cv2.CascadeClassifier('ycascade.xml')

def TakeSnapAndSave():
    cap = cv2.VideoCapture(0)

    num = 0
    while num<1000:
        ret, img = cap.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        object1 = xcascade.detectMultiScale(gray, 10, 10)
        for(x,y,w,h) in object1:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.rectangle(img,(x,y), (x+w,y+h),(255,255,0),5)
            cv2.putText(img, 'Something',(x,y-40), font, 1.5, (255,255,0),5, cv2.LINE_AA)
            object2 = ycascade.detectMultiScale(gray, 15, 15)
            for(x,y,w,h) in object2:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.rectangle(img,(x,y), (x+w,y+h),(0,255,255),5)
                cv2.putText(img, 'Something Else',(x+100,y+80), font, 0.8, (0,0,255),2, cv2.LINE_AA)        
                cv2.imwrite('opencv'+str(num)+'.jpg',img)
                num = num+1
                
    cap.release()
    cv2.destroyAllWindows()
