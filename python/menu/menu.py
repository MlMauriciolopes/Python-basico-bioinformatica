# -*- coding utf-8 -*-
menu = 0

def abrirArquivo():
   nome = input("Digite o nome do aquivo que deseja abrir: ")

   arquivo = open(nome)

   return arquivo

def lerArquivo(arquivo):

  linhas = arquivo.readlines()

  for linha in linhas:
    print: linha.strip()


while menu != 3:

  print: "(1) Abrir Arquivo\n(2) Ler Arquivo\n(3) Sair\n"

  menu = int(input("Digite a opção desejada: "))

  if menu == 1:
    arquivo = abrirArquivo()
  
  elif menu == 2:
    lerArquivo(arquivo)
  