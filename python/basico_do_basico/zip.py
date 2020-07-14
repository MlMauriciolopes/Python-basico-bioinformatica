# zip
#concatena listas (juntar)

lista1 = [1,2,3,4,5]
lista2 = ["abacate","bola","cachorro","dinheiro","elefante"]
lista3 = ["R$ 2,00", "R$ 4,00", "R$6,00", "R$ 8,00","R$ 10,00"]

for numero, nome, valor in zip(lista1, lista2, lista3):
	print(numero, nome, valor)