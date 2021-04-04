import cv2
from PIL import Image
def countPixels(path = 'C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/chess(Lichess)States/', r=255,g=255,b=255):
    img = Image.open(path+input()+'.png')
    w,h = img.size
    colors = img.getcolors(w*h)
    colordict = { x[1]:x[0] for x in colors }
    white_pixels_count = colordict.get((r,g,b))
    print(white_pixels_count)
    return white_pixels_count

countPixels()