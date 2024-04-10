from itertools import permutations

input = 'nqp'

perms = [''.join(p) for p in permutations(input)]
print(len(perms))
print(input)
print(perms)
