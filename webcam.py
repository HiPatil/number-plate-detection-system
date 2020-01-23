import pytesseract
import cv2
from PIL import Image
import numpy as np
from project import *
import time
from reg import check_plate 

def nothing():
    pass
    
cap = cv2.VideoCapture(0)
plate = np.zeros((10,10))
plate_number_list = {}
unauthorised = ['AP 45 MA 9607']
detected_unauthorised = []
# cv2.namedWindow('dilate')
cv2.namedWindow('plate')
cv2.createTrackbar('w','plate',0,500,nothing)
cv2.createTrackbar('h','plate',0,500,nothing)
cv2.createTrackbar('w1','plate',0,500,nothing)
cv2.createTrackbar('h1','plate',0,500,nothing)
cv2.createTrackbar('dilate','dilate',0,10,nothing)
i = 0
while(True):
	ret, img = cap.read()
	img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 
	copy = cv2.copyMakeBorder(img,0,0,0,0,cv2.BORDER_REPLICATE)
	copy2 = cv2.copyMakeBorder(img,0,0,0,0,cv2.BORDER_REPLICATE)
	#img = cv2.GaussianBlur(img,(9,9),0)

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	th = cv2.inRange(img,(140,140,140), (255,255,255) ,cv2.THRESH_BINARY)
	th = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
	ret2,frame_threshold = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	
	iter_val = cv2.getTrackbarPos('dilate','dilate')
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,8)) 
	frame_morphed = cv2.dilate(frame_threshold,kernel,iterations = 1)
	#cv2.imshow('dilate',frame_morphed)
	
	cnts, hierarchy = cv2.findContours(frame_morphed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	
	
	height = cv2.getTrackbarPos('h','plate')
	width = cv2.getTrackbarPos('w','plate')
	height1 = cv2.getTrackbarPos('h1','plate')
	width1 = cv2.getTrackbarPos('w1','plate')
	
	for cnt in cnts:
		x,y,w,h = cv2.boundingRect(cnt)
		if 21<h<36 and 88<w<276:	# Use distance and size information
			cv2.rectangle(img,(x-4,y-4),(x+w+4,y+h+4),(0,255,0),-1)
			th = cv2.inRange(img,(0,250,0), (1,255,1) ,cv2.THRESH_BINARY)
			c, hier = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
			for con in c:
				x1,y1,w1,h1 = cv2.boundingRect(con)
				if w1 > 150:
					cv2.rectangle(copy,(x1,y1),(x1+w1,y1+h1),(255,255,0),2)
					plate = copy2[y1:y1+h1,x1:x1+w1]
					# print('plates found')
					
	if i%25 ==0:
		x = str(pytesseract.image_to_string(plate))
		if x in unauthorised and x not in detected_unauthorised:
			print("Unauthorised, ",x) 
			buzzer()
			detected_unauthorised.append(x)
		elif x not in plate_number_list and check_plate(x) and x not in unauthorised:
			localtime = time.asctime( time.localtime(time.time()) )
			plate_number_list[x] = localtime
			print(plate_number_list)
			open_gate()

	i+=1
	try:
 		cv2.imshow('final_detected', copy)		
	except:
		pass
	cv2.imshow('plate', img)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		with open('detected_plates.txt', 'w') as f:
			for key in plate_number_list.keys():
				f.write("Number Plate: %s || Date and Time: %s\n"%(key,plate_number_list[key]))
		break
        
cap.release()
cv2.destroyAllWindows()
