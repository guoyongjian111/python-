def longestCommonPrefix(strs):
    n = len(strs)
    min_len = 0
    b = 0
    a = []
    for i in range(len(strs)):
        a.append(len(strs[i]))
    min_len = min(a)
    for i in range(min_len):
        set1 = set()
        for j in range(n):
            c = strs[j][i]
            set1.add(c)
        if len(set1) == 1:
            b += 1
        else:
            break
    if b == 0:
        return ""
    else:
        return strs[0][0:b]


print(longestCommonPrefix(["flower", "flow", "flight"]))
