# You're given 2 huge integers represented by linked lists. Each linked list element is a number
# from 0 to 9999 that represents a number with exactly 4 digits.
# The represented number might have leading zeros.
# Your task is to add up these huge integers and return the result in the same format.
#
# Example
#
# For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
# addTwoHugeNumbers(a, b) = [9876, 5434, 0].
#
# Explanation: 987654321999 + 18001 = 987654340000.
#
# For a = [123, 4, 5] and b = [100, 100, 100], the output should be
# addTwoHugeNumbers(a, b) = [223, 104, 105].
#
# Explanation: 12300040005 + 10001000100 = 22301040105.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] linkedlist.integer a
#
# The first number, without its leading zeros.
#
# Guaranteed constraints:
# 0 ≤ a size ≤ 104,
# 0 ≤ element value ≤ 9999.
#
# [input] linkedlist.integer b
#
# The second number, without its leading zeros.
#
# Guaranteed constraints:
# 0 ≤ b size ≤ 104,
# 0 ≤ element value ≤ 9999.
#
# [output] linkedlist.integer
#
# The result of adding a and b together, returned without leading zeros in the same format.


# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None


def getArray(root):
  x = []
  current = root
  while current != None:
    x.append(current.value)
    current = current.next
  return x


def combineArray(A, B):
    C = []
    adding = 0
    while len(A) > 0 or len(B) > 0:
        if len(A) > 0 and len(B) > 0:
            sum = A.pop() + B.pop() + adding
        elif len(A) == 0:
            sum = B.pop() + adding
        else:
            sum = A.pop() + adding

        if sum > 9999:
            sum = sum - 10000
            adding = 1
        else:
            adding = 0
        C.append(sum)
    if adding > 0:
        C.append(adding)
    return C


def addTwoHugeNumbers(a, b):
    answer = combineArray(getArray(a), getArray(b))
    answer.reverse()
    return answer