Task 1: You are provided with a Python script intended to calculate the length of DNA sequences from a FASTA file. The script contains several errors that need to be identified and resolved. Your task is to debug the script and ensure it runs correctly.
Script explanation: 
1.	Read a FASTA file containing multiple DNA sequences.
2.	Calculate the length of each DNA sequence.
3.	Output the results in a CSV file with columns: Sequence ID, Sequence Length.
Script with errors: 
```
import csv

def read_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        sequence_id = None
        sequence = ''
        for line in file:
            if line.startswith('>'):
                if sequence_id:
                    sequences[sequence_id] = sequence
                sequence_id = line[1:].strip()
                sequence = ''
            else:
                sequence += line.strip()
        sequences[sequence_id] = sequence
    return sequences

def main():
    file_path = 'sequences.fasta'
    output_file = 'sequence_lengths.csv'
    
    sequences = read_fasta(file_path)
    
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Sequence ID', 'Sequence Length'])
        for seq_id, sequence in sequences.items():
            length = len(sequence)
            writer.writerow([seq_id, length])

if __name__ == '__main__':
    main()

```

Corrected Script: (run this to make sure it works) 
```
import csv

def read_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        sequence_id = None
        sequence = ''
        for line in file:
            if line.startswith('>'):
                if sequence_id:
                    sequences[sequence_id] = sequence
                sequence_id = line[1:].strip()
                sequence = ''
            else:
                sequence += line.strip()
        if sequence_id:
            sequences[sequence_id] = sequence  # Ensure the last sequence is added
    return sequences

def main():
    file_path = 'sequences.fasta'
    output_file = 'sequence_lengths.csv'
    
    sequences = read_fasta(file_path)
    
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Sequence ID', 'Sequence Length'])
        for seq_id, sequence in sequences.items():
            length = len(sequence)
            writer.writerow([seq_id, length])

if __name__ == '__main__':
    main()
```
