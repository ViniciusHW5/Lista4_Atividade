#1 - Escreva um programa que forneça um tipo de aplicação financeira adequado a um investidor a partir de dois dados fornecidos :
#O grau de aceitação de risco
#O grau de aceitação e o valor e a ser investido 
#O grau de aceitação de risco deve ser lido no teclado na forma BX ou AL
#Se fornecido algo diferente disso o programa deve mostra uma mensagem indicando que foi fornecido dado invalido. Para o valor dever ser numero real
aceita_risco = input ("qual a sua aceitação de risco, bx ou al? ").strip().lower()
if aceita_risco == 'bx' or aceita_risco == 'al':
    valor_investido =float(input("Quando voce quer depositar? "))
    if valor_investido < 1000.00:
        if aceita_risco == "bx":
            print("voce deve abrir um poupança.")
        else:
            print("voce deve abrir uma renda fixa.")
    elif aceita_risco == "al":
        if valor_investido < 1000.00:   
            print("voce deve investir em bitcoin")
    else:
        print("voce deve abrir uma ação.")
if aceita_risco != "bx" and aceita_risco != "al":
    print("Dado invalido tente novamente!")