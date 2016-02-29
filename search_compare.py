#!/user/bin/env python
# -*- Coding: utf-8 -*-

"""
IS211 - Week 4 - Assignment 4 Part I
"""

import time


def sequential_search(seq, lookup):
    """
    Sequential search algorithm
    :param seq: (Sequence) - Unordered sequence to search
    :param lookup: (Mixed) - List item to search
    :return: (Int) - Index of match
    """
    start = time.time()
    idx = 0
    res = -1
    while idx < len(seq):
        if seq[idx] == lookup:
            res = idx
            break
        else:
            idx += 1
    end = time.time()
    return (res, end - start)


def ordered_sequential_search(seq, item):
    """
    Ordered sequential search algorithm
    :param seq: (Sequence) - List to search
    :param item: (Int) - Number to search in list
    :return: (Int) - Index of match
    """
    seq.sort()
    start = time.time()
    idx = 0
    res = -1
    while idx < len(seq):
        if seq[idx] == item or seq[idx] > item:
             res = idx
             break
    end = time.time()
    return (res, end - start)


def binary_search_iterative(seq, item):
    """
    Iterative binary search
    :param seq: (Sequence) - List to search
    :param item: (Int) - Number to search in list
    :return: (Int) - Index of match
    """
    start = time.time()
    head = 0
    last = len(seq) - 1
    res = -1
    if last != head:
        while head < last:
            middle = (head + last) // 2
            if seq[middle] == item:
                res = middle
                break
            elif item < seq[middle]:
                last = middle - 1
            else:
                last = middle + 1
    end = time.time()
    return (res, end - start)


def binary_search_recursive(seq, item):
    """
    Recursive binary search
    :param seq: (Sequence) - List to search
    :param item: (Int) - Number to search in the list
    :return: (Int) - Index of match
    """
    start = time.time()
    head = 0
    curr = len(seq)
    res = -1
    stop = False
    if curr != head and not stop:
        middle = (head + len) //2
        if seq[middle] == item:
            res = middle
            stop = True
        elif seq[middle] < item:
            binary_search_recursive(seq[middle - 1], item)
        else:
            binary_search_recursive(seq[middle + 1], item)
    end = time.time()
    return (res, end - start)


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

def average(seq):
    """
    Calculates an average
    :param seq: List
    :return: Numeric
    """
    return (sum(seq)/len(seq))

if __name__ == '__main__':
    import random
    import time

    SEQ = dict()
    SEQ['500'] = shuffle_list([x for x in xrange(500)])
    SEQ['1000'] = shuffle_list([x for x in xrange(1000)])
    SEQ['10000'] = shuffle_list([x for x in xrange(10000)])

    stats = {'seq': 0.0,
             'oseq': 0.0,
             'bin': 0.0,
             'rbin': 0.0}

    for k, nums in SEQ.iteritems():
        for count in xrange(100):
            length = len(nums)
            stats['seq'] += sequential_search(nums, -1)[1]
            stats['oseq'] += ordered_sequential_search(nums, -1)[1]
            stats['bin'] += binary_search_iterative(nums, -1)[1]
            stats['rbin'] += binary_search_iterative(nums, -1)[1]
        for key, stat in stats.iteritems():
                type = 'Sequential Search'
                if key == 'oseq':
                    type = 'Ordered Sequential Search'
                elif key == 'bin':
                    type = 'Iterative Binary Search'
                elif key == 'rbin':
                    type = 'Recursive Binary Search'
                type + ' took %10.7f seconds to run, on average' % (stat/length)










