import tkinter as tk
from login import login

class login_form():
    
    def __init__(self):
        self.root = tk.Tk()

    def submit(self):
        password = self.put_password.get()
        if password == "":
            print ("no password")
        else:
            login(password)
            self.root.destroy()

    def start(self):

        #setup root
        self.root.title("Login.")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.configure(background = "#1E1503")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(10, weight=1)


        # welcome label
        padding_label = tk.Label(self.root, bg = "#1E1503")
        padding_label.grid(column = 0, row = 0, sticky = "WE", pady = 100)

        welcome_label = tk.Label(self.root, text = "Welcome Pavel!", bg = "#1E1503", font = "Merriweather 25", fg = "#ffffff")
        welcome_label2 = tk.Label(self.root, text = "Insert your password to begin.", bg = "#1E1503", font = "Merriweather 25", fg = "#ffffff")

        welcome_label.grid(column = 0, row = 3, sticky = "WE")
        welcome_label2.grid(column = 0, row = 4, sticky = "WE")


        # entry field
        self.put_password = tk.Entry(self.root, justify = "center", show="•")
        self.put_password.grid(column = 0, row = 5, pady = 10, sticky = "WE", padx = 100)


        #button
        submit_button = tk.Button(self.root, text = "Submit", font = "Merriweather 12", command = self.submit)
        submit_button.grid(column = 0, row = 7, pady = 10)


        self.root.mainloop()