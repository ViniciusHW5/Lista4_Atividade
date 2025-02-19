#5 – No comércio o conceito de margem bruta é uma portagem que é aplicada ao preço de custo para se obter o preço de venda. 
# Uma loja tem como política comercial aplicar margem bruta de 45% quando o preço de custo e menor ou igual a 100 reais se o 
# produto custa mais do que isso e a margem bruta e 35%. Escreva um programa que leia o preço de custo do produto e mostre na
#  tela seu preço de venda com duas 
preco_custo =float(input("Digite o preço de custo do produto: "))
if preco_custo <=100:
    margem = 0.45
else:
    margem = 0.35
preco_venda =preco_custo * (1+margem)
print("O preço de venda do protudo é:R$",preco_venda)
print("Vinicius Haskel Wilbert")