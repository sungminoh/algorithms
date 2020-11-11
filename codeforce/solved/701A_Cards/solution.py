def distribute(deck):
    s = sum(deck)//(len(deck)//2)
    idx_by_val = [[] for x in xrange(101)]
    for i, card in enumerate(deck):
        match_card = s - card
        if idx_by_val[match_card]:
            print '%s %s' % (i+1, idx_by_val[match_card].pop()+1)
        else:
            idx_by_val[card].append(i)


def main():
    int(raw_input().strip())
    deck = map(int, raw_input().strip().split())
    distribute(deck)


if __name__ == '__main__':
    main()
