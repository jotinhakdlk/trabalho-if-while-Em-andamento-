print("Verificador de preço, analisarei a partir de seu sexo e idade")

respostaValida = False

while(respostaValida == False):
    SEntrada = input("Qual seu sexo?(M- Masculino F- Feminino) Resposta: ").lower()
    if(SEntrada not in ["m","f"]):
        print("Resposta inválida!")
    else:
        respostaValida = True

idade = int(input("Qual sua idade? Resposta:"))

if(idade < 10 or idade >65):
    print("O valor da entrada é R$0,50")
elif(idade >= 10 and idade <= 17):
    print("O valor da entrada é R$4,28")
elif(SEntrada == "f" and idade >=18 and idade <=65):
    print("O valor da entrada é R$5,50")
elif(SEntrada == "m" and idade >=18 and idade <=65):
    print("O valor da entrada é R$8,25")