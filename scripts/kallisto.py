#!/usr/bin/env python3


import subprocess
import sys

#index=sys.argv[1]
#readfile=sys.argv[2]
def kallisto_index(index_name,fasta_file):
    kallisto_indexfile=subprocess.check_output('kallisto index --index={} {}'.format(index_name,fasta_file),shell=True)
    return kallisto_indexfile
#takes fasta file and makes it into an index for kallisto alignment


def kallisto_quant(kallisto_indexfile, outfile_name, reads):
    kallisto_counts=subprocess.check_output('kallisto quant -b 5 -i {} -o {} --single -l 51 -s 10 {}'.format(kallisto_indexfile, outfile_name, reads), shell=True)
    return kallisto_counts

#takes in index file made in index step from fasta file
#also takes in fastq files and 


#kallisto_quant(index,readfile)



