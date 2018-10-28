#!/usr/bin/env python3
#Make the python module of interest in the same directory, so the objects in the python script can be accessed by importing 

import HTseqwrapper2
import sys

aligned_sam = sys.argv[1]
gtf_reads = sys.argv[2]

#print(HTseqwrapper2.aligned_sam)
#print(HTseqwrapper2.gtf_reads)

HTseqwrapper2.HTseqwrapperfun(aligned_sam,gtf_reads)


