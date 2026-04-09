print("Calculador de média aritmética de notas \n diga 4 de suas notas e a partir delas avaliarei a partir da média se você está ou não aprovado")
print("Digite no padrão '0,0', exemplo: nota 4,5")

valorescorretos = False

while(valorescorretos == False):
    nota1 = float(input("Valor da primeira nota: ").replace(",", "."))
    nota2 = float(input("Valor da segunda nota: ").replace(",", "."))
    nota3 = float(input("Valor da terceira nota: ").replace(",", "."))
    nota4 = float(input("Valor da quarta nota: ").replace(",", "."))
    
    if(nota1 > 10.0 or nota2 > 10.0 or nota3 > 10.0 or nota4 > 10.0):
        print("Valor incorreto!")
    else:
        valorescorretos = True

media = (nota1 + nota2 + nota3 + nota4) / 4

if(media >= 6.0):
    print("aprovado")
else:
    print("reprovado")
print(f"sua média é {media}")