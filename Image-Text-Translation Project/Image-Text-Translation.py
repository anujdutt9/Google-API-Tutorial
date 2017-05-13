# -*- coding: utf-8 -*-

import io
import sys
from google.cloud import translate
from google.cloud import vision


# Function to Read Text from Images
def readText(image):
	vision_client = vision.Client()
	file_name = image

	with io.open(file_name,'rb') as f:
		content = f.read()
		image = vision_client.image(content=content)

	labels = image.detect_labels()

	#print('Image Labels:\n')
	#for l in labels:
	#	print(l.description, l.score)

	#print('\nText in Image:\n')
	#print(image.detect_full_text().text)
	t = image.detect_full_text().text
	return t
	

# Function to return Translated Text
def translate_text(text, target):
	translate_client = translate.Client()
	result = translate_client.translate(text, target_language=target)
	#print('Text: ', result['input'])
    print('\nDetected Source Language: ', result['detectedSourceLanguage'])
	#print('\nTranslation: ', result['translatedText'])
	#print('\n')
	return result['translatedText']
	


# Main Function	
if __name__ == '__main__':
	image_file = str(sys.argv[1])
	print('Reading Text from Image...')

	text_read = readText(image_file)
	print('Text in Image: ', text_read)
	
	print('Enter Language in which you want it to be Translated: ')
	target_lang = input()
	
	translated_text = translate_text(text_read, target_lang)
	print('Text Translation: ', translated_text)
	
# ----------------------- EOC ----------------------------