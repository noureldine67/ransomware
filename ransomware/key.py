import secrets, os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64


def generate_salt():
    """Génère un sel (salt) cryptographiquement sécurisé."""
    return secrets.token_bytes(16)


def derive_key(salt, password):
    """Dérive une clé à partir d'un mot de passe et du sel, en utilisant Scrypt."""
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())


def load_salt(filename="salt.salt"):
    """Charge le sel à partir d'un fichier existant."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Le fichier de sel '{filename}' est introuvable.")
    return open(filename, "rb").read()


def generate_key(
    password, load_existing_salt=False, save_salt=True, salt_file="salt.salt"
):
    """
    Génère une clé compatible avec Fernet à partir d'un mot de passe et d'un sel.
    - Si `load_existing_salt` est vrai, charge un sel existant.
    - Sinon, génère un nouveau sel si `save_salt` est vrai.
    """
    if load_existing_salt:
        salt = load_salt(salt_file)
    elif save_salt:
        salt = generate_salt()
        with open(salt_file, "wb") as f:
            f.write(salt)
    else:
        raise ValueError("Aucun sel fourni ou généré.")
    derived_key = derive_key(salt, password)
    return base64.urlsafe_b64encode(derived_key)
