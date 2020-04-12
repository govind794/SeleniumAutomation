# odds = set([1, 3, 5, 7, 9])
# evens = set([2, 4, 6, 8, 10])
# primes = set([2, 3, 5, 7])
# composites = set([4, 6, 8, 9, 10])
#
# print(odds.union(evens))
#
# print(evens.union(odds))
#
# print(odds.intersection(primes))
# print(evens.intersection(composites))
#
# print(2 in primes)
#
# print(2 in odds)
#
# print(3 not in evens)

from  numpy import random
import numpy as np
# dataset = np.array(['paul', 'jacob', 'vince', 'paul', 'miky', 'jacob', 'warren'])
# new_var = (dataset == 'paul') | (dataset == 'jacob')
# print (new_var)

# percentiles = [98, 76.37, 55.55, 69, 88]
# first_subject = np.array(percentiles)
# print (first_subject.dtype)

series = [[23,45,12,679], [14,48,69,38]]
new_series = np.array(series)
print (new_series.ndim)
print (new_series.shape)
print (new_series.dtype)