import service as s
import random, Crypto
from Crypto.Cipher import AES
import os
from Crypto.Hash import SHA256
import login
import cifrario


def begin_user_session():
    print("Hello!")
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
                # show a specific service
                show_service_list()
            elif cmd == "3":
                
                show_service()
            elif cmd == "exit":
                break
                
            
def show_service_list():
    with open("p/p.txt", 'r') as p:
        services = p.readlines()
        for s in services:
            serv = s.split(" ")
            print(serv[0])

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
            # generare una password random di x caratteri.
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

