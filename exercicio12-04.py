from os import system as lt
lt("cls")

try:
    numerador = float(input("Digite o numerador: "))
    denominador = float(input("Digite o denominador: "))
    
    resultado = numerador / denominador
    print(f"O resultado é: {resultado}")

except ZeroDivisionError:
    print("Erro: O denominador não pode ser zero!")