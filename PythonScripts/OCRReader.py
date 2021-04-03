# credit goes to https://www.youtube.com/watch?v=4DrCIVS5U3Y AllTech Youtube Channel for Starter Code
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import os.path
from PIL import Image

img = Image.open(os.path.dirname(__file__) + '/../logo.png')

text = tess.image_to_string(img)

print(text)