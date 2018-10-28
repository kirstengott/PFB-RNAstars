#load sleuth library
suppressMessages({
  library("sleuth")
})

#set input and output dirs
#datapath = "/projects/rna-stars/cho/PFB-RNAstars/data/tests"
#resultdir = '/projects/rna-stars/cho/PFB-RNAstars/sleuth'
datapath = "/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/cho/PFB-RNAstars/kallisto_full"
resultdir = '/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/cho/PFB-RNAstars/sleuth'
setwd(resultdir)

#create a sample to condition metadata description
sample_id = dir(file.path(datapath))
kal_dirs = file.path(datapath, sample_id)
print(kal_dirs)
sample = c("SRR4031331", "SRR4031332", "SRR4031333", "SRR4031334", "SRR4031335", "SRR4031336")
condition = c("wt", "wt", "wt", "DRPL15B", "DRPL15B", "DRPL15B")
s2c = data.frame(sample,condition)
s2c <- dplyr::mutate(s2c, path = paste0(kal_dirs, "/abundance.h5"))
print(s2c)



#run sleuth on the data
so <- sleuth_prep(s2c, extra_bootstrap_summary = TRUE)
so <- sleuth_fit(so, ~condition, 'full')
so <- sleuth_fit(so, ~1, 'reduced')
so <- sleuth_lrt(so, 'reduced', 'full')
models(so)


#summarize the sleuth results and view 20 most significant DE transcripts
sleuth_table <- sleuth_results(so, 'reduced:full', 'lrt', show_all = FALSE)
sleuth_significant <- dplyr::filter(sleuth_table, qval <= 0.05)
head(sleuth_significant, 20)

#plot an example DE transcript result
#p1 = plot_bootstrap(so, "ENST00000328933", units = "est_counts", color_by = "condition")
p2 = plot_pca(so, color_by = 'condition')
#sleuth_live(so)
#Print out the plots created above and store in a single PDF file
pdf(file="SleuthResults.pdf")
print(p1)
print(p2)
dev.off()