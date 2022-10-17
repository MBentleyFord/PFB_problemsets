#!/usr/bin/env python3 
#The enzyme ApoI has a restriction site: R^AATTY where R and Y are degenerate nucleotides. See the IUPAC table to identify the nucleotide possibilities for the R and Y. Write a regular expression to find and print all occurrences of the site in the following sequence Python_07_ApoI.fasta.

import re
fastafile=open('/users/student/prbproblemsets/pyth3/txt_files/Python_07_ApoI.fasta','r')
fastafile_string=fastafile.read()



found=re.findall(r"[AG]AATT[CT]",fastafile_string)
print(found)


