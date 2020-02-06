import os
from pathlib import Path
import cifrario
import login
import begin_user_session as bus


if not os.path.exists("p/p.txt.aes"):
    Path("p/p.txt").touch()
    '''username = input("Inserisci il tuo username. > ")
    with open("p/p.txt", 'w') as p_file:
        p_file.write(username)'''
    Path("p/key.txt").touch()
    psw = input("Scegli una password. > ")
    cifrario.make_key_file(psw)
    cifrario.encrypt(cifrario.hash(psw), "p/", "p.txt")

if os.path.exists("p/p.txt.aes"):
    cifrario.decrypt(cifrario.hash("13042008!£$%&/@#"), "p/", "key.txt.aes")
    login.login()
    bus.begin_user_session()
    login.logout()
    