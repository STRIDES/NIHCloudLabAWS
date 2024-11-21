import pandas as pd
import subprocess

# Step 1: Read the sample sheet
sample_sheet = pd.read_csv('samplesheet.csv')

# Step 2: Run FastQC
for index, row in sample_sheet.iterrows():
    fastqc_command = f"fastqc {row['file_path']} -o ./fastqc_results/"
    subprocess.run(fastqc_command, shell=True)

# Step 3: Run MultiQC
multiqc_command = "multiqc ./fastqc_results/ -o ./multiqc_report/"
subprocess.run(multiqc_command, shell=True)

# Step 4: Run STAR aligner
for index, row in sample_sheet.iterrows():
    star_command = f"STAR --genomeDir /path/to/genome --readFilesIn {row['file_path']} --outFileNamePrefix ./star_results/{row['sample_id']}"
    subprocess.run(star_command, shell=True)

# Step 5: Index BAM files with Samtools
for index, row in sample_sheet.iterrows():
    bam_file = f"./star_results/{row['sample_id']}.bam"
    samtools_command = f"samtools index {bam_file}"
    subprocess.run(samtools_command, shell=True) 

