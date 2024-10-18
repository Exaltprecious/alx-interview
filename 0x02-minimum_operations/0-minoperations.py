#!/usr/bin/python3
'''The minimum operations coding challenge.
'''

def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int) or n <= 0:
        return 0
    
    ops_count = 0
    clipboard = 0
    done = 1

    while done < n:
        if clipboard == 0:
            # First operation: copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2  # one for copy, one for paste
        elif (n - done) % done == 0:
            # Copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2  # one for copy, one for paste
        else:
            # Paste from clipboard
            done += clipboard
            ops_count += 1  # one for paste

    return ops_count
