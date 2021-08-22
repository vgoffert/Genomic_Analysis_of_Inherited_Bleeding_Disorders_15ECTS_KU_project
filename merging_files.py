import pandas as pd
import sys
import re

### before running script: module load anaconda3/4.4.0

### requires 2 command line arguments:
# 1) text file with sample file names (samplefilenames.txt)
# 2) gene annotation file (phenotype_anno.tsv)
# 3) name of the output file (PATH/merged.tsv)

# read in text file with list of all samples file names
# and split filenames into a list object
samplefiles = []
with open(sys.argv[1], "r") as f:
    samplefiles = f.read().splitlines()


# merge files into one df
allsamples = []
for samplename in samplefiles:
    sample_i = pd.read_csv(samplename, sep="\t", header=0, na_values=".")
    # get sample number from the file name (1 or 2 digits)
    match = re.search('\d{1,2}', samplename)
    sample_i['Sample'] = f"sample{match.group()}"
    allsamples.append(sample_i)

allvariants = pd.concat(allsamples)
allvariants.sort_values(by=['IMPACT', 'Consequence', 'CADD_PHRED'], inplace=True)

# merging with gene annotation information from .bed file
# using left-merge to keep all rows from variant file
phenotypes = pd.read_csv(sys.argv[2], sep="\t", header=0, na_values=".")
annotated = pd.merge(allvariants, phenotypes, how="left", on="SYMBOL")

annotated.to_csv(str(sys.argv[3]), sep="\t", index=False, na_rep='.')
