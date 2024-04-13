
#from gtts import gTTS

#def text_to_speech(text, language='en', slow=False, filename='output.wav'):
 
  #  tts = gTTS(text, lang=language, slow=slow)
    #tts.save(filename)
#my_text = "Welcome to the app!"
#target_language = 'en' 
#text_to_speech(my_text, language=target_language, slow=False, filename='output.wav')


from translate import Translator
from gtts import gTTS
import os
import pygame

def eng_to_speech(text, language='en', slow=False, filename='eng.mp3'):
 
    tts = gTTS(text, lang=language, slow=slow)
    tts.save(filename)
def translate_to_malayalam(text):
   
    translator = Translator(to_lang="ml")
    translated_text = translator.translate(text)
    return translated_text

def mal_to_speech(text, filename='mal.mp3'):
   
    tts = gTTS(text=text, lang='ml')
    tts.save(filename)
def play_audio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
def text_speech(english_text):
    #english_text = "How many sacks of rice were sold yesterday?"
    malayalam_text = translate_to_malayalam(english_text)
    print("Translated Malayalam text:", malayalam_text)

    mal_to_speech(malayalam_text)  
    # play_audio('mal.mp3')
    eng_to_speech(english_text, language='en', slow=False, filename='eng.mp3')
    # play_audio('eng.mp3')
text_speech("How many sacks of rice were sold yesterday?")

