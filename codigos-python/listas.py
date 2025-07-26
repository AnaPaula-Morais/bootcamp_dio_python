frutas = ["laranja", "maça", "uva"]
print(frutas)
frutas[0] #laranja
frutas[2] #uva

frutas = []
print (frutas)

letras = list("python")
print(letras)

#numeros = list(range(10))
#print(numeros)

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])


numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numeros)


n = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]     
print(n)