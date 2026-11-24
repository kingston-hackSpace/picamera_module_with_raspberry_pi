from picamera2 import Picamera2, Preview
from libcamera import Transform
#import time
#import numpy as np
import cv2
#time.sleep(5)
picam2 = Picamera2()
#video_config = picam2.create_video_configuration()
#capture_config = picam2.create_still_configuration()
picam2.start_preview(Preview.QTGL)
config = picam2.create_preview_configuration()
picam2.configure(config)
picam2.start()

#array = picam2.capture_array("main")

#img = np.zeros((480,640,3),np.uint8)

#horizontal_divisions = 23
#vertical_divisions = 24

#def average_value(x0,x1,y0,y1):
#	total = 0
#	val = 0
#	for i in range (int(x0), int (x1)-1,25):
#		for j in range (int(y0), int (y1)-1,25):
#			val = array[j,i,0]
#			total = val+ total
#	return (total*625)/((x1-x0)*(y1-y0))
while(1):
#	array = picam2.capture_array("main")
#	for i in reversed(range(horizontal_divisions)):
#		for j in reversed(range(vertical_divisions)):
#			x0 = (640) * (i/horizontal_divisions)
#			x1 = (640) * ((i+1)/horizontal_divisions)
#			y0 = (480) * (j/vertical_divisions)
#			y1 = (480) * ((j+1)/vertical_divisions)
#			cv2.rectangle (img, (int(x0), int(y0)) , (int(x1),int(y1)), (0,0,(average_value(x0,x1,y0,y1))),-1)
#		time.sleep(0.04)
#	cv2.imshow("image", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


picam2.switch_mode(preview_config)
#img = np.zeros((480,640,3), np.uint8)
#cv2.rectangle(img, (0,0),(200,200),(255,0,0),-1)
#cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
