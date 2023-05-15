#pip install opencv-python
#haarcascade_frontalface_default.xml

import cv2

cascade_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCature(0)

while True:
    ret, frame = cap.read()
    print(ret)
    g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    f = cascaade_face.detectMultiScale(g, 1.3, 5)

    for(x, y, w, h) in f:
        cv2.rectangle(img, (x,y), (x + w, y + h), (0,0,225), 4)


    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27;
        break

cap.release()
cv2.destroyAllWindows()        
    
