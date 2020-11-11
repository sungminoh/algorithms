import math

base = ['  *  ', ' * * ', '*****']

n = input()


def get_k(n):
    return int(math.log(n/3., 2))


def concat1(a, b):
    return [x[0]+' '+x[1] for x in zip(a, b)]


def concat2(a, b):
    return [x[0]+x[1] for x in zip(a, b)]


def nth(i):
    if i == 0:
        return base
    else:
        child = nth(i-1)
        space = ['   '*(2**(i-1)) for x in range(len(child))]
        return concat2(space, concat2(child, space)) + concat1(child, child)


print '\n'.join(nth(get_k(n)))