#!usr/bin/env python3

import subprocess

def SAMbam(inputSAM, outputBAM):
    output = subprocess.check_output('samtools view -Sb {} > {}'.format(inputSAM, outputBAM), shell=True)
    return output
