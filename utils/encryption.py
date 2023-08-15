from cryptography.fernet import Fernet
import pickle

from utils.shared import *

def encrypt_data(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(pickle.dumps(data))
    return encrypted_data

def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = pickle.loads(f.decrypt(encrypted_data))
    return decrypted_data
