# Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.
#
# Example
#
# For
#
# t = {
#     "value": 1,
#     "left": {
#         "value": 2,
#         "left": {
#             "value": 3,
#             "left": null,
#             "right": null
#         },
#         "right": {
#             "value": 4,
#             "left": null,
#             "right": null
#         }
#     },
#     "right": {
#         "value": 2,
#         "left": {
#             "value": 4,
#             "left": null,
#             "right": null
#         },
#         "right": {
#             "value": 3,
#             "left": null,
#             "right": null
#         }
#     }
# }
# the output should be isTreeSymmetric(t) = true.
#
# Here's what the tree in this example looks like:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# As you can see, it is symmetric.
#
# For
#
# t = {
#     "value": 1,
#     "left": {
#         "value": 2,
#         "left": null,
#         "right": {
#             "value": 3,
#             "left": null,
#             "right": null
#         }
#     },
#     "right": {
#         "value": 2,
#         "left": null,
#         "right": {
#             "value": 3,
#             "left": null,
#             "right": null
#         }
#     }
# }
# the output should be isTreeSymmetric(t) = false.
#
# Here's what the tree in this example looks like:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
# As you can see, it is not symmetric.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] tree.integer t
#
# A binary tree of integers.
#
# Guaranteed constraints:
# 0 ≤ tree size < 5 · 104,
# -1000 ≤ node value ≤ 1000.
#
# [output] boolean
#
# Return true if t is symmetric and false otherwise.


def isSymmetric(L, R):
    if len(L) != len(R):
        return False
    for key in L.keys():
        converted = ''
        for w in key:
            converted += 'l' if w == 'r' else 'r'
        if L[key] != R[converted]:
            return False
    return True


def isTreeSymmetric(t):
    if t == None or (t.right == None and t.left == None):
        return True

    l_dict = {}
    r_dict = {}

    def getValue(t, key, main_key=''):
        if t == None:
            return
        main_key += key
        if key == 'l':
            l_dict[main_key] = t.value
        else:
            r_dict[main_key] = t.value
        getValue(t.left, 'l', main_key)
        getValue(t.right, 'r', main_key)

    getValue(t.left, 'l')
    getValue(t.right, 'r')

    return isSymmetric(l_dict, r_dict)
