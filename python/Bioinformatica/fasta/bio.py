# http://tudosobrebioinformatica.blogspot.com/2011/09/arquivo-em-formato-fasta.html

from Bio import SeqIO

for fasta in SeqIO.parse("my_seq.fasta", "fasta"):
	
	print(fasta.id) # imprime o título

	print(fasta.seq) # imprime a sequência genética