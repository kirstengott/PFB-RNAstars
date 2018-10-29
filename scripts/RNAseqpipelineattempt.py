#!/usr/bin/env python3

#Make the python module of interest in the same directory, so the objects in the python script can be accessed by importing 
#This can be made into a pipeline by extending to include the other smaller modules


import STARalignWrapper_EH
#import kallisto
#import HTseqwrapper2
import sys
import os
import re

listdir=sys.argv[1]
index_star='../../../share/genomeDir'

filelist=os.listdir(listdir)
print(filelist)
print(listdir)
count=0
for files in filelist:
    prefix = str(files[0:10:])
    STARalignWrapper_EH.STARalign(index_star,listdir+'/'+files,prefix)
   
    
    
    
    count+=1
print(count)





#aligned_sam = sys.argv[1]
#gtf_reads = sys.argv[2]

#STARalignWrapper.EH.STARalign(genome, reads)

#HTseqwrapper2 is the name of file to import from and HTseqwrapperfun is the name of the function in the HTseqwrapper2
#For the HTseq count step, this file will only work with HTseqwrapper2

#HTseqwrapper2.HTseqwrapperfun(aligned_sam,gtf_reads)


