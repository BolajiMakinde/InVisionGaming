# credit goes to https://www.youtube.com/watch?v=4DrCIVS5U3Y AllTech Youtube Channel for Starter Code
import pytesseract as tess
import os.path
from PIL import Image

img = Image.open(os.path.dirname(__file__) + '/../logo.png')

text = tess.image_to_string(img)

print(text)