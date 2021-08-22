import pandas as pd
import sys
import re
import argparse


# 1st argument: merged file name  --inp  (/ngc/projects/gm_ext/valgof/results/project_sample/solved/)
# 2nd argument: (optional) --cols: list of columns to sort on
# 3rd argument: --out: output file name
# 4th argument (optional) --missing: output file name for missense variant df
parser = argparse.ArgumentParser()
parser.add_argument('--inp', type=str)
parser.add_argument('--cols', required=False, help='--cols takes a list of columns by which to perform sorting in exact order as passed', nargs='+', type=str)
parser.add_argument('--out', help='--out takes name for the output file', type=str)
# parser.add_argument('--missense', '-m', dest= 'missense', required=False, help='-m output file for Consequence: missing', type=str)
args = parser.parse_args()

# READ IN MERGED FILE
allvars = pd.read_csv(str(args.inp), header=0, sep="\t")
cols_to_keep = ["Sample", "CHROM", "POS", "REF", "ALT", "AF", "DP", "AD", "GT", "Consequence", "SYMBOL", "Feature", "HGVSc", "HGVSp", "MANE", "SIFT", "PolyPhen", "CADD_PHRED", "REVEL", "LoFtool", "gnomAD_AF", "gnomAD_NFE_AF"]
# cols_to_keep = ["Sample", "CHROM", "POS", "REF", "ALT", "QUAL", "AF", "DP", "AD", "GT", "Allele", "CANONICAL", "Consequence", "IMPACT", "SYMBOL", "category", "Tier1isth", "ThromboGenomics", "Tier2isth", "In-house", "Feature_type", "Feature", "BIOTYPE", "EXON", "INTRON", "HGVSc", "Amino_acids", "Codons", "Existing_variation", "SWISSPROT", "MAX_AF", "CLIN_SIG", "CADD_PHRED", "SIFT", "PolyPhen", "REVEL", "LoFtool"] #, "phastCons100way_vertebrate", "phyloP100way_vertebrate"
allvars = allvars.loc[:, cols_to_keep]


if args.cols:
    allvars.sort_values(by=(args.cols).split(), inplace=True)
else:
    allvars.sort_values(by=['Consequence', 'CADD_PHRED'], inplace=True)

# filter out non-canonical transcripts, leave only canonical ones - NOT A GOOD IDEA, VEP DOES NOT HAVE MUCH INFO ON CANONICALICITY
canonical_only = allvars.loc[allvars['CANONICAL'] == 'YES']
canonical_only.to_csv(str(args.out), sep="\t", index=False, na_rep='.')
#canonical_only.drop("CANONICAL", axis=1)

# creating separate tables for different Consequences
consequences = allvars.groupby("Consequence")
for cons in consequences.groups.keys():
    df = allvars[allvars["Consequence"]==cons]
    cons = cons.replace("&", "_A_")
    # !!! DON'T FORGET TO CHANGE THE FOLDER NAME: SOLVED/UNSOLVED
    output_name = str("/ngc/projects/gm_ext/valgof/results/project_sample/solved/conseq_separated/"+cons+".tsv")
    df.to_csv(output_name, sep="\t", index=False, na_rep='.')
