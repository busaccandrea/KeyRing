import random, Crypto
from Crypto.Cipher import AES
import os
from Crypto.Hash import SHA256
import login
import cifrario


def begin_user_session():
    print("Hello!")
    p_list = list_from_p()
    while True:
            cmd = input(r"""

What do you want to do?
1. add a service
2. show service list.
3. show a service.
exit. Exit the program.

""")
            if cmd == "1":
                # add a service
                add_service()
            elif cmd == "2":
                # show all services
                show_service_list(p_list)
            elif cmd == "3":
                # show a specific service
                show_service()
            elif cmd == "exit":
                #exit program
                break
                
def list_from_p():
    p_list = []
    with open("p/p.txt", 'r') as p:
        p_lines = p.readlines()
        for l in p_lines:
            p_list.append(l.split(" "))
    return p_list

def show_service_list(p_list):
    print("#########################################################################\nYour services:")
    for p in p_list:
        print(p[0])

def show_service():
    service_name = input("\nWitch service do you want to see? > ")
    with open("p/p.txt", 'r') as p:
        for line in p.readlines():
            service, password = line.split(" ")
            if service == service_name:
                print(password)

def add_service():
    
    service_name = input("\nService name (e.g. facebook, fineco, PayPal, etc.) > ")
    account_name = input("\nEmail or nickname > ")
    while True:
        cmd = input("\nIf you want i can generate a fandom password for you. Do you want a random password? [y/n]")
        if cmd == "y" or cmd == "Y" or cmd == "yes":
            p_lenght = input("\nHow much characters do you want? (at least 6)")
            password = cifrario.password_gen(int(p_lenght))
            
            break
        else:
            password = input("\nInsert a password. > ")
            password2 = input("\nConfirm the password. > ")
            if password == password2:
                break
    with open("p/p.txt", 'a') as p:    
        p.write(service_name + " " + account_name  + " " +  password + "\n")
        
        
    print("Service added successfully!")

