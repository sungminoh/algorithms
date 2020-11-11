def answer(cities):
    cities = sorted(cities)
    cnt = 0
    m = float('inf')
    for i in range(len(cities)-1):
        dist = cities[i+1] - cities[i]
        if dist < m:
            m = dist
            cnt = 1
        elif dist == m:
            cnt += 1
    return m, cnt


def get_inputs():
    return map(int, raw_input().split())


def main():
    get_inputs()
    cities = get_inputs()
    dist, cnt = answer(cities)
    print dist, cnt


if __name__ == '__main__':
    main()
