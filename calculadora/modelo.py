class CalculadoraModel:
    
    MENSAJE_EXITO = "Operación realizada con exito"
    MENSAJE_ERROR = "No se puede dividir entre 0"
    
    # Constructor con variables iniciales
    def __init__(self, valor_1=0.0, valor_2=0.0):
        self.valor_1 = valor_1
        self.valor_2 = valor_2
        self.resultado = 0.0
        self.resultados = []
        self.historial = []
    
    # Historial
    def add_resultados(self):
        self.resultados.append(self.resultado)
        
    def add_historial(self, operador):
        self.historial.append(self.to_string(operador))

    # Operaciones
    def sumar(self):
        self.resultado = self.valor_1 + self.valor_2
        self.add_resultados()
        self.add_historial("+")
        return [True, self.MENSAJE_EXITO]
        
    def restar(self):
        self.resultado = self.valor_1 - self.valor_2
        self.add_resultados()
        self.add_historial("-")
        return [True, self.MENSAJE_EXITO]
        
    def multiplicar(self):
        self.resultado = self.valor_1 * self.valor_2
        self.add_resultados()
        self.add_historial("x")
        return [True, self.MENSAJE_EXITO]
        
    def dividir(self):
        try:
            self.resultado = self.valor_1 / self.valor_2
            self.add_resultados()
            self.add_historial("/")
            return [True, self.MENSAJE_EXITO]
        except Exception:
            return [False, self.MENSAJE_ERROR]
        
    # Geters and Seters
    def get_valor_1(self):
        return self.valor_1
    
    def set_valor_1(self, valor):
        self.valor_1 = valor
    
    def get_valor_2(self):
        return self.valor_2
        
    def set_valor_2(self, valor):
        self.valor_2 = valor
        
    def get_resultado(self):
        return self.resultado
    
    def set_resultado(self, resultado):
        self.resultado = resultado
        
    def get_resultados(self):
        return self.resultados
    
    def set_resultados(self, array):
        self.resultados = array
        
    def get_historial(self):
        return self.historial
    
    def set_historial(self, array):
        self.historial = array
    
    def to_string(self, operador):
        return f"{self.get_valor_1()} {operador} {self.get_valor_2()} = {self.get_resultado()}"
    
    