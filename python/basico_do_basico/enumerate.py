# função enumerate modo normal
lista = ["abacate", "bola", "cachorro", "dente", "elefante"]

for i in range(len(lista)):
	print(i, lista[i])

print("\n") # quebra de linha

# função enumerate modo python
lista2 = ["zero", "um", "dois", "três", "quatro"]
for i, nome in enumerate(lista2):
	print(i, nome)