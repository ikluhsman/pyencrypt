# pyencrypt
Python encryption using the Fernet library. Script generates a key and encrypts / decrypts messages.

usage:
	Generate a private key file:
		python3 pyencrypt.py -g -k KEYFILE
	Encrypt a message:
		python3 encrypt.py -k KEYFILE -e MESSAGE_TO_ENCRYPT
	Decrypt a message:
		python3 encrypt.py -k KEYFILE -d MESSAGE_TO_DECRYPT

