#!/usr/bin/python

from cryptography.fernet import Fernet
import getopt, sys, os, json, subprocess
usage = "usage:\n\tGenerate a private key file:\n\t\tpython3 pyencrypt.py -g -k KEYFILE\n\tEncrypt a message:\n\t\tpython3 encrypt.py -k KEYFILE -e MESSAGE_TO_ENCRYPT\n\tDecrypt a message:\n\t\tpython3 encrypt.py -k KEYFILE -d MESSAGE_TO_DECRYPT\n\n"

# get opts
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "gk:e:d:", [ "generate=","key=","encrypt=","decrypt=" ])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    optsjsonstr = "{ "
    i = 0
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(usage)
            sys.exit()
        elif opt in ("-g", "--generate"):
            optsjsonstr += '"Generate": ' + '"True"'
        elif opt in ("-k", "--key"):
            optsjsonstr += '"Keyfile": ' + '"' + arg + '"'
        elif opt in ("-e", "--encrypt"):
            optsjsonstr += '"Encrypt": ' + '"' + arg + '"'
        elif opt in ("-d", "--decrypt"):
            optsjsonstr += '"Decrypt": ' + '"' + arg + '"'
        if (i != len(opts) - 1):
            optsjsonstr += ','
        i += 1
    optsjsonstr += " }"
    return json.loads(optsjsonstr)

# generates a key and saves it to a file
def generate_key(path):
    key = Fernet.generate_key()
    with open(path, "wb") as keyfile:
        keyfile.write(key)
    pcmd = "chmod 440 " + path
    subprocess.run([pcmd],shell=True)
    print("Created key file '" + path + "'")

# loads the keyfile
def load_key(path):
    return open(path, "rb").read()

# encryts a message
def encrypt_message(path, message):
    key = load_key(path)
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message.decode()

# decrypts a message
def decrypt_message(path, encrypted_message):
    key = load_key(path)
    f = Fernet(key)
    mbytes = bytes(encrypted_message, 'utf-8')
    decrypted_message = f.decrypt(mbytes)
    return decrypted_message.decode()

if __name__ == "__main__":
    opts = main(sys.argv[1:])

# check some things and give user feedback about incorrect conditions.

if opts == {}:
    quit(2)

if ("Keyfile" not in opts):
    print("\nPlease specify a key file using the '-k Path_to_Keyfile' or '--key Path_to_KeyFile' option.\n\n")
    quit(2)

if ("Generate" in opts and "Encrypt" in opts):
    print("\nOptions -g (generate) and -e Encrypt may not be used together.\n\n" + usage)
    quit(2)

if ("Generate" in opts and "Decrypt" in opts):
    print("\nOptions -g (generate) and -d Decrypt may not be used together.\n\n" + usage)
    quit(2)

if ("Generate" in opts and not "Keyfile" in opts):
    print("\nSpecify a key file to write when using the -g option.\n\n" + usage)
    quit(2)

if ("Encrypt" in opts and not "Keyfile" in opts):
    print("\nSpecify a key file to encrypt the message with.\n\n" + usage)
    quit(2)

if ("Decrypt" in opts and not "Keyfile" in opts):
    print("\nSpecify a key file to decrypt the message with.\n\n" + usage)
    quit(2)

if ("Decrypt" in opts and "Encrypt" in opts):
    print("\nOptions -e Encrypt and -d Decrypt may not be used together.\n\n" + usage)
    quit(2)

# perform the operations

if ("Generate" in opts and "Keyfile" in opts):
    if not os.path.exists(os.path.dirname(opts['Keyfile'])):
        print("\nInvalid path to write key.\n")
        quit()
    generate_key(opts['Keyfile'])
    quit()

if not os.path.exists(opts['Keyfile']):
    print("\nKey file does not exist.\n\n")
    quit()

if ("Encrypt" in opts and "Keyfile" in opts):
    print("Result: " + encrypt_message(opts['Keyfile'], opts['Encrypt']))
    quit()

if ("Decrypt" in opts and "Keyfile" in opts):
    print("Result: " + decrypt_message(opts['Keyfile'], opts['Decrypt']))
    quit()

