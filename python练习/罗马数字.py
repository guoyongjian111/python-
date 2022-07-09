def romanToInt(self, s: str) -> int:
    map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    output = 0
    for i in range(len(s) - 1):
        if map[s[i]] >= map[s[i+1]]:
            output += map[s[i]]
        else:
            output -= map[s[i]]
    output += map[s[-1]]
    return output
