# Genomic_Analysis_of_Inherited_Bleeding_Disorders_15ECTS_KU_project


Files used for variant annotation and filtering

solved cases:     Snakefile_solved, config_sm_0to4.yaml, run_solved.sh
unsolved cases:   Snakefile_unsolved, config_sm_1to10.yaml, run_solved.sh




Auxillary Python scripts

merging several sample files for meta-analysis:                      merging_files.py

a script to produce separate files for different consequence variants, 
  a file withcanonical transcripts only and 
  sort on command line specified fields:                              sorting.py

produce separate file that only includes selected columns
  and sorts a df based on command-line specifies cols:               sort_columns.py
