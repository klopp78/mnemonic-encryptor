README.md Contentmarkdown

# Mnemonic Encryptor

A Python script to securely encrypt and decrypt 12-word mnemonic phrases (e.g., for cryptocurrency wallets) using Base64 encoding, a user-specified special character, and AES-256-CBC encryption. The script provides a command-line menu interface for ease of use.

## Features
- Encrypts a 12-word mnemonic phrase into a Base64-encoded ciphertext with a special character.
- Uses AES-256-CBC for secure encryption with a randomly generated key and initialization vector (IV).
- Decrypts the ciphertext back to the original mnemonic phrase using the key and special character.
- Interactive menu interface for encryption and decryption.

## Prerequisites
- Ubuntu 20.04 or later
- Python 3.6 or higher
- Git (for cloning the repository)
- `pycryptodome` Python library

## Installation on Ubuntu

1. **Update Package List**:
   Ensure your system is up-to-date:
   ```bash
   sudo apt update

Install Python and Pip:
Install Python 3 and pip if not already installed:bash

sudo apt install python3 python3-pip

Install Git (optional, for cloning the repository):bash

sudo apt install git

Clone the Repository (if using Git):bash

git clone https://github.com/your-username/mnemonic-encryptor.git
cd mnemonic-encryptor

Replace your-username with your GitHub username.Alternatively, download the mnemonic_encryptor.py file directly from the GitHub repository.
Set Up a Virtual Environment (recommended):
Create and activate a virtual environment to manage dependencies:bash

python3 -m venv venv
source venv/bin/activate

Install Dependencies:
Install the required pycryptodome library:bash

pip install pycryptodome

Make the Script Executable:
Ensure the script has executable permissions:bash

chmod +x mnemonic_encryptor.py

