import os
from pathlib import Path
import cifrario
import login
import begin_user_session as bus
import getpass
import login_window as lw
import user_session_window as us

if not os.path.exists("p/p.txt.aes"):
    Path("p/p.txt").touch()
    Path("p/key.txt").touch()
    while True:
        psw = getpass.getpass("Choose a login password. > ")
        psw2 = getpass.getpass("Confirm password. > ")
        if psw == psw2:
            break
    cifrario.make_key_file(psw)
    cifrario.encrypt(cifrario.hash(psw), "p/", "p.txt")

if os.path.exists("p/p.txt.aes"):
    cifrario.decrypt(cifrario.hash("13042008!£$%&/@#"), "p/", "key.txt.aes")
    w = lw.login_form()
    w.start()
    us.user_session_window().start()
    login.logout()
     