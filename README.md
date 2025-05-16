# Projet Ransomware Pédagogique

Ce projet est une **démonstration pédagogique** de chiffrement et déchiffrement de fichiers et dossiers en Python.  
Il utilise la bibliothèque `cryptography` avec l’algorithme Fernet, et dérive la clé à partir d’un mot de passe via la fonction `Scrypt`.

---

## Fonctionnalités

- Génération d’une clé sécurisée à partir d’un mot de passe avec `Scrypt`.
- Chiffrement et déchiffrement de fichiers individuels.
- Chiffrement et déchiffrement récursif de dossiers entiers.
- Sauvegarde et chargement automatique d’un sel (`salt.salt`) pour la dérivation de la clé.
- Interface en ligne de commande simple pour utiliser le script principal.

---

## Utilisation

### Chiffrement

```bash
python ransomware.py --encrypt /chemin/vers/fichier_ou_dossier 
```

### Déchiffrement

```bash
python ransomware.py --decrypt /chemin/vers/fichier_ou_dossier
```

---

## Notes de sécurité

* Ce projet est **pédagogique** et ne doit pas être utilisé à des fins malveillantes.

---