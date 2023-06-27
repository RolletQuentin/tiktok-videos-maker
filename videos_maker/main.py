import os
import argparse
from create_audio import create_audio
from create_folder import create_story_folder
from create_video import create_synced_videos
from create_text import create_text_file

SUPPORTED_LANGUAGES = ["en", "fr", "es"]


def create_tiktok_video(title, text):

    folder_path = create_story_folder()

    create_text_file(title, text, folder_path, SUPPORTED_LANGUAGES)

    create_audio(title, folder_path, SUPPORTED_LANGUAGES)

    create_synced_videos(folder_path, SUPPORTED_LANGUAGES, title)


if __name__ == "__main__":

    # Parser les arguments en ligne de commande
    parser = argparse.ArgumentParser(
        description='Créer un dossier d\'histoire avec traduction et synthèse vocale.')
    parser.add_argument('title', type=str, help='Title of the story')
    parser.add_argument('text', type=str, help='Texte de l\'histoire')
    args = parser.parse_args()

    # Utiliser l'argument fourni pour créer le dossier d'histoire
    create_tiktok_video(args.title, args.text)
