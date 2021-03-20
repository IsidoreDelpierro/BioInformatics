#DNA Toolset/Code testing file
#rebelCoder

from DNAToolkit import *
from utilities import colored
import random

randDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(50)])
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
print(f"3' {reverse_complement(DNAStr)} 5'\n")
#print(f"3' {colored(reverse_complement(DNAStr))} 5'\n")
