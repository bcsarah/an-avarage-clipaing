from os import system
from time import sleep
from random import randint
import json

# Salvar e Carregar json
def salvarJson(dados):
    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo)

def carregarJson():
    with open("dados.json", "r") as arquivo:
        return json.load(arquivo)

# Função que simula a fala de um personagem
def falar(mensagem):
    print(mensagem)
    sleep(2)

# Cria um título
def entitular(titulo: str, descricao = "", opcoes = []):
    while True:
        system('clear')
        print(f"#  {titulo.capitalize()}  #")

        # Mostra a descrição
        for linha in descricao.splitlines():
            print(f"  {linha}")
        print()

        # Mostra as opções
        i = 1
        for opcao in opcoes:
            print(f"{i} - {opcao}")
            i += 1

        # Validação e entrada de input
        entrada = int(input(">>"))

        if entrada >= 1 and entrada <= i:
            return entrada
        else:
            return 0