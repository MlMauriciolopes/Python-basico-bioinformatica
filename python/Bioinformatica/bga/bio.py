#https://www.rcsb.org/structure/1BGA  (Arquivo para estudo)
#análise de proteínas/ Estruturas de proteinas com biopython

from Bio.PDB import*

# SMCRA
parser = PDBParser()
estrutura = parser.get_structure("1BGA","1bga.pdb")
'''
modelo = estrutura[0]  #criando variáveis das estruturas que vc deseja buscar
cadeia_A = modelo['A']
residuo_100 = cadeia_A[100]
ca_residuo_100 = residuo_100['CA']'''

atomo_100 = estrutura[0]['A'][100]['CA']

atomo_101 = estrutura[0]['A'][101]['CA']

# Distancia euclidiana
distancia = atomo_101 - atomo_100

print("\n\nA distancia euclidiana entre CA do residuo 101 e 100 eh: ")
print(distancia)

