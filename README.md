
# PFB-RNAstars
RNA-seq pipeline team at programming for biology 2018


Data:
https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE85591

star documentation:

https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf 

sleuth intro:
https://pachterlab.github.io/sleuth_walkthroughs/trapnell/analysis.html

Kallisto Blog post: https://liorpachter.wordpress.com/2015/05/10/near-optimal-rna-seq-quantification-with-kallisto/

Data Download:

`cat SraAccList.txt | parallel -j 7 fastq-dump --gzip {}`


Data subsample:
`for f in `ls *fastq`; do ~/git/seqtk/seqtk sample -s100 $f 10000 >../test/$f; done`