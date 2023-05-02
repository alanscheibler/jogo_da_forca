import os
import string
alfabeto = list(string.ascii_lowercase)

def limpar():
    os.system("cls")
    
def resposta():
    while True:
        letra = input("Digite uma letra: ").lower()
        if letra in alfabeto:
            return letra
        else:
            print(cores[1] + "Digite um caractere válido por favor! " + cores[0])
            limpar()

def sHistorico():
    try:
        historico = open ("historico.txt", "r")
    except:
        historico = open("historico.txt", "w")
        historico.close()
        historico = open("historico.txt", "r")
    dados = historico.readlines()
    historico.close
    return dados

def eHistorico(dados):
    historico = open("historico.txt", "w")
    historico.writelines(dados)
    historico.close()

cores = [
    "\033[0m", # 0 -branco
    "\033[1;33;40m", #1 - amarelo
    "\033[1;34;40m", #2 - azul
    "\033[1;36;40m", #3 - ciano
    "\033[1;32;40m", #4 - verde
    "\033[1;31;40m", #5 - vermelho
]

def menuHistorico():
    try:
        with open("historico.txt", "r") as partidas:
            dados2 = partidas.read()
            print(dados2)
            input("Pressione " + cores[2] + "(enter) " + cores[0] + "para sair")
    except FileNotFoundError:
        print("Ainda não há histórico, jogue uma partida e volte aqui vara verificar os resultados!")