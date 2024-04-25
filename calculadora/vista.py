from tkinter import *
from tkinter import messagebox
from calculadora.controlador import CalculadoraControl

class CalculadoraVista:
    
    def __init__(self):
        # Inicializar la ventana raiz (root)
        self.ventana = Tk()
        self.controlador = CalculadoraControl()
        self.ventana.title("Calculadora")
        self.ventana.geometry("320x500")
        self.ventana.resizable(0,0)
        
        # Agregar icono
        self.ventana.iconbitmap('./calculadora/icon.ico')
        
        # Variables
        self.valor = StringVar(value="0")
        self.valor_float = "0"
        
        self.valor_tiempo_real = StringVar()
        self.valor_tiempo_real_string = ""
        
        self.historial = StringVar()
        self.historial_string = ""
        
        # Manejo de estados para las operaciones 
        # 0 = Activo / 1 = Inactivo
        self.suma_estado = 0
        self.resta_estado = 0
        self.multiplicar_estado = 0
        self.dividir_estado = 0
        self.punto_estado = 0
        

        # Marcos o Frames
        self.titulo()
        self.pantalla_operacion_en_tiempo_real()
        self.pantalla()
        self.teclado()
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
        text_titulo.config(
            font=("Helvica", 14)
        )
        text_titulo.pack(anchor=W)
        
    def pantalla_operacion_en_tiempo_real(self):
        # Mostrar la operación que se esta realizando | Frame
        self.marco_operacion = Frame(self.ventana, height=40, width=320)
        self.marco_operacion.config(
            bd=1,
            relief=SOLID
        )
        self.marco_operacion.pack()
        self.marco_operacion.pack_propagate(False)
        
        self.pantalla_operacion = Label(self.marco_operacion, textvariable=self.valor_tiempo_real)
        self.pantalla_operacion.pack()
        
    def pantalla(self):
        # Muestra los valores que se ingresan por teclado | Frame
        self.marco_ingreso_valores = Frame(self.ventana, height=60, width=320)
        self.marco_ingreso_valores.config(
            bd=1,
            relief=SOLID
        )
        self.marco_ingreso_valores.pack()
        self.marco_ingreso_valores.pack_propagate(False)
        
        # Pantalla
        self.pantalla_ingreso_valores = Label(self.marco_ingreso_valores, textvariable=self.valor)
        self.pantalla_ingreso_valores.config(
            width=320,
            font=("Arial", 35),
            justify="right",
            
        )
        
        self.pantalla_ingreso_valores.pack()
        
    def teclado(self):
        # TECLAS NUMERICAS
        self.ventana.bind("0", lambda e: self.add(0))
        self.ventana.bind("1", lambda e: self.add(1))
        self.ventana.bind("2", lambda e: self.add(2))
        self.ventana.bind("3", lambda e: self.add(3))
        self.ventana.bind("4", lambda e: self.add(4))
        self.ventana.bind("5", lambda e: self.add(5))
        self.ventana.bind("6", lambda e: self.add(6))
        self.ventana.bind("7", lambda e: self.add(7))
        self.ventana.bind("8", lambda e: self.add(8))
        self.ventana.bind("9", lambda e: self.add(9))
        self.ventana.bind(".", lambda e: self.add_punto())
        
        # TECLAS DE OPERACIONES
        self.ventana.bind("<BackSpace>", lambda e: self.delete())
        self.ventana.bind("+", lambda e: self.sumar())
        self.ventana.bind("-", lambda e: self.restar())
        self.ventana.bind("*", lambda e: self.multiplicar())
        self.ventana.bind("/", lambda e: self.dividir())
        self.ventana.bind("<Return>", lambda e: self.realizar_operacion())
        
    # Agregar valor mediante la toma de eventos de teclado    
    def sumar(self):
        if self.suma_estado == 0:
            self.suma_estado = 1
            print("+")
            self.controlador.agregar_primer_valor(self.valor_float)
            
            self.valor_tiempo_real_string = self.valor_float + " + "
            self.valor_tiempo_real.set(self.valor_tiempo_real_string)
            
            self.valor_float = ""
            self.actualizar_pantalla()
            
    def restar(self):
        if self.resta_estado == 0:
            self.resta_estado = 1
            print("-")
            self.controlador.agregar_primer_valor(self.valor_float)
            
            self.valor_tiempo_real_string = self.valor_float + " - "
            self.valor_tiempo_real.set(self.valor_tiempo_real_string)
            
            self.valor_float = ""
            self.actualizar_pantalla()
            
    def multiplicar(self):
        if self.multiplicar_estado == 0:
            self.multiplicar_estado = 1
            print("*")
            self.controlador.agregar_primer_valor(self.valor_float)
            
            self.valor_tiempo_real_string = self.valor_float + " x "
            self.valor_tiempo_real.set(self.valor_tiempo_real_string)
            
            self.valor_float = ""
            self.actualizar_pantalla()
            
    def dividir(self):
        if self.dividir_estado == 0:
            self.dividir_estado = 1
            print("/")
            self.controlador.agregar_primer_valor(self.valor_float)
            
            self.valor_tiempo_real_string = self.valor_float + " / "
            self.valor_tiempo_real.set(self.valor_tiempo_real_string)
            
            self.valor_float = ""
            self.actualizar_pantalla()
        
    # Realizar las operaciones        
    def realizar_operacion(self):
        if self.suma_estado == 1:
            self.controlador.agregar_segundo_valor(self.valor_float)
            self.actualizar_pantalla_tiempo_real()
            result = self.controlador.sumar_valores() # op
            print(result)
            self.suma_estado = 0
            self.valor_float = result
            self.actualizar_pantalla()
            self.actualizar_pantalla_historial(result)
            
        elif self.resta_estado == 1:
            self.controlador.agregar_segundo_valor(self.valor_float)
            self.actualizar_pantalla_tiempo_real()
            result = self.controlador.restar_valores() # op
            print(result)
            self.resta_estado = 0
            self.valor_float = result
            self.actualizar_pantalla()
            self.actualizar_pantalla_historial(result)
            
        elif self.multiplicar_estado == 1:
            self.controlador.agregar_segundo_valor(self.valor_float)
            self.actualizar_pantalla_tiempo_real() 
            result = self.controlador.multiplicar_valores() # op
            print(result)
            self.multiplicar_estado = 0
            self.valor_float = result
            self.actualizar_pantalla()
            self.actualizar_pantalla_historial(result)
            
        elif self.dividir_estado == 1:
            self.controlador.agregar_segundo_valor(self.valor_float)
            self.actualizar_pantalla_tiempo_real()
            result = self.controlador.dividir_valores() # op
            print(result[0])
            self.dividir_estado = 0
            self.valor_float = result[0]
            self.actualizar_pantalla()
            
            if result[1][0] == False:
                messagebox.showerror("Error", "No se puede dividir entre 0.")
            else:
                self.actualizar_pantalla_historial(result)
    
    def actualizar_pantalla_tiempo_real(self):
        self.valor_tiempo_real_string = self.valor_tiempo_real_string + self.valor_float + " = "
        self.valor_tiempo_real.set(self.valor_tiempo_real_string)
             
    def actualizar_pantalla_historial(self, result):
        self.historial_string = self.historial_string + self.valor_tiempo_real_string + result + "\n"
        self.historial.set(self.historial_string)
    
    def delete(self):
        self.valor_float = self.valor_float[:-1]
        self.actualizar_pantalla()
        print(self.valor_float)
        
        try:
            for i in self.valor_float:
                if i == ".":
                    self.punto_estado = 1
            if self.valor_float[-1] == ".":
                self.punto_estado = 0
        except Exception:
            self.punto_estado = 0
        
    def add(self, valor):
        print(valor)
        if valor != 0:
            self.valor_float = ""
            self.valor_float = self.valor_float + str(valor)
            self.actualizar_pantalla()
      
    def actualizar_pantalla(self):
        self.valor.set(self.valor_float)  
    
    # Trabajar en la funcion para agregar el punto    
    def add_punto(self):
        if self.punto_estado == 0:
            self.punto_estado = 1
            print(".")
            self.valor_float = self.valor_float + "."
            self.valor.set(self.valor_float)
            print(self.valor_float)
        
        
    def titulo_historial(self):
        # Titulo para el historial de operaciones | Frame
        self.marco_titulo_historial = Frame(self.ventana, height=30, width=320)
        self.marco_titulo_historial.config(
            bd=1,
            relief=SOLID
        )
        self.marco_titulo_historial.pack()
        self.marco_titulo_historial.pack_propagate(False)
        
        # Titulo historial
        text_titulo = Label(self.marco_titulo_historial, text="Historial")
        text_titulo.config(
            font=("Helvica", 10)
        )
        text_titulo.pack(anchor=W)
        
    def mostrar_historial_en_tiempo_real(self):
        # Muestra el historial de las operaciones realizadas | Frame
        self.historial_caja = Frame(self.ventana, height=340, width=320)
        self.historial_caja.config(
            bd=1,
            relief=SOLID
        )
        self.historial_caja.pack()
        self.historial_caja.pack_propagate(False)
        
        self.pantalla_historial = Label(self.historial_caja, textvariable=self.historial)
        self.pantalla_historial.config(
            font=("Helvica", 12)
        )
        self.pantalla_historial.pack()
        
        
        

