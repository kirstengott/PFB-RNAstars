#!/usr/bin/env python3

# Take file(s) from command line and conduct raw read generation using HTseq as a counter

import sys
import subprocess

aligned_sam = sys.argv [1]
gtf_reads = sys.argv[2]

def HTseqwrapper(sam, gtf):
    output = subprocess.check_output('htseq-count -m union -r pos -i gene_id -a 10 --stranded=no {} {}'.format(sam, gtf), shell=True)
    return output

test = HTseqwrapper(aligned_sam, gtf_reads)
