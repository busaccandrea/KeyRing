import cifrario
import getpass 

def login(password):
    key = ""
    with open("p/key.txt", 'rb') as k:
        key = k.readline()
    #password = getpass.getpass("Insert a password: > ")
    password = cifrario.hash(password)
    if password == key:
        cifrario.decrypt(key, "p/", "p.txt.aes")
        print("Logged in successfully.")
    else: 
        print("Wrong password.")


'''def login():
    key = ""
    with open("p/key.txt", 'rb') as k:
        key = k.readline()
    while True:
        password = getpass.getpass("Insert a password: > ")
        password = cifrario.hash(password)
        if password == key:
            cifrario.decrypt(key, "p/", "p.txt.aes")
            print("Logged in successfully.")
            break
        else: 
            print("Wrong password.")'''

def logout():
    key = cifrario.get_key()
    cifrario.encrypt(key, "p/", "p.txt")
    cifrario.encrypt(cifrario.hash("13042008!£$%&/@#"), "p/", "key.txt")