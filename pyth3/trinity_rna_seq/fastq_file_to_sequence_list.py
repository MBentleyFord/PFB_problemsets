#!/usr/bin/env python

import os, sys



## method: seq_list_from_fastq_file(fastq_filename)
##
##  Extracts the sequence lines from a fastq file and returns a list
##  of the sequence lines
##
##  input parameters:
##
##  fastq_filename :  name of the fastq file (type: string)
##
##  returns seq_list : list of read sequences.
##                    ie.  ["GATCGCATAG", "CGATGCAG", ...]
    
fastq_filename='/Users/student/prbproblemsets/pyth3/trinity_rna_seq/reads.fq'
def seq_list_from_fastq_file(fastq_filename):
    seq_list = list()
    line_count=0
    ## begin your code
    with open(fastq_filename,'r') as fastq_files:
        for line in fastq_files:
            line=line.rstrip()
            line_count+=1
            if line_count % 2 ==0 and line_count%4 !=0:
              seq_list.append(line)
    return seq_list
print(seq_list_from_fastq_file(fastq_filename))

    ## end your code



def main():

    progname = sys.argv[0]
    
    usage = "\n\n\tusage: {} filename.fastq num_seqs_show\n\n\n".format(progname)
    
    if len(sys.argv) < 3:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    num_seqs_show = int(sys.argv[2])

    seq_list = seq_list_from_fastq_file(fastq_filename)

    print(seq_list[0:num_seqs_show])

    sys.exit(0)  # always good practice to indicate worked ok!



#if __name__ == '__main__':
#   main()
    
