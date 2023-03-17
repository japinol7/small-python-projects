import time

from config.config import (
    OPENAI_API_KEY_FILE,
    LANGUAGE,
    )
from chatgpt.chatgpt import ChatGPTClient
from text_to_speech.text_to_speech import play_text_to_speech, init_music_mixer, is_music_busy
from tools.utils import utils
from tools.logger import logger
from tools.logger.logger import log
from voice_speech_recognition import voice_speech_recognition as sr

logger.add_stdout_handler()


def voice_assistant():
    init_music_mixer()
    recognizer = sr.get_recognizer()
    openai_api_key = utils.read_file_as_string(OPENAI_API_KEY_FILE)
    show_all_recognized_input = False

    play_text_to_speech(text="I'm listening...", lang=LANGUAGE)
    try:
        text = sr.get_microphone_audio(recognizer, show_all=show_all_recognized_input)
        log.info(f"User input:\n{text}")
        if text == 'exit' or text == 'end' or text == 'quit':
            play_text_to_speech(text="See you next time!", lang=LANGUAGE)
            time.sleep(2)
            return
        userinput = text['alternative'][-1]['transcript'] if show_all_recognized_input else text
    except sr.UnknownValueError:
        log.info("Sorry, I did not catch your last input")
        userinput = ""
    except sr.RequestError as e:
        userinput = ""
        log.info(f"Error. Could not request results from Google Speech Recognition service: {e}")

    if not userinput:
        return

    chat_gpt_client = ChatGPTClient(openai_api_key)
    messages = []
    messages += [ChatGPTClient.format_message(
        'user',
        userinput
        )]
    chat_gpt_client.get_answer(messages)
    content = chat_gpt_client.response.answer_raw
    log.info(f"Answer:\n{content}")
    play_text_to_speech(text=content, lang=LANGUAGE)

    log.info("Waiting for text to speech feature to end reading the answer")
    while is_music_busy():
        input_val = input("\n\nEnter 'quit' to end this app without waiting for\n"
                          "the text to speech feature to end reading the answer. ")
        if input_val == 'quit':
            break


def main():
    log.info("Start App voice_assistant")
    voice_assistant()
    log.info("End App voice_assistant")


if __name__ == '__main__':
    main()
