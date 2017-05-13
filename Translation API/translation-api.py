# -*- coding: utf-8 -*-

from google.cloud import translate

def translate_text(text, target='en'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target)
    print('Text: ', result['input'])
    print('\nDetected Source Language: ', result['detectedSourceLanguage'])
    print('\nTranslation: ', result['translatedText'])
    print('\n')

t = '''आपके विचार आपके जीवन का निर्माण करते हैं।  यहाँ संग्रह किये गए महान विचारकों के हज़ारों कथन आपके जीवन में एक सक$

translate_text(t)
