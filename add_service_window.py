import tkinter as tk
from cifrario import password_gen

class add_service_form():
    
    def __init__(self):
        self.root = tk.Tk()

    def ok(self):
        serv_name = self.serv_name_entry.get()
        username_mail = self.username_mail_entry.get()
        passw1 = self.password1_entry.get()
        passw2 = self.password2_entry.get()
        if serv_name == "" or username_mail == "":
            return
        elif passw1 == passw2:
            row = serv_name + " " + username_mail + " " + passw1
            with open("p/p.txt", 'a') as p:
                p.writelines("\n" + row)
            self.root.destroy()
    
    def cancel(self):
        self.root.destroy()
        return

    def rng(self):
        pwd_len = self.rand_pass_len_entry.get()
        password = password_gen(int(pwd_len))
        self.password1_entry.delete(0, "end")
        self.password2_entry.delete(0, "end")
        self.password1_entry.insert(1, password)
        self.password2_entry.insert(1, password)

    def start(self):
        main = self.root
        main.config(background = "#494949")

        #setup root
        main.title("Add a new service.")
        main.geometry("700x500")
        main.resizable(False, False)
        
        #buttons
        self.OK_button = tk.Button(main, text = "OK", command = self.ok)
        self.cancel_button = tk.Button(main, text = "Cancel", command = self.cancel)
        self.rng_button = tk.Button(main, text = "⚂⚄⚅", font = ("Helvetica",20), command = self.rng, height = 1)

        # Entry
        self.serv_name_entry = tk.Entry(self.root)
        self.username_mail_entry = tk.Entry(self.root)
        self.password1_entry = tk.Entry(self.root)
        self.password2_entry = tk.Entry(self.root)
        self.rand_pass_len_entry = tk.Entry(self.root)

        #labels
        self.instructions_label = tk.Label( main, text = "Type name, username and password for your service.",
                                            font = "Merriwheather 12 bold", fg = "#efefef", bg = "#494949", anchor = "e", justify = "right")
        self.serv_name_label = tk.Label(main, text = "Service name:", font = "Merriwheather 12", fg = "#efefef",
                                        bg = "#494949", anchor = "e", justify = "right")
        self.username_mail_label = tk.Label(main, text = "Username/e-mail:", font = "Merriwheather 12",
                                            fg = "#efefef", bg = "#494949", anchor = "e", justify = "right")
        self.password1_label = tk.Label(main, text = "Password:", font = "Merriwheather 12",
                                        fg = "#efefef", bg = "#494949", anchor = "e", justify = "right")
        self.password2_label = tk.Label(main, text = "Confirm password:", font = ("Merriwheather", 12),
                                        fg = "#efefef", bg = "#494949", anchor = "e", justify = "right")
        self.rand_pass_len_label = tk.Label(main, text = "Insert the password length:", font = "Merriwheather 12",
                                            fg = "#efefef", bg = "#494949", anchor = "e", justify = "right")
        
        #positioning objects
        #Labels
        self.instructions_label.grid(column = 0, row = 0, columnspan = 4, sticky = "news")
        self.serv_name_label.grid(column = 0, row = 1, sticky = "news")
        self.username_mail_label.grid(column = 0, row = 2, sticky = "news")
        self.password1_label.grid(column = 0, row = 3, sticky = "news")
        self.password2_label.grid(column = 0, row = 4, sticky = "news")
        self.rand_pass_len_label.grid(column = 0, row = 5, sticky = "news")
        
        #entry
        self.serv_name_entry.grid(column = 1, row = 1, columnspan = 2, sticky = "we", padx = 10)
        self.username_mail_entry.grid(column = 1, row = 2, columnspan = 2, sticky = "we", padx = 10)
        self.password1_entry.grid(column = 1, row = 3, columnspan = 2, sticky = "we", padx = 10)
        self.password2_entry.grid(column = 1, row = 4, columnspan = 2, sticky = "we", padx = 10)
        self.rand_pass_len_entry.grid(column = 1, row = 5, sticky = "we", padx = 10)

        #buttons
        self.OK_button.grid(column = 1, row = 7, sticky = "ew", padx = 10)
        self.cancel_button.grid(column = 2, row = 7, sticky = "ew", padx = 10)
        self.rng_button.grid(column = 2, row = 5, columnspan = 1, sticky = "ew", padx = 60)

        for row in range(9):
            main.grid_rowconfigure(row, weight=1)
        for col in range(4):
            main.grid_columnconfigure(col, weight=1)
        

        self.root.mainloop()

#add_service_form().start()