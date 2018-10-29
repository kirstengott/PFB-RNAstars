#!/usr/bin/env python3

#Make the python module of interest in the same directory, so the objects in the python script can be accessed by importing 
#This can be made into a pipeline by extending to include the other smaller modules


import STARalignWrapper_EH
import kallisto
import HTseqwrapper2
import sys
import os
import re

listdir=sys.argv[1]
index_gtf='../../share/genome/ensembl/Saccharomyces_cerevisiae.R64-1-1.94.gtf'
index_star='../../share/genomeDir'
index_kallisto='kallisto/S.cerevisiae_R64_kallisto_index'

filelist=os.listdir(listdir)

## print to make sure we have our files referenced (add try/except?)
print(filelist)
print(listdir)



## Add logic to run STAR and count the SAM file
count=0
for files in filelist:
    prefix = 'output/' +str(files[0:10:])
    STARalignWrapper_EH.STARalign(index_star,listdir+'/'+files,prefix)
    HTseqwrapper2.HTseqwrapperfun(prefix+'Aligned.out.sam', index_gtf, prefix)
    ## add command for a samtools view to convert sam to bam file

    
#    fo = open(prefix+'counts.txt','w')
#    fo.write(str(counts))
#    fo.close()
    count+=1
print(count)


## Add logic to run kallisto
count=0
for files in filelist:
    prefix = 'output/' +str(files[0:10:])
    kallisto.kallisto_quant(index_kallisto,prefix+'kallisto',listdir+'/'+files)
    count+=1

print(count)



#HTseqwrapper2 is the name of file to import from and HTseqwrapperfun is the name of the function in the HTseqwrapper2
#For the HTseq count step, this file will only work with HTseqwrapper2

#HTseqwrapper2.HTseqwrapperfun(aligned_sam,gtf_reads)


