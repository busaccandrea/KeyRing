import tkinter as tk
import begin_user_session as bus

class user_session_window():

    def __init__(self):
        self.root = tk.Tk()

    def show(self):
        service_name = self.lb.selection_get()
        if service_name == "":
            return
        self.text_area.configure(state = "normal")
        self.text_area.delete(1.0, "end")
        self.text_area.insert("end", service_name)
        self.text_area.configure(state = "disabled")

    def add_new_service(self):
        # nuova finestra con 3 text box
        return

    def start(self):
        service_list = bus.list_from_p()
        main = self.root
        main.config(background = "#494949")

        #setup root
        main.title("Keyring session opened.")
        main.geometry("1000x700")
        main.resizable(False, False)
        
        #buttons
        self.show_button = tk.Button(main, text = "show", command = self.show)
        self.new_service_button = tk.Button(main, text = "New service", command = self.add_new_service)

        #text area
        self.text_area = tk.Text(main, bg = "#494949", fg = "#efefef")
        self.text_area.configure(state = "disabled")

        #labels
        self.l1 = tk.Label(main, text = "Your services.", font = "Merriwheather 15", fg = "#efefef", bg = "#494949")
        self.l3 = tk.Label(main, bg = "#494949")

        #listbox
        self.lb = tk.Listbox(main, bg = "#494949", fg = "#efefef", font = "Merriwheather 15")
        '''inserire for che riempie la lista'''
        for s in service_list:
            self.lb.insert("end", s[0])

        #positioning objects
        self.l1.grid(column = 0, row = 0, columnspan = 3, sticky = "news")
        self.lb.grid(column = 0, row = 1, rowspan = 5, sticky = "news")
        self.text_area.grid(column = 2, row = 1, rowspan = 5, sticky = "news")
        self.show_button.grid(column = 1, row = 1, sticky = "ew", padx = 10)
        self.new_service_button.grid(column = 0, row = 7, sticky = "ew", padx = 10)

        for row in range(9):
            main.grid_rowconfigure(row, weight=1)
        for col in range(3):
            main.grid_columnconfigure(col, weight=1)
        

        self.root.mainloop()

#user_session_window().start()