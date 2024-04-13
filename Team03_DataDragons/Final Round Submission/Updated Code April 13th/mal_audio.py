import speech_recognition as sr
from googletrans import Translator
from deep_translator import GoogleTranslator

def recognize_and_translate_malayalam(audio_file_path):
    
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    malayalam_text = recognizer.recognize_google(audio_data, language="ml-IN")
    print(malayalam_text)

    
    # translator = Translator()
    # translated_text = translator.translate(malayalam_text, src="en")

    translated = GoogleTranslator(source='auto', target="en").translate(malayalam_text)

    return translated

# translated_text = recognize_and_translate_malayalam("audio.wav")
# print("Translated Text:", translated_text)