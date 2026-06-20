from os import system as lt
lt("cls")

# Lista de países e capitais
# Use essa lista como dicionário do seu código
capitais = {
    "Brasil": "Brasília",
    "Estados Unidos": "Washington",
    "Reino Unido": "Londres",
    "França": "Paris",
    "Alemanha": "Berlim",
    "Itália": "Roma",
    "Japão": "Tóquio",
    "China": "Pequim",
    "Rússia": "Moscou",
    "Austrália": "Canberra"
}

pais_digitado = input("Digite o nome de um país para informar-mos sua capital: ")

try:

    capital = capitais[pais_digitado]
    print(f"A capital de {pais_digitado} é {capital}.")

except KeyError:
    print(f"Desculpe, o país '{pais_digitado}' não está em nossa lista.")