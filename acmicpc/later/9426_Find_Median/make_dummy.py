from random import randint
import sys


if len(sys.argv) < 2:
    n = randint(1, 250000)
else:
    n = int(sys.argv[1])

if len(sys.argv) < 3:
    k = randint(1, min(5000, n))
else:
    k = int(sys.argv[2])

if len(sys.argv) < 4:
    m = 65536
else:
    m = int(sys.argv[3])


with open('./dummy.txt', 'w') as f:
    f.write('%d %d\n' % (n, k))
    for i in range(0, n):
        # f.write("%d\n" % randint(0, m))
        f.write("%d\n" % (i % m))
