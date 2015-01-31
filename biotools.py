#!/usr/bin/bash

import re
from collections import defaultdict

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
            self.data[label.replace('>', '')] = dt.replace('\n', '')

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


