import cifrario
def login():
    key = ""
    with open("p/key.txt", 'rb') as k:
        key = k.readline()

    while True:   
        password = input("Insert a password: > ")
        password = cifrario.hash(password)
        if password == key:
            cifrario.decrypt(key, "p/", "p.txt.aes")
            print("Logged in successfully.")
            break
        else: 
            print("Wrong password.")

def logout():
    key = cifrario.get_key()
    cifrario.encrypt(key, "p/", "p.txt")
    cifrario.encrypt(cifrario.hash("13042008!£$%&/@#"), "p/", "key.txt")