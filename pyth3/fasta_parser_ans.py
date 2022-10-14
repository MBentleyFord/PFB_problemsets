#!/usr/bin/env python3
#Create a FASTA parser, or modify your FASTA parser from the previous problem set, to use regular expressions. Also make sure your parser can deal with a sequence that is split over many lines.

import re

fastafile=open('/users/student/prbproblemsets/pyth3/txt_files/Python_07.fasta','r')

fasta_dict={}
sequence=''
for line in fastafile:
    line=line.rstrip()
    match=re.match(r'>(\S+)\s+(.*)',line) 
    if match:
         if sequence:
             fasta_dict[fasta_key]=sequence
             fasta_key=match.group(1)
             sequenc=''
         else:
             fasta_key=match.group(1)
             sequence=''
    else:
          sequence += line
fasta_dict[fasta_key]=sequence

for fasta_key in fasta_dict:
   print(fasta_key,fasta_dict[fasta_key], sep='\t')

