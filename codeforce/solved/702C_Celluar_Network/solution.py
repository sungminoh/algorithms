def find_nearest(city, towers):
    i = 0
    j = len(towers)-1
    ret = abs(city - towers[i])
    while i < j:
        if i == j-1:
            ret = min(abs(towers[i] - city), abs(city - towers[j]))
            break
        p = (j+i) // 2
        if towers[p] > city:
            j = p
        elif towers[p] < city:
            i = p
        else:
            return 0
    return ret


def mininum_r(cities, towers):
    maximum = 0
    for city in cities:
        dist = find_nearest(city, towers)
        if dist > maximum:
            maximum = dist
    return maximum


def main():
    n, m = map(int, raw_input().split())
    cities = map(int, raw_input().split())
    towers = map(int, raw_input().split())
    print mininum_r(cities, towers)


if __name__ == '__main__':
    main()
