def calc(beauties, capitals):
    ret = 0
    sum_of_beauties = sum(beauties)
    for capital in capitals:
        sum_of_beauties -= beauties[capital]
        ret += beauties[capital]*sum_of_beauties
    for i in range(len(beauties)):
        j = (i + 1)%len(beauties)
        if i not in capitals and j not in capitals:
            ret += beauties[i]*beauties[j]
    return ret


def main():
    n, k = map(int, raw_input().split())
    beauties = map(int, raw_input().split())
    capitals = set(map(lambda x: int(x)-1, raw_input().split()))
    print calc(beauties, capitals)


if __name__ == '__main__':
    main()
