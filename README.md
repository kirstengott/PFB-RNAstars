# PFB-RNAstars
RNA-seq pipeline team at programming for biology 2018


Data:
https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE85591

star documentation:
https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf 


# Download the Data from the SRA:

`cat SraAccList.txt | parallel -j 7 fastq-dump --gzip {}` 
