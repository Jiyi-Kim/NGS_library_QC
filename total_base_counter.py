#!/usr/bin/env python3

import os
import sys
import gzip

## Usage
# python total_base_counter.py {fastq_file}_R1.fastq.gz

fq_path = sys.argv[1]

fq_name = os.path.basename(fq_path)
total_bases = 0
with gzip.open(fq_path, "rt") as fq:
    for i, line in enumerate(fq): # fq index 1 = sequences
        if i % 4 == 1:
            seq = line.strip()
            total_bases += len(seq)

Gbp = total_bases/1e9

print(fq_name, total_bases, Gbp, sep='\t')
