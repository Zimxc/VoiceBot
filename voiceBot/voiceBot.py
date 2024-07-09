import speech_recognition as sr

recognizer = sr.Recognizer()


def capture_voice_input():
    with sr.Microphone() as sourse:
        print('Listening...')
        audio = recognizer.listen(sourse)    
        
    return audio


def convert_voice_to_text(audio):
    try:
        text =recognizer.recognize_google(audio)
        print('You said:  '+ text)
    except sr.UnknownValueError:
        text = ''
        print('-_-')
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text

def main():
    audio = capture_voice_input()
    text = convert_voice_to_text(audio)

if __name__ == '__main__':
    main()