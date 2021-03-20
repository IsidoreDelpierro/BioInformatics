#DNA Toolset/Code testing file
#rebelCoder

from DNAToolkit import *
import random

randDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(20)])
randDNAStr1 = "ATTTCGT"
randDNAStr2 = "ATTTCGTx"
randDNAStr3 = "AtCCgGGtGGt"

DNAStr = validateSeq(randDNAStr)
#print(validateSeq(randDNAStr1))
#print(validateSeq(randDNAStr2))
#print(validateSeq(randDNAStr3))
print(validateSeq(randDNAStr))
print(countNucFrequency(DNAStr))
