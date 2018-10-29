#!/usr/bin/env python3

# I want this to take a file from command line (list of files?)
# and allign giving a known set/location of indices.

import sys
import subprocess

genome = sys.argv[1]
reads = sys.argv[2]

#if readsFile endswith '.fastq.gz':
#       readsFile = sys.argv[2]
#else:
#       print('Wrong file type. gunzipped fastq required')



def STARalign(genomeDir, readsFile):
#    	prefix = str(readsFile[0:10:])
#	prefix_output = './path/{}'.format(prefix)
#	need to add '--outFileNamePrefix {}' to subprocess output check
	output = subprocess.check_output('STAR --runThreadN 15 --genomeDir {} --readFilesIn {} --readFilesCommand gunzip -c --quantMode GeneCounts'.format(genomeDir, readsFile,), shell=True)
    return output

test = STARalign(genome, reads)

