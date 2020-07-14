# reduce
from functools import reduce

def soma(x,y):
	return x+y

lista = [1,3,5,7,9,10,20,50]

soma = reduce(soma, lista)
print(soma)

#importa uma biblioteca
#faz uma função
#cria uma variável, no caso soma
#o soma e lista, recebe o x e y