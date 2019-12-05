from PIL import Image
import PIL.Image

from pytesseract import image_to_string
import pytesseract
from date_extractor import extract_date
def ocr_core(filename):
	pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
	TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'
	output = pytesseract.image_to_string(PIL.Image.open(filename).convert("RGB"), lang='eng')
	result=output.strip()
	date,precision=extract_date(result, return_precision=True)
	dictionary={'date':date}
	return dictionary
print(ocr_core('C:/Users/samaresh yadav/Downloads/3deff9fb.jpg'))

