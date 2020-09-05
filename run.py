from gen import *
import itertools
import sys

s = sys.argv[1]

# print(iter_arr(s))

# for x in iter_arr(s)[0]:
#     print(x)

for i, x in enumerate(itertools.product(*iter_arr(s))):
    print('{} {}'.format(i ,''.join(x)))
