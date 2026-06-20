entrada_usuario = input("Digite um número inteiro: ")

try:
    numero = int(entrada_usuario)
    print(f"Que bom ! O número {numero} é um n° inteiro válido.")

except:
    print("Erro: Por favor, digite um número inteiro válido.")