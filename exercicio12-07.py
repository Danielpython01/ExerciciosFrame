from os import system as lt
lt("cls")
numeros = [50, 100, 200, 300, 400]

try:
    indice = int(input("Digite um índice da lista (0 a 5): "))
    divisor = int(input("Digite um número para ser o divisor: "))
    
    resultado = numeros[indice] / divisor
    print(f"O resultado de {numeros[indice]} / {divisor} é {resultado}.")

except ValueError:
    print("Erro: Por favor, digite apenas números inteiros.")
except IndexError:
    print("Erro: O índice digitado não existe na lista.")
except ZeroDivisionError:
    print("Erro: O divisor não pode ser zero.")