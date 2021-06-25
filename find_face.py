#C:/Users/user/Desktop/OpenCV/CV2/DATA/
import cv2
cascade=cv2.CascadeClassifier('C:/Users/user/Desktop/OpenCV/CV2/DATA/haarcascades/haarcascade_frontalface_alt.xml')
def find_face(img):
    copy=img.copy()
    faces = cascade.detectMultiScale(copy, scaleFactor=None, minNeighbors = None)
    for (x,y,w,h) in faces:
        cv2.rectangle(copy,(x,y),(x+w,y+h),(255,255,0),3)
    return copy,len(faces)

if __name__=="__main__":
    pass