def maximum_length_of_increasing_subarray(array):
    ret = 0
    cnt = 1
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            cnt += 1
        else:
            if cnt > ret:
                ret = cnt
            cnt = 1
    if cnt > ret:
        ret = cnt
    return ret


def main():
    n = int(raw_input())
    array = map(int, raw_input().split())
    print maximum_length_of_increasing_subarray(array)


if __name__ == '__main__':
    main()
