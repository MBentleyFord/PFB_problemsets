#!/usr/bin/env python3

#Open and print the reverse complement of each sequence in Python_06.seq.txt. Each line is the following format: seqName\tsequence\n. Make sure to print the output in fasta format including the sequence name and a note in the description that this is the reverse complement. Print to STDOUT and capture the output into a file with a command line redirect '>'.
 

finalfasta2=open('/Users/student/prbproblemsets/pyth3/txt_files/Python_06_fasta.seq.txt','w')

fasta_dict={}
with open('/Users/student/prbproblemsets/pyth3/txt_files/Python_06.seq.txt','r') as raw:
	for line in raw:
		line=line.rstrip()
		gene,sequence=line.split('\t')

		sequence=sequence.replace('A','t')
		sequence=sequence.replace('T','a')
		sequence=sequence.replace('G','c')
		sequence=sequence.replace('C','g')

		revsequence=sequence[::-1]
		upperrevsequence=revsequence.upper()
		fasta_dict[gene]=upperrevsequence

for gene,sequence in fasta_dict.items():
	print('>' + gene + '\n' + sequence + '\n')
	finalfasta='>' + gene + '\n' + sequence + '\n'
	finalfasta2.write(finalfasta)
finalfasta2.close()
              
