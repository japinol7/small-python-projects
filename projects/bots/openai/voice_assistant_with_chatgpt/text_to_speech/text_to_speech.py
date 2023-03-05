import time

import gtts
from pygame import mixer
import tempfile

from config.config import AUDIO_FILE_EXT


def init_music_mixer():
    mixer.init()


def is_music_busy():
    return mixer.music.get_busy()


def play_text_to_speech(text, lang):
    tts = gtts.gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(suffix=AUDIO_FILE_EXT, delete=False) as f:
        filename = f.name
        tts.write_to_fp(f)
    mixer.music.load(filename)
    mixer.music.play()


if __name__ == '__main__':
    from config.config import LANGUAGE

    init_music_mixer()
    play_text_to_speech("I'm listening, cutie!", LANGUAGE)
    time.sleep(2)
