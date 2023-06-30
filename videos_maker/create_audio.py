from gtts import gTTS
from deep_translator import GoogleTranslator
import os


def create_audio(title, folder_path, supported_languages):

    for language in supported_languages:

        with open(os.path.join(folder_path, f"{language}_{title}.txt"), 'r') as file:
            text = file.read()

        text_speech = gTTS(text, lang=language)
        text_speech.save(f"{folder_path}/{language}_text.wav")

        translated_title = GoogleTranslator(
            source='auto', target=language).translate(text)
        title_speech = gTTS(translated_title, lang=language)
        title_speech.save(f"{folder_path}/{language}_title.wav")
