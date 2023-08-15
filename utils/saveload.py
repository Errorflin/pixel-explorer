from utils.encryption import *
from utils.shared import *

game_settings = {
    "keys": {
        "forward": "up"
    }
}

def load_data(filename):
    try:
        with open(filename, 'rb') as file:
            decrypted_data = decrypt_data(file.read(), encryption_key)
            return decrypted_data
    except FileNotFoundError:
        save_data(game_settings, filename)

def save_data(data, filename):
    with open(filename, 'wb') as file:
        encrypted_data = encrypt_data(data, encryption_key)
        file.write(encrypted_data)

settings_data = load_data("data/save/settings.dat")
