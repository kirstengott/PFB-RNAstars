#!/usr/bin/env python3


import subprocess
import sys


#rtn = subprocess.check_output('ls -l', shell=True)  # specify you want to capture STDOUT
#stdout = rtn.decode('utf-8')

#lines = stdout.splitlines()
#print(lines)


#files=os.path.dirname(/projects/rna-stars/cho/PFB-RNAstars/data/test)
#fileDir = os.path.dirname(os.path.realpath('__file__'))
#print fileDir
#filename = os.path.join(fileDir, '../data/test/SRR4031331.fastq.gz')
#readFile(filename)
index=sys.argv[1]
readfile=sys.argv[2]


def kallisto_quant(genome,reads):
    kallisto_counts=subprocess.check_output('kallisto quant -i {} -o kallisto_quant_SRR4031332 --single -l 51 -s 10 {}'.format(genome,reads), shell=True)  # specify you want to capture STDOUT
   # stdout = rtn.decode('utf-8')
   # lines = stdout.splitlines()
    return kallisto_counts

kallisto_quant(index,readfile)



