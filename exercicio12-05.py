from os import system as lt
lt("cls")



try:
    idade = int(input("Digite sua idade: "))
    print(f"Voce tem {idade} anos. ")

except ValueError:
    print("ERRO!! Por favor digite um numero inteiro válido para idade.")    