import tkinter as tk
from login import login

class login_form():
    
    def __init__(self):
        self.root = tk.Tk()

    def submit(self, event = None):
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
        self.root.configure(background = "#212121")

        #background image
        background_image = tk.PhotoImage("bg/logokeyring.png")


        #label
        self.welcome_label = tk.Label(self.root, text = "Welcome Pavel!\nInsert your password to begin.\n", font = "Merriweather 25", bg = "#212121", fg = "#F25454")
        background_label = tk.Label(self.root, image = background_image)
        background_label.place(x = 0, y = 0)
        background_label.image = background_image

        # entry field
        self.put_password = tk.Entry(self.root, justify = "center", show = "•")
        self.put_password.bind('<Return>', self.submit)

        #button
        self.submit_button = tk.Button(self.root, text = "Submit", font = "Merriweather 12", command = self.submit)
        
        #place things
        self.welcome_label.grid(column = 0, row = 3, rowspan = 2, sticky = "WE")
        self.put_password.grid(column = 0, row = 4, sticky = "WE")
        self.submit_button.grid(column = 0, row = 5)

        for row in range(6):
            self.root.grid_rowconfigure(row, weight=1)
        for col in range(1):
            self.root.grid_columnconfigure(col, weight=1)

        self.root.mainloop()