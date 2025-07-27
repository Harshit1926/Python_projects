import cv2
import time
import os

face_cascade=cv2.CascadeClassifier("openCV\CV 4\haarcascade_frontalface_default.xml")
eyes_cascade=cv2.CascadeClassifier("openCV\CV 4\haarcascade_eye.xml")
smile_cascade=cv2.CascadeClassifier("openCV\CV 4\haarcascade_smile.xml")


print("Press 0 for using inbuild webcam and 1 for using external webcam ")
print("To quit press 'q'")
print("# A photo will be captured automatically when you're smiling, and again after 20 seconds if you keep smiling.")

try:
    cam_section=int(input("Enter your choice (0/1):"))
    while True:
        if cam_section not in [0,1]:
            print("Enter a valid number from 0 or 1:")
            continue
        break
except ValueError:
    print("Enter a valid number")

cap=cv2.VideoCapture(cam_section)
cooldown=20
last_photo_time=0

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
        roi_gray= gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]

        eyes=eyes_cascade.detectMultiScale(roi_gray,1.1,10)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),1)

        smile=smile_cascade.detectMultiScale(roi_gray,1.8,30)
        for (sx,sy,sw,sh) in smile:
            cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,255,255),1)
       
        if len(eyes)>0:
            cv2.putText(frame,"Eyes Detected",(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2) 
        if len(smile)>0:
            cv2.putText(frame,"Smile Detected",(x,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
            current_time=time.time()
            if current_time-last_photo_time>cooldown:
                timestamp=time.strftime("%Y-%m-%d %H %M %S")
                filename=f"photo_{timestamp}.jpg"
                success=cv2.imwrite(filename,frame)
                if success:
                    print("photo taken")
                else:
                    print("unable to click photo")
                last_photo_time=current_time     
        
        

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("quitting...")
        break
    cv2.imshow("face detection",frame)
    

cap.release()

cv2.destroyAllWindows()