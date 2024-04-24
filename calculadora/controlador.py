from calculadora.modelo import CalculadoraModel

class CalculadoraControl:
    
    def __init__(self):
        self.modelo = CalculadoraModel()
        self.valor_1 = 0
        self.valor_2 = 0
        self.resultado = 0
        self.historial = ""
        
        
        
    def agregar_primer_valor(self, valor_1):
        self.modelo.set_valor_1(float(valor_1))
        
    def agregar_segundo_valor(self, valor_2):
        self.modelo.set_valor_2(float(valor_2))
        
    def eliminar_valores(self):
        self.modelo.set_valor_1(0)
        self.modelo.set_valor_2(0)
        
    def sumar_valores(self):
        self.modelo.sumar()
        return str(self.modelo.get_resultado())
    
    def restar_valores(self):
        self.modelo.restar()
        return str(self.modelo.get_resultado())