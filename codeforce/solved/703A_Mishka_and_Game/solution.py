def main():
    n = int(raw_input())
    wins = 0
    draw = 0
    lose = 0
    for i in xrange(n):
        m, c = map(int, raw_input().split())
        if m == c:
            draw += 1
        elif m > c:
            wins += 1
        else:
            lose += 1
    if wins > lose:
        print 'Mishka'
    elif wins < lose:
        print 'Chris'
    else:
        print 'Friendship is magic!^^'

if __name__ == '__main__':
    main()
