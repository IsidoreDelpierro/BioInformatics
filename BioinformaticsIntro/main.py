#DNA Toolset/Code testing file
#rebelCoder

from dna_toolkit import *
from utilities import colored
import random

randDNAStr = ''.join([random.choice(DNA_Nucleotides) for nuc in range(51)])
randDNAStr1 = "ATTTCGT"
randDNAStr2 = "ATTTCGTx"
randDNAStr3 = "AtCCgGGtGGt"

DNAStr = validateSeq(randDNAStr)
#print(validateSeq(randDNAStr1))
#print(validateSeq(randDNAStr2))
#print(validateSeq(randDNAStr3))
print(f'\nSequence: {DNAStr}\n')
#print(f'\nSequence: {colored(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n')
#print(colored(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))
print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')
#print(f'[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')

print(f"[4] + DNA String + Reverse Complement:\n5' {DNAStr} 3'")
#print(f"[4] + DNA String + Reverse Complement:\n5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {reverse_complement(DNAStr)[::-1]} 5' [Complement]")
print(f"5' {reverse_complement(DNAStr)} 3' [Rev. Complement]\n")
#print(f"3' {colored(reverse_complement(DNAStr))} 5'\n")
print(f'[5] + GC Content: {gc_content(DNAStr)}%\n')
print(f'[6] + GC Content in Subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n')
print(f'[7] + Aminoacids Sequence from DNA: {translate_seq(DNAStr, 0)}\n')
print(f'[8] + Codon frequency (L): {codon_usage(DNAStr, "L")}\n')
