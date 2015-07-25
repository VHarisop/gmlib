#!/usr/bin/python

import re
from operator import mul
from collections import defaultdict
from functools import reduce


def edit_distance(seq_a, seq_b):

    if not seq_a: return len(seq_b)
    if not seq_b: return len(seq_a)
    
    return edit_distance(seq_a[:-1], seq_b[:-1]) if seq_a[-1] == seq_b[-1] else 1 + min(
                edit_distance(seq_a[:-1], seq_b), 
                edit_distance(seq_a, seq_b[:-1]))


class TypeException(Exception):

    ''' TypeException is raised when passing something
        other than 'RNA' or 'DNA' as genetic material's type.
    '''
    pass

class CodonTable(object):

    ''' A class that implements a DNA/RNA codon table
        providing methods for codon lookup (common and inverse),
        codon synthesis etc.
    '''
    
    # A template RNA codon table

    rna_codon_table = {
        'A': 'GCU, GCC, GCA, GCG',
        'C': 'UGU, UGC',
        'D': 'GAU, GAC',
        'R': 'CGU, CGC, CGA, CGG, AGA, AGG',
        'N': 'AAU, AAC',
        'Q': 'CAA, CAG',
        'E': 'GAA, GAG',
        'G': 'GGU, GGC, GGA, GGG',
        'H': 'CAU, CAC',
        'I': 'AUU, AUC, AUA',
        'L': 'UUA, UUG, CUU, CUC, CUA, CUG',
        'K': 'AAA, AAG',
        'M': 'AUG',
        'F': 'UUU, UUC',
        'P': 'CCU, CCC, CCA, CCG',
        'S': 'UCU, UCC, UCA, UCG, AGU, AGC',
        'T': 'ACU, ACC, ACA, ACG',
        'W': 'UGG',
        'Y': 'UAU, UAC',
        'V': 'GUU, GUC, GUA, GUG',
        'START': 'AUG',
        'STOP': 'UAA, UGA, UAG'
    }


    def __init__(self, type='RNA'):

        ''' initializes a CodonTable class. Actions taken 
            upon initialization include parsing of the codon_table
            dictionary and storing of a length variable for each codon
            that indicates number of combinations available. 

            Should the user pass 'DNA' as type, each <U> in the codon table
            is replaced with T(Thymine) as DNA's counterpart to Uracille.

        '''

        # replace appropriate symbols depending on genetic type
        if type == 'RNA':
            self.codon_table = {k: set(v.replace(' ', '').split(',')) for k, v in self.rna_codon_table.items()}
        elif type == 'DNA':
            self.codon_table = {k: set(v.replace(' ', '').replace('U', 'T').split(',')) for k, v in self.rna_codon_table.items()}
        else:
            raise TypeException


    def codon_generators(self, codon):

        ''' returns the set of base sequences that produce 
            the given codon
        '''

        return self.codon_table[codon]


    def codon_combinations(self, codon):

        ''' returns the number of ways the given
            codon can be produced 
        '''

        return len(self.codon_generators(codon))


    def sequence_combinations(self, sequence):

        ''' returns the number of ways the
            given sequence of codons can be produced
        '''

        # returns 3 times the product of individual combinations
        # as there are 3 ways to generate a stop codon
        return reduce(mul, (self.codon_combinations(cdn) for cdn in sequence)) * 3


class FastaReader(object):

    ''' Simple reader class to read strings in FASTA format '''

    def __init__(self, path, fmt=None):

        ''' initializes a FastaReader class using a file in the given path.

            fmt is a format string that specifies format of labels.
            e.g., for Rosalind cases (>Rosalind_09) fmt would be '>\w+_\d+', 
            which is actually the default format
        '''

        if not fmt:
            fmt = '\w+_\d+'

        # init data
        self.data = defaultdict(list)

        with open(path, 'r') as f:    
            # read whole content at once
            content = ''.join(i for i in f)

        # split according to label formats
        content = re.split('(' + fmt + ')', content)

        # strip leading whitespace
        content = iter(content[1:])
        
        # group data by 2
        for (label, dt) in zip(content, content):
            self.data[label.replace('>', '')] = dt.replace('\n', '').replace('>', '')

        self.fmt = fmt


    def validate_data(self, fmt=None):

        ''' Checks the sanity of the data labels 
            to ensure that none of them has been
            stored improperly.
        '''

        if not fmt: 
            # handle FASTA case
            fmt = self.fmt.replace('>', '')

        # check that all labels match fully with the given format
        return all(re.fullmatch(fmt, lbl) for lbl in self.data)



