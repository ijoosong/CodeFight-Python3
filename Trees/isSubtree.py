# Given two binary trees t1 and t2, determine whether the second tree is a subtree of the first tree.
# A subtree for vertex v in a binary tree t is a tree consisting of v and all its descendants in t.
# Determine whether or not there is a vertex v (possibly none) in tree t1 such that a subtree
# for vertex v (possibly empty) in t1 equals t2.
#
# Example
#
# For
#       t1:             t2:
#        5              10
#       / \            /  \
#     10   7          4    6
#    /  \            / \    \
#   4    6          1   2   -1
#  / \    \
# 1   2   -1
#
# the output should be isSubtree(t1, t2) = true.
# As you can see, t2 is a subtree of t1 (the vertex in t1 with value 10).
#
# For
#         t1:            t2:
#          5             10
#        /   \          /  \
#      10     7        4    6
#    /    \           / \    \
#   4     6          1   2   -1
#  / \   /
# 1   2 -1
#
# the output should be isSubtree(t1, t2) = false.
# As you can see, there is no vertex v such that the subtree of t1 for vertex v equals t2.
#
# For
#
# t1 = {
#     "value": 1,
#     "left": {
#         "value": 2,
#         "left": null,
#         "right": null
#     },
#     "right": {
#         "value": 2,
#         "left": null,
#         "right": null
#     }
# }
# and
#
# t2 = {
#     "value": 2,
#     "left": {
#         "value": 1,
#         "left": null,
#         "right": null
#     },
#     "right": null
# }
# the output should be isSubtree(t1, t2) = false.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] tree.integer t1
#
# A binary tree of integers.
#
# Guaranteed constraints:
# 0 ≤ tree size ≤ 6 · 104,
# -1000 ≤ node value ≤ 1000.
#
# [input] tree.integer t2
#
# Another binary tree of integers.
#
# Guaranteed constraints:
# 0 ≤ tree size ≤ 6 · 104,
# -1000 ≤ node value ≤ 1000.
#
# [output] boolean
#
# Return true if t2 is a subtree of t1, otherwise return false.


def findAndCheck(t1, t2):
    if t1 == None:
        return False
    if t1.value == t2.value:
        if checkThem(t1, t2):
            return True
    if t1.left != None:
        if findAndCheck(t1.left, t2):
            return True
    if t1.right != None:
        if findAndCheck(t1.right,t2):
            return True
    return False


def checkThem(t1, t2):
    if t1 == None and t2 == None:
        return True
    if t1 == None or t2 == None:
        return False
    if t1.value == t2.value:
        return checkThem(t1.left, t2.left) and checkThem(t1.right, t2.right)
    else:
        return False


def isSubtree(t1, t2):
    if t2 == None:
        return True
    return findAndCheck(t1, t2)