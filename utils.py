# A set of useful functions in Python

from collections import deque as dq 

def multi_remove(list_object, *indices):

# Inspired by: 
# <so>/497426/deleting-multiple-elements-from-a-list/7016104#7016104
# where <etc> : stackoverflow.com/questions/

    ''' Removes objects from list at multiple indices.
        The list is modified in place and the removed 
        items are returned. '''

    return list(dq((list.pop(list_object, i)
        for i in sorted(indices, reverse=True)),
        maxlen = len(indices)))

