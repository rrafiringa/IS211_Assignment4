#!/user/bin/env python
# -*- Coding: utf-8 -*-

"""
IS211 - Week 4 - Assignment 4 Part dataset
"""

import random


def shuffle_list(seq):
    """
    Shuffles a list of any size
    :param seq: (List) - List to shuffle
    :return: (List) - Shuffled list
    """
    out = []
    for i in xrange(len(seq)):
        num = random.choice(seq)
        seq.remove(num)
        out.append(num)
    return out


SEQ = dict()
SEQ['500'] = shuffle_list([x for x in xrange(500)])
SEQ['1000'] = shuffle_list([x for x in xrange(1000)])
SEQ['10000'] = shuffle_list([x for x in xrange(10000)])