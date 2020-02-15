import tkinter as tk
import begin_user_session as bus
import add_service_window as asw

class user_session_window():

    def __init__(self):
        self.root = tk.Tk()

    def show(self):
        service_name = self.lb.selection_get()
        if service_name == "":
            print("EE")
            return
        self.text_area.configure(state = "normal")
        self.text_area.delete(1.0, "end")
        for s in self.service_list:
            if s[0] == service_name:
                for i in s:
                    self.text_area.insert("end", i + "\n")
        self.text_area.configure(state = "disabled")

    def refresh(self):
        self.lb.delete(0, "end")
        for s in bus.list_from_p():
            self.lb.insert("end", s[0])

    def add_new_service(self):
        asw.add_service_form().start()

    def start(self):
        
        main = self.root
        main.config(background = "#494949")

        #setup root
        main.title("Keyring session opened.")
        main.geometry("1000x700")
        main.resizable(False, False)
        
        #buttons
        self.show_button = tk.Button(main, text = "show", command = self.show)
        self.new_service_button = tk.Button(main, text = "New service", command = self.add_new_service)
        self.refresh_button = tk.Button(main, text = "↻", command = self.refresh)

        #text area
        self.text_area = tk.Text(main, bg = "#494949", fg = "#efefef", width = 20, height=8, font=("Merriwheather", 20))
        self.text_area.configure(state = "disabled")

        #labels
        self.l1 = tk.Label(main, text = "Your services.", font = "Merriwheather 15", fg = "#efefef", bg = "#494949", anchor = "w")
        self.refresh_label = tk.Label(main, text = "Refresh list", bg = "#494949", fg = "#efefef", padx = 10, anchor = "sw")

        #listbox
        self.service_list = bus.list_from_p()
        self.lb = tk.Listbox(main, bg = "#494949", fg = "#efefef", font = "Merriwheather 15")
        for s in self.service_list:
            self.lb.insert("end", s[0])

        #positioning objects
        self.l1.grid(column = 0, row = 0, columnspan = 3, sticky = "news")
        self.lb.grid(column = 0, row = 1, rowspan = 5, sticky = "news")
        self.text_area.grid(column = 2, row = 1, rowspan = 5)
        self.show_button.grid(column = 1, row = 3, sticky = "ew", padx = 10)
        self.refresh_label.grid(column = 1, row = 1, sticky = "w")
        self.refresh_button.grid(column = 1, row = 2, sticky = "wn")
        self.new_service_button.grid(column = 0, row = 7, sticky = "ew", padx = 10)

        for row in range(9):
            main.grid_rowconfigure(row, weight=1)
        for col in range(3):
            main.grid_columnconfigure(col, weight=1)
        

        self.root.mainloop()

#user_session_window().start()