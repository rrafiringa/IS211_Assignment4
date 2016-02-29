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
    if last != 0:
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
    res = -1
    stop = False
    if len(seq) == 0:
        stop = True
    if not stop:
        midpoint = len(seq) // 2
        if seq[midpoint] == item:
            res = midpoint
            stop = True
        elif item < seq[midpoint]:
            return binary_search_recursive(seq[:midpoint], item)
        else:
            return binary_search_recursive(seq[midpoint + 1:], item)

    end = time.time()
    return (res, end - start)


if __name__ == '__main__':
    import random
    from data import *

    stats = {'seq': 0.0,
             'oseq': 0.0,
             'bin': 0.0,
             'rbin': 0.0}

    for k, nums in SEQ.iteritems():
        print 'Size: ', k
        length = len(nums)

        for count in xrange(101):
            stats['seq'] += sequential_search(nums, -1)[1]
            stats['oseq'] += ordered_sequential_search(nums, -1)[1]
            stats['bin'] += binary_search_iterative(nums, -1)[1]
            stats['rbin'] += binary_search_iterative(nums, -1)[1]
        print 'Count: ', count
        for key, stat in stats.iteritems():
            search_type = 'Sequential Search'
            if key == 'oseq':
                search_type = 'Ordered Sequential Search'
            elif key == 'bin':
                search_type = 'Iterative Binary Search'
            elif key == 'rbin':
                search_type = 'Recursive Binary Search'
            print search_type + ' took %10.7f seconds to run, on average' % (stat / length)










