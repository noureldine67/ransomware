import pathlib
from cryptography.fernet import Fernet, InvalidToken


def decrypt_file(filename, key):
    """Déchiffre un fichier avec la clé donnée."""
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except InvalidToken:
        print(
            f"[!] Jeton invalide — le mot de passe est peut-être incorrect pour : {filename}"
        )
        return
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print(f"[+] Fichier déchiffré : {filename}")


def decrypt_folder(foldername, key):
    """Déchiffre récursivement tous les fichiers d’un dossier."""
    for child in pathlib.Path(foldername).rglob("*"):
        if child.is_file():
            decrypt_file(str(child), key)
