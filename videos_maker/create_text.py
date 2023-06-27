import os
from deep_translator import GoogleTranslator


def create_text_file(title, text, folder_path, supported_languages):

    for language in supported_languages:

        translated_text = GoogleTranslator(
            source='auto', target=language).translate(text)

        with open(os.path.join(folder_path, f"{language}_{title}.txt"), 'w') as file:
            file.write(translated_text)
