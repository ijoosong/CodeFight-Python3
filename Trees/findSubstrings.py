# You have two arrays of strings, words and parts. Return an array that contains the strings from words, modified
# so that any occurrences of the substrings from parts are surrounded by square brackets [], following these guidelines:
#
# If several parts substrings occur in one string in words, choose the longest one. If there is still
# more than one such part, then choose the one that appears first in the string.
#
# Example
#
# For words = ["Apple", "Melon", "Orange", "Watermelon"] and parts = ["a", "mel", "lon", "el", "An"], the output should be
# findSubstrings(words, parts) = ["Apple", "Me[lon]", "Or[a]nge", "Water[mel]on"].
#
# While "Watermelon" contains three substrings from the parts array, "a", "mel", and "lon", "mel" is the longest substring
# that appears first in the string.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.string words
#
# An array of strings consisting only of uppercase and lowercase English letters.
#
# Guaranteed constraints:
# 0 ≤ words.length ≤ 104,
# 1 ≤ words[i].length ≤ 30.
#
# [input] array.string parts
#
# An array of strings consisting only of uppercase and lower English letters. Each string is no more than 5 characters in length.
#
# Guaranteed constraints:
# 0 ≤ parts.length ≤ 105,
# 1 ≤ parts[i].length ≤ 5,
# parts[i] ≠ parts[j].
#
# [output] array.string


def findSubstrings(words, parts):
    strings_of_length = dict()  # key = len(part), value = dict()

    def add_to_tree(t, val):
        if len(val) == 1:
            t[val] = False
        else:
            if val[0] not in t:
                t[val[0]] = dict()
            next_t = t[val[0]]
            add_to_tree(next_t, val[1:])

    for part in parts:
        l = len(part)
        if l not in strings_of_length:
            strings_of_length[l] = dict()

        add_to_tree(strings_of_length[l], part)

    def check(string, tree, top=True):
        if not string:
            return False
        if string[0] not in tree:
            return False
        temp = '[' if top else ''

        next_tree = tree[string[0]]
        if next_tree:
            next_check = check(string[1:], next_tree, False)
            if not next_check:
                return False
            temp += (string[0] + next_check)
        else:
            temp += (string[0] + ']' + string[1:])

        return temp

    for l in sorted(strings_of_length.keys(), reverse=True):
        for word_pos, word in enumerate(words):
            if '[' not in word:
                for letter_pos, letter in enumerate(word):
                    new_end = check(word[letter_pos:], strings_of_length[l])
                    if new_end:
                        words[word_pos] = word[:letter_pos] + new_end
                        break
    return words
