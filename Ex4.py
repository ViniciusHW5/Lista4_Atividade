#4 – No Senailandia mulheres e homens poder servir do pais. O serviço e opcional e muito comum que as pessoas se apresentem para o serviço em algum momento da vida . 
# existe uma única restrição para o ingresso que e a idade da pessoa:
#A.	Para mulheres a idade aceita é entre 21 e 34 anos 
#B.	Para Homens a idade aceita é entre 18 e 39 anos. 
#Escreva um programa que leia 3 dados de entrada : nome da pessoa, idade, e sexo e informe se a pessoa sera aceita ou não para o serviço. Obs: para o Sexo deve ser lido 
# apenas um caractere que pode ser ‘f’ ou ‘F’ para feminino ‘m’ ou ‘M’ masculino 
nome = ("Digite o nome: ")
idade = int(input("Digite A idade: "))
gereno = input("Digite seu gereno: ")
if gereno ==("M") or ("m") and idade >= 18 and idade < 39:
    print("voce pode servir.")
if gereno ==("F") or ("f") and idade >= 21 and idade < 34:
    print("voce pode servir.")
else:
    print('descupa voce nao pode servir')
