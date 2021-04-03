# credit goes to https://www.youtube.com/watch?v=4DrCIVS5U3Y AllTech Youtube Channel for Starter Code
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import os.path
import time
#from picamera import Picamera
import cv2
import numpy as np
from PIL import Image
from PIL import ImageGrab

Screen_Capture = False

if Screen_Capture == True:
    img = ImageGrab.grab()
else:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
#img = Image.open(os.path.dirname(__file__) + '/../logo.png')

#with picamera.PiCamera() as camera:
#    camera.resolution = (1024, 768)
#    camera.start_preview()
#    time.sleep(2)
#    camera.capture(foo.jpg)
#img = Image.open(foo.jpg)
#text = tess.image_to_string(img)

#print(text)