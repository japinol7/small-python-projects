import speech_recognition as sr


class UnknownValueError(Exception):
    pass


class RequestError(Exception):
    pass


def get_recognizer():
    return sr.Recognizer()


def get_microphone_audio(recognizer, show_all=False):
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        response = recognizer.recognize_google(audio, show_all=show_all)
        return response
    except sr.UnknownValueError:
        raise UnknownValueError("Error! UnknownValueError!")
    except sr.RequestError:
        raise RequestError("Error! RequestError!")


if __name__ == '__main__':
    res = get_microphone_audio(sr.Recognizer())
    print(res)
