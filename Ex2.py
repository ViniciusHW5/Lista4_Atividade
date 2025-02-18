#2 – Escreva um programa para exibir o nome e a categoria de um lutador o programa deve ler um String para o nome e um numero real para o peso. Conforme o peso ocorrera o 
# enquadramento da categoria segundo a tabela.

#Peso | Categoria
#Menor que 52 quilos categoria invalidade 
#Maior ou igual o 65 o menor que 65 e menor 62 categoria leve 
#maior ou igual 72 e menor 79 ligero 
#maior ou igual 79 e menor 86 meio pesado
#maior ou igual 90 e <100 pesado 
#maior ou igual 100 pesado	
nome = input(("qual nome do lutador? "))
peso = float(input("qual o seu peso? "))
if peso < (52):
    print("invalido, tente de novo")

elif peso >= (52) and peso< (65):
    print(nome)
    print("peso pena")

elif peso >= (62) and peso < (72):
    print(nome)
    print("peso pena")

elif peso >= (72) and peso < (79):
    print(nome)
    print("peso ligeiro")

elif peso >= (79) and peso < (86):
    print(nome)
    print("peso meio medio")

elif peso >= (86) and peso < (90):
    print(nome)
    print("peso medio")

elif peso >= (90) and peso < (100):
    print(nome)
    print("meio pesado")

elif peso >= (100):
    print(nome)
    print("peso pesado")



