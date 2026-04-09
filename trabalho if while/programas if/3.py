print("Me diga qual ação deseja realizar e dois numeros")
print("Qual cálculo deseja realizar? (1-Soma 2-Diferença 3-Produto 4-Divisão )")

acao = int(input("Ação desejada: "))

n1 = float(input("Primeiro número: ").replace(",", "."))
n2 = float(input("Segundo número: ").replace(",", "."))

if(acao == 1):
    print("Certo, irei realizar a soma dos números")
    resultado = n1 + n2
    print(f"A soma de {n1} e {n2} é igual a {resultado}")

elif(acao == 2):
    print("Certo, verificar a diferença de valor entre os números")
    if(n1 > n2):
        resultado = n1 - n2
    else:
        resultado = n2 - n1
    print(f"O valor da diferença entre {n1} e {n2} números é igual a {resultado}")

elif(acao == 3):
    print("Certo, irei analisar o produto dos dois números")
    resultado = n1 * n2
    print(f"O produto de {n1} e {n2} é igual a {resultado}")

elif(acao == 4):

    while(n2 == 0):
        print("Não é possível dividir por 0, digite um novo denominador")
        n2 = float(input("Novo denominador: ").replace(",", "."))
    print("Certo, irei fazer a divisão dos valores")
    resultado = n1 / n2
    print(f"O resultado da divisão entre {n1} e {n2} é igual a {resultado}")
