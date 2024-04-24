from tkinter import *

class CalculadoraVista:
    
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Calculadora")
        self.ventana.geometry("320x500")
        self.ventana.resizable(0,0)
        
        # Marcos o Frames
        self.titulo()
        self.operacion_en_tiempo_real()
        self.entrada_de_valores()
        self.titulo_historial()
        self.mostrar_historial_en_tiempo_real()
        
        # Ejecutar la ventana
        self.ventana.mainloop()
        
    def titulo(self):
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
        
    def operacion_en_tiempo_real(self):
        # Mostrar la operación que se esta realizando | Frame
        self.marco_operacion = Frame(self.ventana, height=40, width=320)
        self.marco_operacion.config(
            bd=1,
            relief=SOLID
        )
        self.marco_operacion.pack()
        
    def entrada_de_valores(self):
        # Muestra los valores que se ingresan por teclado | Frame
        self.marco_ingreso_valores = Frame(self.ventana, height=60, width=320)
        self.marco_ingreso_valores.config(
            bd=1,
            relief=SOLID
        )
        self.marco_ingreso_valores.pack()
        
    def titulo_historial(self):
        # Titulo para el historial de operaciones | Frame
        self.marco_titulo_historial = Frame(self.ventana, height=30, width=320)
        self.marco_titulo_historial.config(
            bd=1,
            relief=SOLID
        )
        self.marco_titulo_historial.pack()
        
    def mostrar_historial_en_tiempo_real(self):
        # Muestra el historial de las operaciones realizadas | Frame
        self.historial = Frame(self.ventana, height=340, width=320)
        self.historial.config(
            bd=1,
            relief=SOLID
        )
        self.historial.pack()
        
        



cal = CalculadoraVista()

