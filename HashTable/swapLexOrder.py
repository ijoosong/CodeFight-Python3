# Given a string str and array of pairs that indicates which indices in the string can be swapped, return
# the lexicographically largest string that results from doing the allowed swaps. You can swap indices any number of times.
#
# Example
#
# For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
# swapLexOrder(str, pairs) = "dbca".
#
# By swapping the given indices, you get the strings: "cbda", "cbad", "dbac", "dbca".
# The lexicographically largest string in this list is "dbca".
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] string str
#
# A string consisting only of lowercase English letters.
#
# Guaranteed constraints:
# 1 ≤ str.length ≤ 104.
#
# [input] array.array.integer pairs
#
# An array containing pairs of indices that can be swapped in str (1-based). This means that for each pairs[i],
# you can swap elements in str that have the indices pairs[i][0] and pairs[i][1].
#
# Guaranteed constraints:
# 0 ≤ pairs.length ≤ 5000,
# pairs[i].length = 2.
#
# [output] string


#  Answer 1
def swapLexOrder(str, pairs):
    length = len(str)
    pairs = [[i-1 for i in p] for p in pairs]
    linked = [set([x]) for x in range(length)]
    for x, y in pairs:
        linked[x].add(y)
        linked[y].add(x)

    def make_group(index):
        for x in linked[index]:
            if x not in group:
                group.add(x)
                make_group(x)

    groups = set()
    for Set in linked:
        if len(Set) > 1:
            group = set()
            for x in Set:
                make_group(x)
            groups.add(tuple(sorted(group)))

    word = [char for char in str]
    for group in groups:
        L = sorted(group)
        chars = [str[l] for l in L]
        chars.sort()
        for x in L:
            word[x] = chars.pop()
    return ''.join(word)


#  Answer 2
# def swapLexOrder(str, pairs):
#     swap_lists = []
#     pairs = [[p[0]-1,p[1]-1] for p in pairs]
#     for i in range(len(pairs)):
#         for L in swap_lists:
#             if pairs[i][0] in L or pairs[i][1] in L:
#                 break
#         else:
#             swap_lists.extend([set([pairs[i][0], pairs[i][1]])])
#             k = 0
#             while k < len(swap_lists[-1]):
#                 for j in range(k+1, len(pairs)):
#                     if pairs[j][0] in swap_lists[-1]:
#                         swap_lists[-1].add(pairs[j][1])
#                     elif pairs[j][1] in swap_lists[-1]:
#                         swap_lists[-1].add(pairs[j][0])
#                 k += 1

#     word = [char for char in str]
#     for Set in swap_lists:
#         L = sorted(Set)
#         chars = [str[l] for l in L]
#         chars.sort()
#         for x in L:
#             word[x] = chars.pop()
#     return ''.join(word)
