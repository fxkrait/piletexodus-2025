# https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
# from cv2 import *

# https://stackoverflow.com/questions/71454786/nameerror-name-videocapture-is-not-defined
from cv2 import (VideoCapture, namedWindow, imshow, waitKey, destroyWindow, imwrite)

cam_port = 0
cam = VideoCapture(cam_port)
result, image = cam.read()
  
if result:  
    imwrite("GeeksForGeeks.png", image)
  
else:
    print("Error!")
