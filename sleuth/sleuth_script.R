#!/usr/bin/env Rscript

args <- commandArgs(TRUE)

if (length(args) == 0L || any(c('-h', '--help') %in% args)) {
  message('usage: path/to/sleuth_script.R kallistodir resultdir
          kallistodir       path to the blastdb directory
          resultdir         path to store results
          -h, --help        to print help messages')
  q('no')
}

#load sleuth library
suppressMessages({
  library("sleuth")
  library('ggplot2')
})




#set input and output dirs

datapath = args[1]
resultdir = args[2]

dir.create(resultdir)


significance = 0.001

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
so <- sleuth_wt(so, 'conditionwt')


#summarize the sleuth results and view 20 most significant DE transcripts
sleuth_table <- sleuth_results(so, 'reduced:full', 'lrt', show_all = FALSE)
sleuth_significant <- dplyr::filter(sleuth_table, qval <= significance)
head(sleuth_significant, 20)

write.table(sleuth_significant, file = 'resultdir/significant_genes.tsv',
            quote = FALSE,
            sep = "\t",
            row.names = FALSE)

#plot an example DE transcript result
#p1 = plot_bootstrap(so, "ENST00000328933", units = "est_counts", color_by = "condition")
plot_pca(so, color_by = 'condition') +
  theme_bw() +
  ggsave(paste0(resultdir, '/pca.pdf'))

plot_qq(so, test = 'conditionwt', test_type = 'wt', sig_level = significance) +
  theme_bw() +
  ggsave(paste0(resultdir, '/qq.pdf'))

plot_volcano(so, test = 'conditionwt', test_type = 'wt', sig_level = significance) +
  theme_bw() +
  ggsave(paste0(resultdir, '/volcano.pdf'))

plot_ma(so, test = 'conditionwt', test_type = 'wt', sig_level = significance) +
  theme_bw() +
  ggsave(paste0(resultdir, '/ma.pdf'))

