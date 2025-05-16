import os
import getpass
from ransomware.encrypt import encrypt_file, encrypt_folder
from ransomware.decrypt import decrypt_file, decrypt_folder
from ransomware.key import generate_key

if __name__ == "__main__":
    import argparse

    # Configuration des arguments de la ligne de commande
    parser = argparse.ArgumentParser(
        description="Chiffrement/Déchiffrement de fichiers via mot de passe."
    )
    parser.add_argument("path", help="Chemin vers un fichier ou dossier à traiter.")
    parser.add_argument(
        "-e", "--encrypt", action="store_true", help="Chiffrer le fichier ou dossier."
    )
    parser.add_argument(
        "-d", "--decrypt", action="store_true", help="Déchiffrer le fichier ou dossier."
    )
    args = parser.parse_args()

    # Vérification des options
    if not args.encrypt and not args.decrypt:
        raise ValueError("Veuillez spécifier --encrypt ou --decrypt.")

    if args.encrypt and args.decrypt:
        raise ValueError("Vous ne pouvez pas chiffrer ET déchiffrer en même temps.")

    # Saisie sécurisée du mot de passe
    password = getpass.getpass("Entrez le mot de passe : ")

    # Génération ou chargement de la clé
    try:
        # Si le fichier de sel existe, on le charge automatiquement
        if os.path.exists("salt.salt"):
            print("[i] Fichier de sel trouvé : salt.salt")
            key = generate_key(password, load_existing_salt=True, save_salt=False)
        else:
            # Sinon on en génère un nouveau
            key = generate_key(password, load_existing_salt=False, save_salt=True)
    except Exception as e:
        print(f"[!] Erreur : {e}")
        exit(1)

    # Traitement : fichier ou dossier
    if os.path.isfile(args.path):
        if args.encrypt:
            encrypt_file(args.path, key)
        else:
            decrypt_file(args.path, key)
    elif os.path.isdir(args.path):
        if args.encrypt:
            encrypt_folder(args.path, key)
        else:
            decrypt_folder(args.path, key)
    else:
        print("[!] Le chemin fourni n'existe pas ou n'est pas valide.")
