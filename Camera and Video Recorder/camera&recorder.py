import cv2

print("""Camera and Video Recorder
    1.Type 0 for using Inbuild Webcam
    2.Type 1 for using External Webcam
    """)
try:
    camera_selection=int(input("Enter your choice (0/1):"))
    while True:
        if camera_selection not in [0,1]:
            print("Enter a valid number between 0 and 1")
            continue
        break
except ValueError:
    print("Enter a valid number")

print("""Enter 1 for Clicking a photograph
Enter 2 for recording a video""")
while True:
    try:
        choice=int(input("Enter your choice between (1/2):"))
        if choice not in [1,2]:
            print("Enter a valid number between (1/2)")
            continue
        break
    except ValueError:
        print("Enter a valid number ")

if choice == 1:
    camera=cv2.VideoCapture(camera_selection)
    print("To save the photograph press 's'")
    print("To quit press 'e'")
    while True:
        ret,frame=camera.read()
        if not ret:
            print("Couldn't access camera")
            break
        cv2.imshow("clicking photograph",frame)

        if cv2.waitKey(1) & 0xFF== ord('s'):
            name=input("Enter the name and format of image:")
            success=cv2.imwrite(name,frame)
            if success:
                print("Image saved successfully...")
            else:
                print("Couldn't save the image")
            break

        elif cv2.waitKey(1) & 0xFF==ord('e'):
            print("Quitting....")
            break
else:
    
    camera=cv2.VideoCapture(camera_selection)
    codec=cv2.VideoWriter_fourcc(*'XVID')
    frame_width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    name=input("Enter the name of video in avi format:")
    recorder=cv2.VideoWriter(name,codec,60,(frame_width,frame_height))
    print("To quit press 'q'")
    
    while True:
        ret,frame=camera.read()
        if not ret:
            print("Couldn't access camera")
            break
       
        recorder.write(frame)
        cv2.imshow("Recording live",frame)

            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("quitting.....")
            break        

        
    recorder.release()
        

camera.release()
cv2.destroyAllWindows()
