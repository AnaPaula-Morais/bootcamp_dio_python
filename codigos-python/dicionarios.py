pessoa = {
    "nome": "Ana Paula",
    "idade": 36
}

pessoa = dict(
    nome = "Ana Paula",
    idade = 36
)

pessoa ["estado_civil"] = "Casada"

print(pessoa)

# métodos dicinários: clear, copy, fromkeys, get, items, keys, pop, popitem, setdefault, update, values, in, del

carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}
print(carro.get("motor"))