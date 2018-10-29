#!/usr/bin/env python3

#Take file(s) from command line and conduct raw read generation using HTseq as a counter
#Save this python script as a module that can imported and cobbled together with other modules like building blocks to create a larger applicatio/pipeline.
#name: HTseqwrapper2.py
#This file does not work on its own, must be used with HTmodules.py

import sys
import subprocess

#define few objects below (variables, function)

#aligned_sam = sys.argv [1]
#gtf_reads = sys.argv[2]

def HTseqwrapperfun(sam, gtf):
    output = subprocess.check_output('htseq-count -m union -r pos -i gene_id -a 10 --stranded=no {} {}'.format(sam,gtf), shell=True)
    return output

#test = HTseqwrapperfun(aligned_sam, gtf_reads)
