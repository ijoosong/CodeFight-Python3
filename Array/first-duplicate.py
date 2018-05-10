# Note: Write a solution with O(n) time complexity and O(1) additional space complexity,
# since this is what you would be asked to do during a real interview.
#
# Given an array a that contains only numbers in the range from 1 to a.length,
# find the first duplicate number for which the second occurrence has the minimal index.
# In other words, if there are more than 1 duplicated numbers, return the number for which
# the second occurrence has a smaller index than the second occurrence of the other number does.
# If there are no such elements, return -1.
#
# Example
#
# For a = [2, 3, 3, 1, 5, 2], the output should be
# firstDuplicate(a) = 3.
#
# There are 2 duplicates: numbers 2 and 3.
# The second occurrence of 3 has a smaller index than than second occurrence of 2 does,
# so the answer is 3.

def firstDuplicate2(a):
    answer = -1
    while len(a) > 1:
        for j in range(1, len(a)):
            if a[0] == a[j]:
                answer = a[0]
                a = a[1:j+1]
                break
        else:
            a = a[1:]
    return answer

def firstDuplicate(a):
    d = {}
    ans = -1
    for num in a:
        if num in d:
            ans = num
            break
        else:
            d[num] = 1
    return ans

print(firstDuplicate([2, 3, 4, 3, 5, 2]))
    
