#map

def dobro(x):
	return x*2

valor = [1,2,3,4,5,6]

valor_dobrado = map(dobro, valor)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado) 

# pega cada elemeno da lista, e determina cada função

print("\n") #quebra de linha

# função lambda
# Faz combinação com outras funções
#função que pode ser utilizada uma única vez
valor2 = [1,2,3,4,5,6]

valor_dobrado = map(lambda i: i*2, valor2)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado) 
