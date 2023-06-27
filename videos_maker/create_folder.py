import os
import argparse
from gtts import gTTS


def create_story_folder():
    # Vérifier si le dossier "stories" existe, sinon le créer
    if not os.path.exists('./stories'):
        os.makedirs('./stories')

    # Récupérer le numéro de l'histoire en comptant les dossiers existants dans "./stories"
    story_number = len([name for name in os.listdir(
        './stories') if os.path.isdir(os.path.join('./stories', name))]) + 1

    # Créer le dossier pour l'histoire
    folder_name = f'story_{story_number:02d}'
    folder_path = os.path.join('./stories', folder_name)
    os.makedirs(folder_path)

    print(f"Folder '{folder_name}' created with success.")

    return folder_path
