'''
Created on July 24, 2014

@author: raniba
'''

import argparse

__version__ = '0.0.1'


#==============================================================================
# make a UI
#==============================================================================
parser = argparse.ArgumentParser(
    prog='align_bowtie2_pe',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='''This script is used to align paired end reads to a reference genome using Bowtie2''')

# required arguments
parser.add_argument('--seq1', metavar='SEQ1',
                    help='Forward FastQ File')

parser.add_argument('--seq2', metavar='SEQ2',
                    help='Reverse FastQ File')

parser.add_argument('--reference', metavar="REFERENCE",
                    help="Path to Reference Fasta File")

parser.add_argument('--outfile', metavar="OUTFILE",
                    help="Name of the Bam file")

args, x = parser.parse_known_args()
