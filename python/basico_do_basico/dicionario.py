dicionario = {"A":"ABACATE", "B":"BANANA", "C":"CAJU","D":"DAMASCO"}

#imprime dicionário inteiro
print(dicionario)

#imprime o item selecionado pelas marcações
print(dicionario["C"])

#imprime valores da chave
for chave in dicionario:
    print(dicionario[chave])

#valores em chave com índice
for chave in dicionario:
  print(chave+":"+dicionario[chave])

#dicionario em itens
for i in dicionario.items():
  print(i)

#dicionario em valores
for i in dicionario.values():
  print(i)

#dicionario em chaves
for i in dicionario.keys():
  print(i)