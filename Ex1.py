#1 - Escreva um programa que forneça um tipo de aplicação financeira adequado a um investidor a partir de dois dados fornecidos :
#O grau de aceitação de risco
#O grau de aceitação e o valor e a ser investido 
#O grau de aceitação de risco deve ser lido no teclado na forma BX ou AL
#Se fornecido algo diferente disso o programa deve mostra uma mensagem indicando que foi fornecido dado invalido. Para o valor dever ser numero real

rend1 =float(print("quando você quer depositar? "))    
aceita_risc1 = input ("qual a sua aceitação de risco, bx ou al? ").strip().lower()
if aceita_risc1 == "bx" and rend1 < 1000.00:
    print("você deve abrir uma poupança")
 if rend1 > 1000.00:

#    print("você deve abrir uma renda fixa")
#else aceita_risc1 == "al":
#    rend2 =float(input("quanto vc quer depositar? "))
#    if rend2 <(1000.00):
#        print("voce deve investir em bitcoin. ")
#    else:
#        print("voce deve abrir uma ação")
#else:
#    print("dado informado invalido")