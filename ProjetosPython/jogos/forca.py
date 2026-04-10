import random as rd

def mensagem_inicial():
    print("__________________________")
    print("Seja bem vindo ao forca!")
    print("__________________________")

def seleciona_palavra_aleatoria():
    arquivo = open("palavras.txt", 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()
    posicao = rd.randrange(0, len(palavras))

    palavra_secreta = palavras[posicao].lower()
    return palavra_secreta

def letras_corretas(palavra_secreta):
    return ['_' for letra in palavra_secreta]

def entrada_dados():
    chute = input('Digite uma letra: ')
    chute = chute.strip().lower()
    return chute

def chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra 
        index += 1 

def jogar_forca():

    mensagem_inicial()

    palavra_secreta = seleciona_palavra_aleatoria()

    letras_acertadas = letras_corretas(palavra_secreta)

    perdeu = False
    acertou = False
    erros = 0

    while(not perdeu and not acertou):
        chute = entrada_dados()
        #Index define a posição da letra

        if(chute in palavra_secreta):
            chute_correto(chute, palavra_secreta, letras_acertadas)
        else: 
            erros += 1
        
        acertou = '_' not in letras_acertadas

        perdeu = erros == 6
        print(letras_acertadas)

if (__name__ == "__main__"):
    jogar_forca()