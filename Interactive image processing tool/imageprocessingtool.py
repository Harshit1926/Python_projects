import cv2
import time
import numpy as np
import os

def gray_scale(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return gray

def black_and_white(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    _,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    return thresh

def crop(image):
    print("To you Crop the image you have to enter the point from where you want to crop")
    print("The points are mentioned as x1,y1 and x2,y2")
    print("x1 and x2 are distance from the left corner and y1 and y2 are distance from top")
    print("For your help below are mentioned the dimensions of your image for reference")
    print("x2 should be bigger than x1 and y2 should be bigger than y1")
    h,w=image.shape[:2]
    print(f"Height:{h},Width:{w}")

    x1=int(input("Enter the value of x1:"))
    y1=int(input("Enter the value of y1:"))
    x2=int(input("Enter the value of x2:"))
    y2=int(input("Enter the value of y2:"))
    if x1>=x2 and y1>=y2:
        print("Invalid crop range")
    else:
        cropped_image=image[y1:y2,x1:x2]
    
    return cropped_image

def flipped(image):
    print("For flipping the image vertically type 0")
    print("For flipping the image horizontally type 1")
    print("For flipping the image both vertically and horizontally type -1")
    try:
        choice=int(input("Enter your choice from (0/1/-1):"))
        while True:
            if choice not in [0,1,-1]:
                print("Enter Valid number")
                continue
            break
            
        flipped_image=cv2.flip(image,choice)
    except Exception as e :
        print(f"couldn't flip image due to {e}")

    return flipped_image

def rotation(image):
    angle=int(input("Enter how many degree you want to rotate the image:"))
    height,width=image.shape[:2]
    center=(height//2,width//2)

    rotate=cv2.getRotationMatrix2D(center,angle,1)
    rotated_image=cv2.warpAffine(image,rotate,(width,height))

    return rotated_image

def blur(image):
    blurred_image=cv2.GaussianBlur(image,(3,3),0)
    return blurred_image

def sharpening(image):
    sharpen_kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    sharpen_image=cv2.filter2D(image,-1,sharpen_kernel)

    return sharpen_image

def resize(image):
    new_height=int(input("Enter new height:"))
    new_width=int(input("Enter new width:"))
    new_image=cv2.resize(image,(new_width,new_height))

    return new_image

actions={1:gray_scale,
         2:black_and_white,
         3:crop,
         4:flipped,
         5:rotation,
         6:blur,
         7:sharpening,
         8:resize}

image_path=input("Enter the path of image:").strip().strip('"')
if os.path.isfile(image_path):
    image=cv2.imread(image_path)
    print("""Type 1 to convert into gray scale - shows soft gradients in gray tones
Type 2 to convert into black & white - pure contrast, no shading
Type 3 to crop the image
Type 4 to flip the image
Type 5 to rotate the image
Type 6 to blur image
Type 7 to sharpen the image
Type 8 to resize image""")

    choice=int(input("Enter your choice:"))
    if choice not in actions:
        print("Invalid Choice")
    else:
        image=actions[choice](image)

else:
    print("Unable to find the file")
    
cv2.imshow("Final Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

save=input("Do you want to save image (yes/no):").lower()
timestamp=time.strftime("%y-%m-%d %H %M %S")
filename=f"photo-{timestamp}.jpg"

if save=="yes": 
    success=cv2.imwrite(filename,image)
    if success:
        print("image saved successfully")
    else:
        print("unable to save image")
else:
    print("Thank you for using....")
