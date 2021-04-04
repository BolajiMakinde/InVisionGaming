# credit goes to https://www.youtube.com/watch?v=4DrCIVS5U3Y 'AllTech' YouTube Channel for Starter Code
# credit goes to https://www.youtube.com/watch?v=Jvf5y21ZqtQ 'sentdex' YouTube Channel for webcam support
# credit goes to https://github.com/KingArnaiz/Object-Detection-Tutorial for object detection scripts for chess
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import os.path
import time
#from picamera import Picamera
import cv2
import numpy as np
from PIL import Image
from PIL import ImageGrab
#import pixelSummer;

#for speaking without interrupts
import threading

import pyttsx3

playingLichess = False
lichessBoard = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
useLetterPieceSet = True
useImageEnhancement = True
def countPixels(path = 'C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/f3.png', r=255,g=255,b=255):
    img = Image.open(path)
    w,h = img.size
    colors = img.getcolors(w*h)
    colordict = { x[1]:x[0] for x in colors }
    white_pixels_count = colordict.get((r,g,b))
    #print(white_pixels_count)
    return white_pixels_count

OCRSpeech = True

readRate = 1

# 0 for male voice and 1 for female voice
VoiceType = 1

engine = pyttsx3.init()
voices = engine.getProperty('voices')

Screen_Capture = True
Use_GrayScale = True

bbCoordPath = 'C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/HapticState/screenCoordinates.txt'
offsetPath = 'C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/HapticState/offsets.txt'
readFreqPath = 'C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/HapticState/readFrequency.txt'
inputTypePath = 'C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/HapticState/inputType.txt'
hapticPath = 'C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/HapticState/test.txt'
defaultPath = 'C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/HapticState/test.txt'

inputType = 'OCR'

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
        f = open(offsetPath, 'r')
        offset_top = int(f.readline())
        offset_left = int(f.readline())
        offset_width = int(f.readline())
        offset_height = int(f.readline())
        f.close()
        f1 = open(readFreqPath, 'r')
        readRate = int(f1.readline())
        f1.close()
        f = open(inputTypePath)
        inputType = f.readline()
        f.close()
        img = img.crop((left+offset_left,top+offset_top,left+width+offset_width,top+height+offset_height))
        img.save('readerCropped.png')
        if inputType == "Text to Speech":
            OCRSpeech = True
        else:
            OCRSpeech = False
            playingLichess = True
        if inputType == 'Lichess (Lichess.com)':
            playingLichess = True
        else:
            pass
            #playingLichess = False
        #print(inputType)
        #cv2.imshow('InVision Gaming Screen Capture', img)
        if readRate > 0 or (readRate <= 0 and cv2.waitKey(1) & 0xFF==ord('r')):
            if readRate > 0:
                time.sleep(readRate)
            #print('here3')
            #print('Playing Lichess is: ' + str(playingLichess))
            if playingLichess == True:
                lichessBoard = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
                for x in range(8):
                    for y in range(8):
                        sqr = img.crop(((img.width/8)*x,(img.height/8)*y,(img.width/8)*x+(img.width/8), (img.height/8)*y+(img.height/8)))
                        if useImageEnhancement == True:
                            pass
                        increaseContrast = False
                        if increaseContrast == True:
                            lab = cv2.cvtColor(sqr, cv2.COLOR_BGR2LAB)
                            l, a, b = cv2.split(lab)
                            clache = cv2.createCLAHE(clipLimit - 3.0, tileGridSize=(8,8))
                            cl = clache.apply(l)
                            limg = cv2.merge((cl,a,b))
                            final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
                            sqr = final
                        sqr.save('C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/'+str(chr(x+ord('a')))+ str(8-y)+'.png')
                        
                        # 0 for empty square 
                        ''' braile
                        00
                        00
                        00
                        '''


                        # 1 for pawn
                        ''' braile
                        11
                        10
                        10
                        '''
                        # 2 for knight

                        ''' braile
                        11
                        01
                        10
                        '''
                        # 3 for bishop

                        ''' braile
                        10
                        10
                        00
                        '''
                        # 4 for rook
                        ''' braile
                        10
                        11
                        10
                        '''
                        # 5 for queen
                        ''' braile
                        11
                        11
                        10
                        '''
                        # 6 for king
                        ''' braile
                        10
                        00
                        10
                        '''
                        # -(negative) for black
                        '''braile
                        lower right corner is 1
                        00
                        00
                        0(1)
                        '''
                        # +(positive) for white
                        '''braile
                        lower right corner is 0
                        00
                        00
                        0(0)
                        '''
                        #newsqr = cv2.imread('C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/'+str(chr(x+ord('a')))+ str(8-y)+'.png')
                        #newsqr = cv2.cvtColor(newsqr, cv2.COLOR_GRAY2BGR)
                        #text = tess.image_to_string(newsqr)
                        #print(text)
                        #print(str(x) + ", " + str(7-y))
                        if countPixels('C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/'+str(chr(x+ord('a')))+ str(8-y)+'.png') == 635:
                            lichessBoard[x][7-y] = 1
                        elif countPixels('C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/'+str(chr(x+ord('a')))+ str(8-y)+'.png') == 1895:
                            lichessBoard[x][7-y] = 2
                        elif countPixels('C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/'+str(chr(x+ord('a')))+ str(8-y)+'.png') == 1105:
                            lichessBoard[x][7-y] = 3
                        elif countPixels('C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/'+str(chr(x+ord('a')))+ str(8-y)+'.png') == 1469:
                            lichessBoard[x][7-y] = 4
                        elif countPixels('C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/'+str(chr(x+ord('a')))+ str(8-y)+'.png') == 1427:
                            lichessBoard[x][7-y] = 5
                        elif countPixels('C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/'+str(chr(x+ord('a')))+ str(8-y)+'.png') == 1925:
                            lichessBoard[x][7-y] = 6
                        elif countPixels('C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/'+str(chr(x+ord('a')))+ str(8-y)+'.png') == 188:
                            lichessBoard[x][7-y] = -2
                        elif countPixels('C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/'+str(chr(x+ord('a')))+ str(8-y)+'.png') == 177:
                            lichessBoard[x][7-y] = -3
                        elif countPixels('C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/'+str(chr(x+ord('a')))+ str(8-y)+'.png') == 196:
                            lichessBoard[x][7-y] = -4
                        elif countPixels('C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/'+str(chr(x+ord('a')))+ str(8-y)+'.png') == 240:
                            lichessBoard[x][7-y] = -5
                        elif countPixels('C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/'+str(chr(x+ord('a')))+ str(8-y)+'.png') == 533:
                            lichessBoard[x][7-y] = -6
                        elif countPixels('C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/'+str(chr(x+ord('a')))+ str(8-y)+'.png',2,2,2) == None:
                            lichessBoard[x][7-y] = 0
                        else:
                            lichessBoard[x][7-y] = -1
                #print (lichessBoard)
                #rn = 0
                lichessBoard = np.array(list(zip(*lichessBoard)))[::-1]
                rn = 0
                hapticr = open(defaultPath, "r")
                hapticw = open(hapticPath, "w").close()
                hapticw = open(hapticPath, "w")
                for row in lichessBoard:
                    print(row)
                    str1 = ""
                    str2 = ""
                    str3 = ""
                    for num in row:
                        if num == 0:
                            str1 += "00"
                            str2 += "00"
                            str3 += "00"
                        if num == 1:
                            str1 += "11"
                            str2 += "10"
                            str3 += "10"
                        if num == 2:
                            str1 += "11"
                            str2 += "01"
                            str3 += "10"
                        if num == 3:
                            str1 += "10"
                            str2 += "10"
                            str3 += "00"
                        if num == 4:
                            str1 += "10"
                            str2 += "11"
                            str3 += "10"
                        if num == 5:
                            str1 += "11"
                            str2 += "11"
                            str3 += "10"
                        if num == 6:
                            str1 += "10"
                            str2 += "00"
                            str3 += "10"
                        if num == -6:
                            str1 += "10"
                            str2 += "00"
                            str3 += "11"
                        if num == -5:
                            str1 += "11"
                            str2 += "11"
                            str3 += "11"
                        if num == -4:
                            str1 += "10"
                            str2 += "11"
                            str3 += "11"
                        if num == -3:
                            str1 += "10"
                            str2 += "10"
                            str3 += "01"
                        if num == -2:
                            str1 += "11"
                            str2 += "01"
                            str3 += "11"
                        if num == -1:
                            str1 += "11"
                            str2 += "10"
                            str3 += "11"
                    str1 += '\n'
                    str2 += '\n'
                    str3 += '\n'
                    hapticw.write(str1 + str2+ str3)
                    #haptic = open(hapticPath, "r")
                    #print(str(rn))
                    #all_lines[(rn*3)] = str1
                    #all_lines[(rn*3)+1] = str2
                    #all_lines[(rn*3)+2] = str3
                    rn+=1

                    #haptic = open(hapticPath, "w")
                    #hapticw.writelines(all_lines)
                hapticr.close()
                hapticw.close()


                print('---------- new board state ----------')
                '''with open(hapticPath, 'r') as file:
                    data = hapticPath.readlines()
                    for num in row:
                        if num == 1:
                            data[row*3] += '11'
                            data[row*3+1] += '10'
                            data[row*3+2] += '10'

                rn +=1'''
            if OCRSpeech == True:
                text = tess.image_to_string(img)
                print(text)
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