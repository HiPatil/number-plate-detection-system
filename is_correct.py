import cv2
import numpy as np

img = cv2.imread('/home/himanshu/dl/number_plate_detection/Enet/test/5.jpg',0)
mask = cv2.imread('/home/himanshu/dl/number_plate_detection/Enet/mask_test/5_predict.png',0)
mask = cv2.resize(mask, (img.shape[1],img.shape[0]))
masked = cv2.bitwise_and(img,mask)
cv2.imshow('img', masked)
cv2.waitKey(0)
cv2.destroyAllWindows()