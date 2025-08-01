# Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = int(input("Qual a distância a ser percorrida? "))
velocidade = int(input("Qual a velocidade média esperada para a viagem? "))

tempo = distancia/velocidade

print(f"O tempo esperado para uma viagem de {distancia}km com uma velociade de {velocidade}km/h será {tempo:g} horas")