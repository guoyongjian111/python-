def is_palindrome(x: int) -> bool:
    if x >= 0:
        a = str(x)
        n = len(a)
        d = 0
        for i in range(int(n / 2)):
            b = a[i]
            c = a[-i - 1]
            if b == c:
                d += 1
        if d == int(n / 2):
            return True
        else:
            return False
    else:
        return False


print((is_palindrome(1001)))
