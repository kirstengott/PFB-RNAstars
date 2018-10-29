#!/usr/bin/env Rscript

args <- commandArgs(TRUE)

if (length(args) == 0L || any(c('-h', '--help') %in% args)) {
  message('usage: path/to/DESeq2.R dirname resultdir
          dirname           path to "HTseqoutput" files
          resultdir         path to store results
          -h, --help        to print help messages')
  q('no')
}


directory = args[1]
resultdir = args[2]

library('dplyr')
library('DESeq2')
library('ggplot2')

#directory = '.'
#resultdir = 'deseq2'

dir.create(resultdir)


pval <-  0.001

sampleFiles <- grep("HTseqoutput",list.files(directory),value=TRUE)


sample          <- c("SRR4031331", "SRR4031332", "SRR4031333", "SRR4031334", "SRR4031335", "SRR4031336")
sampleCondition <-  c("wt", "wt", "wt", "DRPL15B", "DRPL15B", "DRPL15B")


sample_order <- sapply(sample, function(y){base::grep(pattern = y, x = sampleFiles)})
sampleTable  <- data.frame(sampleName = sampleFiles[sample_order],
                          fileName = sampleFiles[sample_order],
                          condition = sampleCondition)

ddsHTSeq <- DESeqDataSetFromHTSeqCount(sampleTable = sampleTable,
                                       directory = directory,
                                       design= ~ condition)

dds <- DESeq(ddsHTSeq)

resultsNames(dds) # lists the coefficients

res <- results(dds, name="condition_wt_vs_DRPL15B")



## make a PCA plot
rld     <- rlogTransformation(dds, blind = TRUE)

DESeq2::plotPCA(rld) + theme_bw() + ggsave(filename = paste0(resultdir, '/pca.pdf'))





df <- res %>%
  na.omit(.) %>%
  data.frame(., stringsAsFactors = FALSE) %>%
  mutate(significance_group = ifelse(padj <= pval, yes = 'yes', no = 'no'))



## make a MA plot

ggplot(df, aes(x = log(baseMean), y = log2FoldChange, group = significance_group, colour = significance_group))  +
  geom_point() +
  xlab("A = Mean of log2(Abundance)") + ylab("M = log2(Fold Change)") +
  scale_color_manual(values = c("gray24", "red")) +
  theme_bw() +
  ggsave(paste0(resultdir, '/ma.pdf'))



## make a volcano plot
ggplot(df, aes(x = log2FoldChange, y = -log(padj, base = c(10)), group = significance_group, colour = significance_group)) +
  geom_point() +
  xlab("M = log2(Fold Change)") + ylab("-log10(Adjusted P-Value)") +
  scale_color_manual(values = c("gray24", "red")) +
  theme_bw() +
  ggsave(paste0(resultdir, '/volcano.pdf'))




## make a qq plot
res <- dplyr::mutate(df, significant = padj < pval)

pnts <- stats::qqnorm(res$log2FoldChange, plot.it = FALSE)
res <- dplyr::mutate(res, theoretical = pnts[["x"]],
                     observed = pnts[["y"]])
y <- quantile(res$observed, c(0.25, 0.75))
x <- qnorm(c(0.25, 0.75))
slope <- diff(y)/diff(x)
intercept <- y[1L] - slope * x[1L]
p <- ggplot(res, aes(theoretical, observed))
p <- p + geom_point(aes(colour = significant), alpha = 0.2)
p <- p + scale_colour_manual(values = c("black", 'red'))
p <- p + xlab("theoretical quantile")
p <- p + ylab(paste0("observed quantile"))
p + theme_bw() +
  ggsave(paste0(resultdir, '/qq.pdf'))




