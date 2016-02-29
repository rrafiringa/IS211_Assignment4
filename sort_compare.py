#!/user/bin/env python
# -*- Coding: utf-8 -*-

"""
IS211 - Week 4 - Assignment 4 Part II
"""

import time


def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            a_list[position] = current_value
    end = time.time()
    return (end - start)


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value


def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count //= 2
    end = time.time()
    return (end - start)


def python_sort(a_list):
    start = time.time()
    a_list.sort()
    end = time.time()
    return (end - start)


if __name__ == '__main__':
    from data import *

    stats = {'Insertion Sort': 0.0,
             'Shell Sort': 0.0,
             'Python Sort': 0.0}

    for key, items in SEQ.iteritems():
        length = len(items)
        print 'Size: ', key
        for count in xrange(101):
            stats['Insertion Sort'] += insertion_sort(items)
            stats['Shell Sort'] += shell_sort(items)
            stats['Python Sort'] += python_sort(items)

        for sort_type, stat in stats.iteritems():
            print sort_type + ' took %10.7f seconds to run, on average' % (stat/length)

