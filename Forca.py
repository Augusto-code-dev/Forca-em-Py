import random as rd

palavras = [
    "abacaxi", "girassol", "aviao", "planeta", "agua", "abelha", "cadeira", "elefante", "banana", "computador",
    "nuvem", "guitarra", "sorvete", "livro", "maca", "oceano", "cachorro", "passaro", "colher", "relogio",
    "bicicleta", "janela", "papel", "montanha", "estrela", "foguete", "carro", "lua", "flor", "musica",
    "tigre", "caneta", "arco-iris", "terra", "bola", "sapato", "televisao", "morango", "ponte", "chave",
    "abobora", "telefone", "laranja", "astronauta", "arco", "cama", "peixe", "balao", "vela", "travesseiro",
    "pintura", "tesoura", "fruta", "fogao", "pinguim", "fogos de artificio", "eletricidade", "tesouro", "fantasma",
    "castelo", "abelha", "caverna", "cinto", "gato", "cacto", "faca", "luz", "teclado", "espeto", "canguru",
    "vaso", "xicara", "neve", "violino", "cobertor", "mesa", "teia", "nariz", "grama", "dado", "papelao",
    "microfone", "aranha", "ventilador", "espelho", "rocha", "sino", "chapeu", "brinquedo", "mala", "abacate",
    "sacola"
]


pchave = rd.choice(palavras)
psecreta = ["_"] * len(pchave)



print("Forca do Solis\nSeja Bem vindo!!\nBoa Sorte :)")

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False



while True:

    chances = input("Digite quantas tentativas você quer ter de 1 a 10\n")

    if is_integer(chances) and int(chances) < 10 and int(chances) > 0:
        break


while int(chances) > 0:
    print(psecreta)
    print("Voce tem " ,chances , " chances")
    letraD = input("Digite uma Letra\n").lower()
    
    if letraD in pchave: 
        for i in range(len(pchave)):
            if pchave[i] == letraD:
                psecreta[i] = letraD
    else:
        chances = int(chances) - 1
    if "_" not in psecreta:
        print(psecreta)
        print("Parabéns! Você venceu!")
        break
else:
    print("Você perdeu! A palavra era:", pchave)
        

