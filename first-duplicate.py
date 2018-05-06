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
    for i in range(len(a)):
        if a[i] in d.keys():
            ans = a[i]
            break
        else:
            d[a[i]] = i
    return ans