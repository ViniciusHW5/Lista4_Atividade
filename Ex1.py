#1 - Escreva um programa que forneça um tipo de aplicação financeira adequado a um investidor a partir de dois dados fornecidos :
#O grau de aceitação de risco
#O grau de aceitação e o valor e a ser investido 
#O grau de aceitação de risco deve ser lido no teclado na forma BX ou AL
#Se fornecido algo diferente disso o programa deve mostra uma mensagem indicando que foi fornecido dado invalido. Para o valor dever ser numero real
aceita_risc1 = input ("qual a sua aceitação de risco, bx ou al? ")
if aceita_risc1 == "bx":
    rend1 =int(print("quando você quer depositar? "))    
    if rend1 < 1000.00:
        print("você deve abrir uma poupança")
    if rend1 >=1000.00:
        print("você deve abrir uma renda fixa")
    elif aceita_risc1 == "al":
        rend2 =int(input("quanto vc quer depositar? "))
