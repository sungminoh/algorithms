import math


def is_integer(num):
    return num - int(num) == 0


def answer(a, b):
    same_at = math.log(float(b)/a, 1.5)
    if is_integer(same_at):
        return int(same_at + 1)
    else:
        return int(math.ceil(math.log(float(b)/a, 1.5)))


def get_inputs():
    return map(int, raw_input().split())


def main():
    a, b = get_inputs()
    print answer(a, b)


if __name__ == '__main__':
    main()
