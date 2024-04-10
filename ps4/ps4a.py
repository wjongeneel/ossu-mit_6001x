# Problem Set 4A
# Name: Willem Jongeneel
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
    if len(sequence) == 2:
        return [sequence, sequence[::-1]]
    else: 
        permutations = []
        first_char = sequence[0]
        tmp_permutations = get_permutations(sequence[1:])
        for tmp_permutation in tmp_permutations:
            for i in range(len(tmp_permutation) + 1):
                permutations.append(f'{tmp_permutation[:i]}{first_char}{tmp_permutation[i:]}')
    return permutations

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    
    # testcase 1 
    example_input = 'ieu' 
    print('Input:', example_input)
    print("Expected Output: ['ieu', 'iue', 'eiu', 'eui', 'uie', 'uei']")
    print('Actual Output:', get_permutations(example_input))

    # testcase 2 
    example_input = 'diw' 
    print('Input:', example_input)
    print("Expected Output: ['diw', 'dwi', 'idw', 'iwd', 'wdi', 'wid']")
    print('Actual Output:', get_permutations(example_input))

    # testcase 3
    example_input = 'nqp' 
    print('Input:', example_input)
    print("Expected Output: ['nqp', 'npq', 'qnp', 'qpn', 'pnq', 'pqn']")
    print('Actual Output:', get_permutations(example_input))

