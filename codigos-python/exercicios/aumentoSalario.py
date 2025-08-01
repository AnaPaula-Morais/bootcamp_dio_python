#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário

salario = float(input("Qual o valor do salário? "))
aumento = float(input("Qual a porcentagem do aumento? "))
porcentagem = aumento/100
novoSalario = (salario * porcentagem) + salario

print(f"O valor do aumento é: {aumento}%")
print(f"O valor do novo salário com o aumento é: R${novoSalario:.2f}")



