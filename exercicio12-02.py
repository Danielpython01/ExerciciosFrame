from os import system as lt
lt("cls")
pessoas_texto = input("Quantas pessoas tem na sala? ")

try:
    numero_pessoas = int(pessoas_texto)
    resultado = 100 / numero_pessoas
    print(f"Cada pessoa recebe {resultado:.2f} partes.")

except:
    print("Não é possivel dividir por 0 pessoas, por favor, digite somente o numero inteiro!")