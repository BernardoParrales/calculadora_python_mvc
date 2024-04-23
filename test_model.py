from calculadora.modelo import CalculadoraModel

calculadora = CalculadoraModel(2, 3)
calculadora.sumar()
calculadora.restar()
calculadora.multiplicar()
calculadora.dividir()

calculadora.set_valor_1(5)
calculadora.set_valor_2(4)

calculadora.sumar()
calculadora.restar()

calculadora.set_valor_2(10)

calculadora.multiplicar()

calculadora.set_valor_1(100)

calculadora.dividir()


print(calculadora.resultado)
print(calculadora.get_resultados())

# print(calculadora.get_historial())

for operacion in calculadora.get_historial():
    print(operacion)
