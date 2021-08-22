iqsub
cd /ngc/projects/gm_ext/valgof/scriptos/unsolved

module load perl/5.24.0
module load vcftools/0.1.16
module load htslib/1.10.2
module load bcftools/1.10
module load bedtools/2.27.1
module load vt/0.5772
module load ensembl-vep/100.4

module load snakemake/6.0.4

snakemake --cluster "qsub -A gm_ext -l nodes=1:ppn=20,mem=100gb,walltime=99:00:00 -V -X" -j --latency-wait 400000
## -R vcf2tsv # -R option used to force rerun certain rules
