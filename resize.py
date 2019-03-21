# resize pokeGAN.py
import os
import cv2

WIDTH=256
HEIGHT=256

#haarcascade_frontalface_alt.xml
cascPath = "/home/rasse/anaconda3/pkgs/opencv-3.3.1-py36h0a11808_0/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

src = "./faces" #pokeRGB_black
dst = "./facesResized" # resized

if not os.path.exists(dst):
    os.mkdir(dst)

for each in os.listdir(src):
    img = cv2.imread(os.path.join(src,each))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (ih, iw, ic) = img.shape
    #print("Image h={0}, w={1}, c={2}".format(ih, iw, ic))

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(WIDTH, HEIGHT)
        #flags = cv2.CASCADE_SCALE_IMAGE
    )
    (height, width, channels) = img.shape
    if (len(faces) < 1):
        print("Found no faces for {0}".format(each))
        img2 = img
    else:
        (x, y, w, h) = faces[0]
        #print("Face at {0}, {1}, {2}, {3}".format(x,y,w,h))
        img2 = img[y:y+h, x:x+w]
        if w < WIDTH or h < HEIGHT:
            print("Image to smal W={0}, H={1}".format(w,h))
        else:
            img = cv2.resize(img2,(WIDTH, HEIGHT))
            cv2.imwrite(os.path.join(dst,each), img)
    
