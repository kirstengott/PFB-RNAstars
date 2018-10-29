#!/usr/bin/env python3

#Make the python module of interest in the same directory, so the objects in the python script can be accessed by importing 
#This can be made into a pipeline by extending to include the other smaller modules

import subprocess
import samtoolstest
import STARalignWrapper_EH
import kallisto
import HTseqwrapper2
import sys
import os
import re

index_kallisto='../../share/S.cerevisiae_R64_kallisto_index'

## print to make sure we have our files referenced (add try/except?)
try:
    listdir = sys.argv[1]
    print('User provided directory:', listdir)
except:
    print('Please provide a directory!!!!!!!!')
    sys.exit(1)

filelist=os.listdir(listdir)
print('file names to be run:', filelist)

#checking for index file to run star: 
try:
    index_star='../../share/genomeDir'
    os.path.exists(index_star)
except:
    print('Please provide a STAR index file!!!!!!!!')
    sys.exit(1)

#checking for a gtf file:
try:
    index_gtf='../../share/genome/ensembl/Saccharomyces_cerevisiae.R64-1-1.94.gtf'
    os.path.exists(index_gtf)
except:
    print('Please provide a gtf file!!!!!!!!')
    sys.exit(1)
## Add logic to run STAR and count the SAM file
SAMcount = 0
HTSeqCount = 0
for files in filelist:
    prefix = 'output/' +str(files[0:10:])
    STARalignWrapper_EH.STARalign(index_star,listdir+'/'+files,prefix)
    SAMcount += 1
    print(prefix + '.sam created', 'Total SAM files:', SAMcount)
#making sure SAM files were created from STAR
    try:
        os.path.exists(prefix+'Aligned.out.sam')
        print(prefix,'SAM exists')
    except:
        print('SAM file not created')
        sys.exit(1)
    prefix1 = 'output/'+str(files[0:10:])
    prefix2 = 'output/HTseq/'+str(files[0:10:])
    HTseqwrapper2.HTseqwrapperfun(prefix1+'Aligned.out.sam', index_gtf, prefix2)
    HTSeqCount += 1
    print(prefix2 + 'counts.txt created', 'Total Counts Files:', HTSeqCount)
    
    samtoolstest.SAMbam(prefix+'Aligned.out.sam', prefix+'Aligned.out.bam')

## add command for a samtools view to convert sam to bam file
    try:
        os.path.exists(prefix2+'counts.txt')
        print(prefix2,'counts file exists')
    except:
        print('Counts file not created')
        sys.exit(1)

    
#    fo = open(prefix+'counts.txt','w')
#    fo.write(str(counts))
#    fo.close()
print('Total SAM files:', SAMcount, '\t', 'Total Counts Files:', HTSeqCount)
print('STAR and HTseq complete')

## Add logic to run kallisto
kallistocount=0
for files in filelist:
    prefix = 'output/kallisto/' +str(files[0:10:])
    kallisto.kallisto_quant(index_kallisto,prefix+'kallisto',listdir+'/'+files)
    kallistocount+=1
    print(prefix+'kallisto created','Total kallisto files:',kallistocount)
    try:
        os.path.exists(prefix+'kallisto/abundance.h5')
        print(prefix,'kallisto abundance file exists')
    except:
        print('kallisto abundance file not created')
        sys.exit(1)

subprocess.check_output('./sleuth/sleuth_script.R output/kallisto output/sleuth', shell=True)
subprocess.check_output('./scripts/DESeq2.R output/HTseq output/DESeq2', shell=True)


