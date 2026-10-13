#!/usr/bin/env python3

from atcoder.segtree import SegTree
from atcoder.dsu import DSU
from sortedcontainers import SortedDict, SortedList, SortedSet
from collections import deque, Counter
import itertools
import numpy
import re
import sys
import string

# ------------------------------------
# Array assignment
# ------------------------------------
length, *A = [5, 1, 2, 3, 4, 5]
print(length == (len(A))) # True
length, *A = [1, 1]
print(length == len(A)) # True
print(type(length)) # <class 'int'>
print(type(A)) # <class 'list'>

# ------------------------------------
# Removing multiple indexes from array
# ------------------------------------

del_indexes = lambda items, indexes: [item for index, item in enumerate(items) if index not in indexes]
ary = ["aaa", "bbb", "ccc", "ddd", "eee"]

print("del indexes=", del_indexes(ary, [0, 1, 2]))
# del indexes= ['ddd', 'eee']

# ------------------------------------
# Collect negative numbers in a list.
#
# Also, add a single value in the list.
# ------------------------------------
ary = [1, 2, 3, -1, -2, 5]
new_ary = list(filter(lambda a:a < 0, ary))
print(new_ary)
# [-1, -2]
print([x + 10 for x in new_ary])
# [9, 8]

# ------------------------------------
# Pick up some elements in array per
# specific size.
# ------------------------------------
size = 3
for start in range(0, len(ary), size):
    print(ary[start : start + size])
# [1, 2, 3]
# [-1, -2, 5]

# ------------------------------------
# Sorting 'String' numbers shows
# different result with 'Integer' numbers.
# ------------------------------------
str_ary = ["1", "2", "3", "4", "5",
           "11", "12", "13"]
str_ary.sort(reverse = True)
int_ary = list(map(int, str_ary))
int_ary.sort(reverse = True)
print(str_ary)
print(int_ary)
# ['5', '4', '3', '2', '13', '12', '11', '1']
# [13, 12, 11, 5, 4, 3, 2, 1]


# ------------------------------------
# String operation
# ------------------------------------
print("python".upper())
print("PYTHON".lower())
print("Python".swapcase())

# ------------------------------------
# Iterate array from the end index.
#
# The next code shows the print
# output of -2, -1, 3, 2, 1.
# ------------------------------------
# for i in ary[::-1]:
#     print(i)

# ------------------------------------
# Integer Division (//)
# ------------------------------------
# print(5 // 5)  => 1
# print(3 // 2)  => 1
# print(10 // 3) => 3

# ------------------------------------
# Convert decimal number to n-adic number
# ------------------------------------
def convert_dec_to_n_adic(decimal, n):

    s = ''
    while decimal > 0:
        s = str(decimal % n) + s
        decimal = decimal // n
    return s

print(convert_dec_to_n_adic(8, 2))
# '1000'

# ------------------------------------
# Remove one leftmost char (or sub string)
# in a string.
# ------------------------------------
S = "abcdefghiabc"
S = S.replace('a', '', count = 1)
# print(S)
# "bcdefghiabc"

# ------------------------------------
# SortedList
# ------------------------------------
# requires 'from sortedcontainers import SortedList, SortedSet'
sorted_list = SortedList([1, 2, 3, 4, 5])
sorted_list.add(6)
sorted_list.add(7)
print(sorted_list)
# [1, 2, 3, 4, 5, 6, 7]

# --------------------------------------------------
# List up divisors as SortedSet
#
# If 'include_edges' is True, then add both 1 and N
# to the return value.
#
# If 'include_pair' is True, then add divisor and
# its counterpair when N % divisor == 0.
#
# Note that for *GCD*, use math.gcd(A, B).
# --------------------------------------------------
def get_divisors(N, include_edges = True, include_pair = True):
    if include_edges:
        div = SortedSet([1, N])
    else:
        div = SortedSet([])
    i = 2
    while True:
        # Continue the iteration until the is math.sqrt(N).
        # math.sqrt(N) ** 2 == N and
        # when any divisor is found equal to or less than
        # math.sqrt(N), then the couterpart (pair) is
        # already found as N // i (in the path of
        # 'include_pair' == True.
        if i * i > N:
            break
        if N % i == 0:
            div.add(i)
            if include_pair and N // i != i:
                div.add(N // i)
        i += 1
    return div

print("divisors of 36 =", get_divisors(36))
# divisors of 36 = SortedSet([1, 2, 3, 4, 6, 9, 12, 18, 36])
print("divisors of 36 (include_edges = False)=",
      get_divisors(36, include_edges = False))
# divisors of 36 (include_edges = False)= SortedSet([2, 3, 4, 6, 9, 12, 18])
print("divisors of 36 (include_edges & include_pair = False)=",
      get_divisors(36, include_edges = False, include_pair = False))
# divisors of 36 (include_edges & include_pair = False)= SortedSet([2, 3, 4, 6])
print("divisors of 36 (include_edges = True, include_pair = False)=",
      get_divisors(36, include_edges = True, include_pair = False))
# divisors of 36 (include_edges = True, include_pair = False)= SortedSet([1, 2, 3, 4, 6, 36])


# ------------------------------------
# Prime Check
# ------------------------------------
def is_prime(val):
    i = 2
    while True:
        if i * i > val:
            break
        if val % i == 0:
            return False
        i += 1
        if i == val:
            break
    return True

# ------------------------------------
# Prime Factorization
# ------------------------------------
def prime_factorization(orig_N):
    N = orig_N
    factors = []
    i = 2
    while True:
        if i * i > orig_N:
            break
        if N % i == 0:
            # Continue until 'i' can divide N.
            while N % i == 0:
                factors.append(i)
                N = N // i
        i += 1

    # If the while loop (N % i == 0) sets N to 1,
    # then the prime factorization ended. No
    # additional append is required.
    #
    # The example for this is 125.
    # 125 changes like 25 => 5 => 1.
    #
    # If the last N is equal to 1, it means
    # the last divisor 'i' divided the same value
    # as i // i <=> N // N.
    #
    # Meanwhile, when the last N is not equal to 1,
    # the last value didn't divide the same value,
    # unlike the above.
    #
    # The examples for this is 7, 97 and 2020.
    # The cases should be the original N is a prime
    # number or the quotient of 'i' is bigger than
    # math.sqrt(N).
    #
    # When N = 2020 changes like 1010 => 505
    # and i=5 divides 505 to 101, the last 101 is
    # the left value as N. Do not miss this value.
    if N != 1:
        factors.append(N)

    return factors

print("prime factors of 7=", prime_factorization(7))
# prime factors of 7= [7]
print("prime factors of 125=", prime_factorization(125))
# prime factors of 125= [5, 5, 5]
print("prime factors of 36=", prime_factorization(36))
# prime factors of 36= [2, 2, 3, 3]
print("prime factors of 97=", prime_factorization(97))
# prime factors of 97= [97]
print("prime factors of 240=", prime_factorization(240))
# prime factors of 240= [2, 2, 2, 2, 3, 5]
print("prime factors of 2020=", prime_factorization(2020))
# prime factors of 2020= [2, 2, 5, 101]

# ------------------------------------
# itertools
# ------------------------------------
# requires 'import itertools'
print("permutations=", list(itertools.permutations(range(1, 4))))
print("combinations=", list(itertools.combinations(range(1, 5), 3)))
print("combinations_with_replacement=",
      list(itertools.combinations_with_replacement(range(1, 4), 3)))
print("product=", list(itertools.product(range(1, 4), range(1, 4))))
# permutations= [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# combinations= [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
# combinations_with_replacement=
# [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 2),
#  (1, 2, 3), (1, 3, 3), (2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3)]
# product= [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]


def runLengthEncode(string, get_freqs):
    chars = list(string)
    pairs = [ (k, list(g)) for k, g in itertools.groupby(chars) ]
    char_freqs = [ (t[0], len(t[1])) for t in pairs ]
    if get_freqs:
        return char_freqs
    ans = ""
    for t in char_freqs:
        c, freq = t
        ans += (c + str(freq))
    return ans

print("runLengthEncode=", runLengthEncode("foo", True)) # runLengthEncode= [('f', 1), ('o', 2)]
print("runLengthEncode=", runLengthEncode("foo", False)) # runLengthEncode= f1o2

# ------------------------------------
# Bit Brute Force
#
# List up 2**N patterns for N argument.
#
# The internal is to iterate all values from 0 to 2 ** N - 1
# and checks if binary representation of each value has 1
# on each digits like 3 = '0b11' leads to [0, 1], when N == 2.
#
# The core part is to check each binary digits by '(i >> j) & 1'
# and append 'j' to the 'ary'.
#
# (3 >> 0) & 1 => append 0 to 'ary', the rightmost digit.
# (3 >> 1) & 1 => append 1 to 'ary', the 2nd digit from the rightmost.
#
# Then, [0, 1] are added to the returned 'comb' as a one single
# element in the array, with other arrays for iterated i=0, 1, 2.
# ------------------------------------
def bit_brute_force(N, mat):
    comb = []
    for i in range(2 ** N):
        ary = []
        # print("i=", i)
        for j in range(N):
            # print("\tj=", j, " ... and i >> j =", i >> j, ": (i >> j) & 1 =>", (i >> j) & 1)
            if ((i >> j) & 1):
                ary.append(mat[j])
        comb.append(ary)
    return comb

mat = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]]

print(bit_brute_force(1, mat))
# [[], [[1, 1, 1]]]
print(bit_brute_force(2, mat))
# [[],
# [[1, 1, 1]],
# [[2, 2, 2]],
# [[1, 1, 1], [2, 2, 2]]]
# print(bit_brute_force(3, mat))
# [[],
# [[1, 1, 1]],
# [[2, 2, 2]],
# [[1, 1, 1], [2, 2, 2]],
# [[3, 3, 3]],
# [[1, 1, 1], [3, 3, 3]],
# [[2, 2, 2], [3, 3, 3]],
# [[1, 1, 1], [2, 2, 2], [3, 3, 3]]]

# ------------------------------------
# Bit Brute Force from N integer
# ------------------------------------
def bit_brute_force_patterns(N):
    combinations = []
    for i in range(2 ** N):
        ary = []
        for j in range(N):
            if ((i >> j) & 1):
                ary.append(j)
        combinations.append(ary)

    return combinations

# print(bit_brute_force_patterns(3))
# [[], [0], [1], [0, 1], [2], [0, 2], [1, 2], [0, 1, 2]]

# ------------------------------------
# Characters
# ------------------------------------
# help(string) # requires 'import string'
# ...
#     ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
#     ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     digits = '0123456789'
#     hexdigits = '0123456789abcdefABCDEF'
#     octdigits = '01234567'
#     punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#     whitespace = ' \t\n\r\x0b\x0c'
# print(string.ascii_letters)
# print(string.ascii_uppercase)

# Convert character and integer.
print(ord('A'))
print(ord('a'))
print(chr(65))
print(chr(66))

# ------------------------------------
# Dictionary (1)
#
# Add a new key if the dictionary doesn't have
# the same. If it exists as key, apply some operation.
# ------------------------------------
my_dict = { "apple" : 1, "orange" : 2, "grape" : 3 , "lemon" : 4 }

target = "apple"
if target in my_dict.keys():
    my_dict[target] += 100
else:
    my_dict[target] = 1
print(my_dict)
# {'apple': 101, 'orange': 2, 'grape': 3, 'lemon': 4}

# ------------------------------------
# Dictionary (2)
#
# Sort key-value pair according to values.
# Below code shows the ascending order output.
# ------------------------------------
for key, value in sorted(my_dict.items(), key = lambda x:x[1]):
    print("sorted=", key, value)
# sorted= orange 2
# sorted= grape 3
# sorted= lemon 4
# sorted= apple 101

# ------------------------------------
# Set operations
# ------------------------------------
a = { 1, 2, 3, 4, 5 }
b = { 3, 4, 5, 6, 7 }
print(a | b) # { 1, 2, 3, 4, 5, 6, 7 }
print(a & b) # { 3, 4, 5 }
print(a - b) # { 1, 2 }
print(b - a) # { 6, 7 }

# ------------------------------------
# Dictionary (2)
#
# Make a dictionary whose values have each isolated
# different data structure. Below example shows set().
#
# Note : Using zip() to gererate dictionary requires
# two lists like below.
#
# keys = ['a', 'b', 'c' ]
# values = [ 1, 2, 3 ]
# d = { k : v for k, v in zip(keys, values) }
#
# {'a': 1, 'b': 2, 'c': 3}
# ------------------------------------
keys_list = list(string.ascii_lowercase)
char_dicts = { k : v for k, v
               in zip(keys_list, [ set() for _ in keys_list ]) }
char_dicts['a'].add(1)
char_dicts['b'].add(2)
char_dicts['c'].add(3)
char_dicts['c'].add(4)
char_dicts['c'].add(5)
print(char_dicts)

# ------------------------------------
# Print dictionary values in ascending
# keys order.
#
# Besides, recognize the difference
# between list.sort() and
# new_list = sorted(list).
# ------------------------------------
keys = [5, 4, 3, 1, 2, 6]
values = ["a", "b", "c", "d", "e", "f"]
my_dict = { k : v for k, v
            in zip(keys, values) }

keys = list(my_dict.keys())
keys.sort()

# This 'keys' variable can be replaced
# with sorted(my_dict.keys()).
for k in keys:
    print(k, my_dict[k])
# 1 d
# 2 e
# 3 c
# 4 b
# 5 a
# 6 f

# ------------------------------------
# print() without a new line (line break)
# ------------------------------------
print("No line break", end="")
print("")

# ------------------------------------
# deque
# ------------------------------------
d = deque([1, 2, 3]) # requires 'from collections import deque'
d.append(4) # append an element at the end
d.appendleft(0) # append an element at the front
print(d)
# deque([0, 1, 2, 3, 4])
print(d.pop()) # pop from the end
# 4
print(d.popleft()) # pop from the front
# 0

# ------------------------------------
# Counter
#
# Count each elements and generate
# dictionary.
# ------------------------------------
counts = Counter(list("aaabbcdddde")) # requires 'from collections import Counter'
print("char counts =", counts)
# char counts = Counter({'d': 4, 'a': 3, 'b': 2, 'c': 1, 'e': 1})

# ------------------------------------
# numpy
# ------------------------------------
npmat = numpy.array(range(24)).reshape(4, 6) # requires 'import numpy'
print(npmat)
# array([[ 0,  1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10, 11],
#        [12, 13, 14, 15, 16, 17],
#        [18, 19, 20, 21, 22, 23]])
print(npmat.ndim) # 2
print(npmat.shape[0]) # 4
print(npmat.shape[1]) # 6
print(npmat.T)
# array([[ 0,  6, 12, 18],
#        [ 1,  7, 13, 19],
#        [ 2,  8, 14, 20],
#        [ 3,  9, 15, 21],
#        [ 4, 10, 16, 22],
#        [ 5, 11, 17, 23]])


# ------------------------------------
# Another way to extract columns
# ------------------------------------
columns = list(zip(*mat))
print("columns=", columns)
# columns= [(1, 2, 3, 4, 5), (1, 2, 3, 4, 5), (1, 2, 3, 4, 5)]

# ------------------------------------
# Regular Expression
#
# Get the matched indexes to retrieve.
# Note that the m.end(0) is the next
# index of the last character captured
# by the regular expression.
# ------------------------------------
S = "This is a test. foo and bar."
for m in re.finditer(r"(foo)|(bar)", S): # requires 'import re'
    print("Index=", m.start(0), "&", m.end(0),
          ", Sub string : ", S[ m.start(0) : m.end(0) ])


# ------------------------------------
# BFS function.
#
# Return the maximum cost from the start cell.
# ------------------------------------
def BFS(area, max_h, max_w, start_h, start_w, four_directions):

    cur_max_c = 0

    d = deque([(start_h, start_w, 0)])

    visited = [ [False] * max_w for _ in range(max_h) ]
    visited[start_h][start_w] = True

    movable_cell = '.'

    if four_direction:
        moves = [          [-1, 0],
                  [0, -1],          [0, 1],
                           [ 1, 0]]
    else:
        moves = [[-1, -1], [-1, 0], [-1, 1],
                 [ 0, -1],          [ 0, 1],
                 [ 1, -1], [ 1, 0], [ 1, 1]]

    while len(d) > 0:
        cur_h, cur_w, cur_c = d.popleft()
        if cur_max_c < cur_c:
            cur_max_c = cur_c

        for m in moves:
            moved_w = cur_w + m[1]
            moved_h = cur_h + m[0]
            if (0 <= moved_w <= max_w - 1) and (0 <= moved_h <= max_h - 1) \
               and (area[moved_h][moved_w] == movable_cell) \
               and (visited[moved_h][moved_w] is False):
                visited[moved_h][moved_w] = True
                d.append((moved_h, moved_w, cur_c + 1))

    return cur_max_c


# ------------------------------------
# * DO NOT ADD ANY NOTES AFTER THE SHELL START *
#
# Initialize and launch an interactive
# shell with vars defined here.
# ------------------------------------
import code

print("===<Variable Examples>===")
print("string : 'S'")
print("array : 'ary', 'new_ary'")
print("matrix : 'mat'")
print("dictionary : 'my_dict'")
print("SortedList : 'sorted_list'")
vars = globals().copy()
shell = code.InteractiveConsole(vars)
shell.interact(banner = "Interactive console started (type 'quit()' to exit) : ")
