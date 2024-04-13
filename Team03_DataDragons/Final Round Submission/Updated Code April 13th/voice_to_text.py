import speech_recognition as sr

def voice_to_text(sound):

    # sound="recorded.wav"

    r=sr.Recognizer()

    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)

        # print("Converting audio file to text...")

        audio=r.listen(source)

        try:
            return r.recognize_google(audio)

        except Exception as e:
            print(e)
     

