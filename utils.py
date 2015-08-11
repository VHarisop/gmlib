# A set of useful functions in Python

from collections import deque as dq 

def multi_remove(list_object, *indices):

# Inspired by: 
# <so>/497426/deleting-multiple-elements-from-a-list/7016104#7016104
# where <so> : stackoverflow.com/questions/

    ''' Removes objects from list at multiple indices.
        The list is modified in place and the removed 
        items are returned. 
        
        Example: 
            >> x = [1,4,6,7,8]
            >> removed = multi_remove(x, 1, 3)
            >> x
            [1, 6, 8]
            >> removed 
            [7, 4]
        
    '''

    return list(dq((list.pop(list_object, i)
        for i in sorted(indices, reverse=True)),
        maxlen = len(indices)))


def multi_intersection(*lists):

    ''' Returns a set of all items common in all the lists provided.
        Only works for lists of hashable objects. 

        The time complexity here is [n - 1] * O(L), where:
            - L is the maximum length of all sets of unique items 
            - n is the number of lists provided. '''

    return set.intersection(*map(set, lists))
