#Escrerva um programa que leia um valor em metros e o exiba convertido em milimetros

metros = float(input("Digite um valor em metros para ser transfomado em milimetros: "))
conversor_milimetros = metros * 1000
print(f"Você converteu {metros} metros em milimetros que será: {conversor_milimetros:.2f} milimetros")
