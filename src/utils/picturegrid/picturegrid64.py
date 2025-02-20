# https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
# https://www.geeksforgeeks.org/concatenate-images-using-opencv-in-python/
# https://realpython.com/python-sleep/
# https://learnopencv.com/image-resizing-with-opencv/

from cv2 import *
import time
  
cam_port = 0
cam = VideoCapture(cam_port)


images = []

for i in range(64):
    result, image = cam.read()
    images.append(image)
    time.sleep(1)

# horizontally concatenates images
# of same height 
image_h1 = hconcat([images[0], images[1], images[2], images[3], images[4], images[5], images[6], images[7]])
image_h2 = hconcat([images[8], images[9], images[10], images[11], images[12], images[13], images[14], images[15]])
image_h3 = hconcat([images[16], images[17], images[18], images[19], images[20], images[21], images[22], images[23]])
image_h4 = hconcat([images[24], images[25], images[26], images[27], images[28], images[29], images[30], images[31]])
image_h5 = hconcat([images[32], images[33], images[34], images[35], images[36], images[37], images[38], images[39]])
image_h6 = hconcat([images[40], images[41], images[42], images[43], images[44], images[45], images[46], images[47]])
image_h7 = hconcat([images[48], images[49], images[50], images[51], images[52], images[53], images[54], images[55]])
image_h8 = hconcat([images[56], images[57], images[58], images[59], images[60], images[61], images[62], images[63]])

# vertically concatenates images 
# of same width 
image_v = vconcat([image_h1, image_h2, image_h3, image_h4, image_h5, image_h6, image_h7, image_h8])

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
