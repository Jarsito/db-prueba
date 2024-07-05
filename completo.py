#Se importan las librerías 
import re 
import tkinter as tk
import mysql.connector
from tkinter import ttk

#Esta clase pertenece al MODELO
class Persona:

    #Constructor de la clase
    def __init__(self, email):
        self.email = email

    #Declaracion de atributo de la clase
    @property
    def email(self):
        return self.__email

    #Método SET de Email"
    @email.setter
    def email(self, value):
        #Uso de expresion regular
        #Patron con el que se compara el formato que debe tener un Email cuando se ingrese
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    #Guardar emails en archivo emails.txt"
    def save(self):
        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')

# Esta clase pertenece a la VISTA
class View(ttk.Frame):

    #Constructor que inicializa el contenedor o ventana
    def __init__(self, parent):
        super().__init__(parent)

    # Se inicializan los controles que van a ir dentro de la ventana
        self.label = ttk.Label(self, text='Email:')
        self.label.grid(row=1, column=0)
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self,textvariable=self.email_var, width=30)
        self.email_entry.grid(row=1, column=1,sticky=tk.NSEW)
        self.save_button = ttk.Button(self, text='Save',command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)
        self.message_label = ttk.Label(self, text='',foreground='red')
        self.message_label.grid(row=2, column=1,sticky=tk.W)

    # Método Set de la variable Controller
    def set_controller(self, controller):
        self.controller = controller

    # Metodo 
    def save_button_clicked(self):
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)
        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        self.message_label['text'] = ''

    # Con esta clase controlamos el progrma
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, email):

        try:
            # save the model
            self.model.email = email
            self.model.save()
            # show a success message
            self.view.show_success(f'The email {email} saved!')
        except ValueError as error:
            # show an error message
            self.view.show_error(error)

        # Esta clase es la solicitud
class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Tkinter MVC Demo')
        # create a model
        model = Persona('hello@pythontutorial.net')
        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)
        # create a controller
        controller = Controller(model, view)
        # set the controller to view
        view.set_controller(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()

    # Clase Sigelton
class Singleton:
    __instance = None
    @staticmethod
    def getInstance():
        # acceso a metodo estatico  
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    def __init__(self):
        #  constructor privado, virtual. """
        if Singleton.__instance != None:
            raise Exception("soy singleton")
        else:
            Singleton.__instance = self
s = Singleton()
print (s)
s = Singleton.getInstance()
print (s)
s = Singleton.getInstance()
print (s)
