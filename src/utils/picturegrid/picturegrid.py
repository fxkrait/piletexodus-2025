# https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
# https://www.geeksforgeeks.org/concatenate-images-using-opencv-in-python/
# https://realpython.com/python-sleep/
# https://learnopencv.com/image-resizing-with-opencv/

from cv2 import *
import time
  
cam_port = 0
cam = VideoCapture(cam_port)

result1, image1 = cam.read()
time.sleep(1)
result2, image2 = cam.read()
time.sleep(1)
result3, image3 = cam.read()
time.sleep(1)
result4, image4 = cam.read()
time.sleep(1)
result5, image5 = cam.read()
time.sleep(1)
result6, image6 = cam.read()
time.sleep(1)
result7, image7 = cam.read()
time.sleep(1)
result8, image8 = cam.read()

# horizontally concatenates images
# of same height 
image_h = hconcat([image1, image2, image3, image4, image5, image6, image7, image8])

# vertically concatenates images 
# of same width 
image_v = vconcat([image_h, image_h, image_h, image_h, image_h, image_h, image_h, image_h])

imwrite("image.png", image_v)


# let's downscale the image using new  width and height
down_width = 600
down_height = 600
down_points = (down_width, down_height)
image_600x600 = resize(image_v, down_points, interpolation=INTER_LINEAR)
imwrite("image_600x600.png", image_600x600)


# let's downscale the image using new  width and height
down_width = 400
down_height = 400
down_points = (down_width, down_height)
image_400x400 = resize(image_v, down_points, interpolation=INTER_LINEAR)
imwrite("image_400x400.png", image_400x400)


# let's downscale the image using new  width and height
down_width = 200
down_height = 200
down_points = (down_width, down_height)
image_200x200 = resize(image_v, down_points, interpolation=INTER_LINEAR)
imwrite("image_200x200.png", image_200x200)
