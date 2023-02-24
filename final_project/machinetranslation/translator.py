'''French to English and English to French Translator using IBM Watson'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['mJ9pLYNGnYblQN5oU_FtsL-e7saapxpzrsbzV67__uvN']
url = os.environ['https://api.us-south.language-translator.watson.cloud.ibm.com/instances/2e7fc3ee-20e8-4418-9d85-32e12078884f']

#Instantiate IBM Watson Language Translator
authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    '''Function translates English string input and return a string output of French'''
    french_text = language_translator.translate(
        text = english_text,
        model_id='en-fr').get_result()
    print(json.dumps(french_text, indent=2,
    ensure_ascii=False))
    return french_text

def french_to_english(french_text):
    '''Function translates French string input and return a string output of English'''
    english_text = language_translator.translate(
        text = french_text,
        model_id='fr-en').get_result()
    print(json.dumps(english_text, indent=2,
    ensure_ascii=False))
    return english_text
