# pyencrypt
Python script to generate keys and encrypt/decrypt messages with the Fernet library.

usage:
	Generate a private key file:
		python3 pyencrypt.py -g -k KEYFILE
	Encrypt a message:
		python3 encrypt.py -k KEYFILE -e MESSAGE_TO_ENCRYPT
	Decrypt a message:
		python3 encrypt.py -k KEYFILE -d MESSAGE_TO_DECRYPT

