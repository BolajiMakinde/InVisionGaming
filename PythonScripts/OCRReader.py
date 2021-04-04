# credit goes to https://www.youtube.com/watch?v=4DrCIVS5U3Y 'AllTech' YouTube Channel for Starter Code
# credit goes to https://www.youtube.com/watch?v=Jvf5y21ZqtQ 'sentdex' YouTube Channel for webcam support
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import os.path
import time
#from picamera import Picamera
import cv2
import numpy as np
from PIL import Image
from PIL import ImageGrab

#for speaking without interrupts
import threading

import pyttsx3

OCRSpeech = True

readRate = 1

# 0 for male voice and 1 for female voice
VoiceType = 1

engine = pyttsx3.init()
voices = engine.getProperty('voices')

Screen_Capture = True
Use_GrayScale = True

bbCoordPath = 'C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/HapticState/screenCoordinates.txt'

def speakText(text):
    engine.setProperty('voice', voices[VoiceType].id)
    engine.say(text)
    engine.runAndWait()

if Screen_Capture == True:
    while True:
        img = ImageGrab.grab()
        img.save('reader.png')
        f = open(bbCoordPath, 'r')
        width = int(f.readline())
        height = int(f.readline())
        top = int(f.readline())
        left = int(f.readline())
        f.close()
        img = img.crop((left,top,left+width,top+height))
        img.save('readerCropped.png')

        #cv2.imshow('InVision Gaming Screen Capture', img)
        if readRate > 0 or (readRate <= 0 and cv2.waitKey(1) & 0xFF==ord('r')):
            if readRate > 0:
                time.sleep(readRate)
            text = tess.image_to_string(img)
            print(text)
            if OCRSpeech == True:
                worker = threading.Thread(target = speakText(text))
                worker.start()
                worker.join()

else:
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if Use_GrayScale == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('InVision Gaming WebCam', frame)
        if readRate > 0 or (readRate <= 0 and cv2.waitKey(1) & 0xFF == ord('r')):
            if readRate > 0:
                time.sleep(readRate)
            print('Reading ...')
            status = cv2.imwrite('reader.png',frame)
            #print("Image written to file-system : ",status)
            img = Image.open(os.path.dirname(__file__) + '/../reader.png')
            text = tess.image_to_string(img)
            print(text)
            if OCRSpeech == True:
                worker = threading.Thread(target = speakText(text))
                worker.start()
                worker.join()

    cap.release()
    cv2.destroyAllWindows()


#img = Image.open(os.path.dirname(__file__) + '/../logo.png')

#with picamera.PiCamera() as camera:
#    camera.resolution = (1024, 768)
#    camera.start_preview()
#    time.sleep(2)
#    camera.capture(foo.jpg)
#img = Image.open(foo.jpg)
#text = tess.image_to_string(img)

#print(text)