def min_time(d, k, a, b, t):
    if d <= k:
        return a*d
    if b - a > t / k:
        x = (d//k)*k
        return min(t*((x-1)//k) + (a-b)*x + b*d,
                   t*((d-1)//k) + (a-b)*d + b*d)
    else:
        return (a-b)*k + b*d


def main():
    print min_time(*map(int, raw_input().split()))


if __name__ == '__main__':
    main()
