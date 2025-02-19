#3 – uma empresa financeira concebe empréstimos a pessoa física quando o valor 
#Da parcela e menor que 8% do salario da pessoa . Escreva um programa que leia dois números reais : o valor no salario e o valor da parcela e informe se o empréstimo será 
# concebido ou não 
valor_salario =float(input("digite seu salario:"))
valor_parcela =float(input("digite sua parcela:"))
if valor_parcela < ((valor_salario * 0.08)):
    print("seu emprestimo sera consebido.")
    print("Vinicius Haskel Wilbert")
else:
    print("seu emprestimo nao sera consebido.")
    print("Vinicius Haskel Wilbert")