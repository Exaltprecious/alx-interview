#!/usr/bin/python3
'''Minimum Operations python challenge'''


def minOperations(n):
    '''calculates the fewest number of
    operations needed to result in exactly n H
    characters.
    Returns:
        Integer : if n is impossible to achieve, return 0
    '''
    pasted_chrs = 1  # how many chars in the file
    my_clipboard = 0  # how many H's copied
    counter = 0  # operations counter

    while pasted_chrs < n:
        # if did not copy anything yet
        if my_clipboard == 0:
            # copyall
            my_clipboard = pasted_chrs
            # increment operations counter
            counter += 1

        # if haven't pasted anything yet
        if pasted_chrs == 1:
            # paste
            pasted_chrs += my_clipboard
            # increment operations counter
            counter += 1
            # continue to next loop
            continue

        remaining = n - pasted_chrs  # remaining chars to Paste
        # check if impossible by checking if my_clipboard
        # has more than needed to reach the number desired
        # which also means num of chars in file is equal
        # or more than in the my_clipboard.
        # in both situations it's impossible to achieve n of chars
        if remaining < my_clipboard:
            return 0

# if can't be devided
        if remaining % pasted_chrs != 0:
            # paste current my_clipboard
            pasted_chrs += my_clipboard
            # increment operations counter
            counter += 1
        else:
            # copyall
            my_clipboard = pasted_chrs
            # paste
            pasted_chrs += my_clipboard
            # increment operations counter
            counter += 2

                # if got the desired result
    if pasted_chrs == n:
        return counter
    else:
        return 0
