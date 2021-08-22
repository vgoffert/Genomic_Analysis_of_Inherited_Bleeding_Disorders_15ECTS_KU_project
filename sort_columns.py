import pandas as pd
import sys
import re
import argparse

# arg1: -s sample number on which to perform sorting (path and filenames are already included)
# arg2: -c list of columns, just: COL1 Col2 col3 COL4

parser = argparse.ArgumentParser()
parser.add_argument('--sample', '-s', dest='s', type=str)
parser.add_argument('--cols', '-c', dest='cols', type=str, nargs='+', default=[], required=False)
args = parser.parse_args()

df = pd.read_csv("/ngc/projects/gm_ext/valgof/results/project_sample/solved/project_sample_"+args.s+"/genesfiltered"+args.s+".tsv", sep="\t", header=0)
basecols = ["CHROM", "POS", "REF", "ALT", "AF", "DP", "AD", "GT", "Consequence", "SYMBOL", "Feature", "HGVSc", "HGVSp", "MANE", "SIFT", "PolyPhen", "CADD_PHRED", "REVEL", "LoFtool", "gnomAD_AF", "gnomAD_NFE_AF"]
cols_to_keep = basecols # add here --cols!
df = df.loc[:, cols_to_keep]
df.sort_values(by=args.cols, inplace=True)
df.to_csv("/ngc/projects/gm_ext/valgof/results/project_sample/solved/project_sample_"+args.s+"/"+"_".join(args.cols)+"_genesfiltered"+args.s+".tsv", sep="\t", index=False, na_rep='.')
