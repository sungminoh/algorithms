def is_hansoo(n):
    if n < 10:
        return True
    l = [(n / 10**x) % 10 for x in range(len(str(n)) - 1, -1, -1)]
    gap = l[0] - l[1]
    for i in range(1, len(l)-1):
        if gap != l[i] - l[i+1]:
            return False
    return True

print len(filter(is_hansoo, range(1, input()+1)))