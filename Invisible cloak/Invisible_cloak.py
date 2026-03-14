import cv2
import numpy as np

camera_mode=int(input("Enter 0 for internal webcam and 1 for external webcam: "))
if not (camera_mode==0 or camera_mode==1):
    print("Invalid input. Defaulting to internal webcam.")
    camera_mode=0
cloak_color=input("Enter the color of the cloak (red, green, blue): ").lower()
if not (cloak_color in ['red', 'green', 'blue']):
    print("Invalid input. Defaulting to red.")
    cloak_color='red'
def get_mask(cloak_color, hsv):
    if cloak_color=='red':
        lower_red=np.array([0,120,70])
        upper_red=np.array([10,255,255])
        mask1=cv2.inRange(hsv,lower_red,upper_red)
        lower_red1=np.array([170,120,70])
        upper_red1=np.array([180,255,255])
        mask2=cv2.inRange(hsv,lower_red1,upper_red1)
        mask=mask1+mask2
        return mask
    elif cloak_color=='green':
        lower_green=np.array([36,25,25])
        upper_green=np.array([86,255,255])
        mask= cv2.inRange(hsv,lower_green,upper_green)
        return mask
    elif cloak_color=='blue':
        lower_blue=np.array([94,80,2])
        upper_blue=np.array([126,255,255])
        mask=cv2.inRange(hsv,lower_blue,upper_blue)
        return mask
    else:
        print("Invalid color. Defaulting to red.")
        return get_mask('red', hsv)
    

cap=cv2.VideoCapture(camera_mode)

for i in range(120):
    ret,background=cap.read()    
background=np.flip(background,axis=1)
print("Background captured successfully. Starting cloak effect...")

while(cap.isOpened()):
    ret,frame=cap.read()
    if not ret:
        break
    frame=np.flip(frame,axis=1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=get_mask(cloak_color, hsv)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    mask=cv2.dilate(mask,np.ones((3,3),np.uint8),iterations=1)

    cloak_area=cv2.bitwise_and(background,background,mask=mask)
    non_cloak_area=cv2.bitwise_and(frame,frame,mask=cv2.bitwise_not(mask))
    final_output=cv2.addWeighted(cloak_area,1,non_cloak_area,1,0)
    cv2.imshow('cloak',final_output)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()