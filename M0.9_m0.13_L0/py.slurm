#!/bin/bash

#SBATCH --mail-user=acpepper@ucdavis.edu #email this user
#SBATCH --mail-type=END #mail at end of run
#SBATCH --mail-type=BEGIN #mail at beginning of run
#SBATCH -p high2
#SBATCH -t 20000 # minutes
#SBATCH -J Python #name of job
#SBATCH -n 1 #number of cores
#SBATCH -o stdout.txt
#SBATCH -e stderr.txt
#SBATCH --mem=32000

#ulimit -l unlimited

python impactAnalysis.py > runlog.txt
