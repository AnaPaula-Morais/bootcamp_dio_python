# Escreva um programa que converta uma temperatura digitada em ºC para ºF. A fórmula para esta conversão é: f  = 9 * c / 5 + 32

temperaturaCelsius = int(input("Digite o valor da temperatura em Celsius: "))
conversao = (9 * temperaturaCelsius / 5) + 32

print(f"A temperatura convertida para fahrenheit é: F{conversao:.2f}")