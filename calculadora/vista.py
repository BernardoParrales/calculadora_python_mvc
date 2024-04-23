from tkinter import *

class CalculadoraVista:
    
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Calculadora")
        self.ventana.geometry("320x500")
        self.ventana.resizable(0,0)
        
        # Presenta el titulo de la APP | Frame
        self.marco_titulo_principal = Frame(self.ventana, height=30, width=320)
        self.marco_titulo_principal.config(
            bd=1,
            relief=SOLID
        )
        self.marco_titulo_principal.pack()
        self.marco_titulo_principal.pack_propagate(False)
        
        # Titulo principal
        text_titulo = Label(self.marco_titulo_principal, text="CALCULADORA BÁSICA")
        text_titulo.pack(anchor=W)
        
        # Mostrar la operación que se esta realizando | Frame
        self.marco_operacion = Frame(self.ventana, height=40, width=320)
        self.marco_operacion.config(
            bd=1,
            relief=SOLID
        )
        self.marco_operacion.pack()
        
        # Muestra los valores que se ingresan por teclado | Frame
        self.marco_ingreso_valores = Frame(self.ventana, height=60, width=320)
        self.marco_ingreso_valores.config(
            bd=1,
            relief=SOLID
        )
        self.marco_ingreso_valores.pack()
        
        # Titulo para el historial de operaciones | Frame
        self.marco_titulo_historial = Frame(self.ventana, height=30, width=320)
        self.marco_titulo_historial.config(
            bd=1,
            relief=SOLID
        )
        self.marco_titulo_historial.pack()
        
        # Muestra el historial de las operaciones realizadas | Frame
        self.historial = Frame(self.ventana, height=340, width=320)
        self.historial.config(
            bd=1,
            relief=SOLID
        )
        self.historial.pack()
        
        self.ventana.mainloop()

cal = CalculadoraVista()

