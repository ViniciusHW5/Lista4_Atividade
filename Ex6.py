#6 – Nas eleições municipais os municípios com 200mil eleitores ou mais  tem segundo turno caso o primeiro colocado não tenha mais de 50% dos votos. 
# Escreva um programa que leia o nome do municípios, a quantidade de eleitores e quantidade de votos do candidato mas votado e informe se haverá segundo turno ou não
municipio =("Digite o nome do municipio: ")
eleitores =int(input("Digite a quantidade total de eleitores: "))
votos_mais_votados =int(input("Digite a quantidade de votos de candidado mais votado:"))
porcentagem = (votos_mais_votados / eleitores)*100
if eleitores >=200.000 and porcentagem <=50:
    print("no municipio de",municipio,"Havera segundo turno.")
else:
    print("no municipio de",municipio,"não Havera segundo turno.")