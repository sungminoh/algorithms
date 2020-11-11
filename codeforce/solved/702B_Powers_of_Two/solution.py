def number_of_power_of_two_pairs(numbers):
    ret = 0
    dic = dict()
    for num in numbers:
        for i in range(32):
            ret += dic.get(2**i - num, 0)
        dic[num] = dic.get(num, 0) + 1
    return ret


def main():
    n = int(raw_input())
    numbers = map(int, raw_input().split())
    print number_of_power_of_two_pairs(numbers)


if __name__ == '__main__':
    main()
