
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.

Initially, all the cards start face down (unrevealed) in one deck.

Now, you do the following steps repeatedly, until all cards are revealed:

	Take the top card of the deck, reveal it, and take it out of the deck.
	If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
	If there are still unrevealed cards, go back to step 1.  Otherwise, stop.

Return an ordering of the deck that would reveal the cards in increasing order.

The first entry in the answer is considered to be the top of the deck.

Example 1:

Input: [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation:
We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.

Note:
    1. 1 <= A.length <= 1000
    2. 1 <= A[i] <= 10^6
    3. A[i] != A[j] for all i != j
"""
import sys
from typing import List
import pytest


def zip_all(*lsts):
    lsts = {i: iter(l) for i, l in enumerate(lsts)}
    while lsts:
        exhausted = set()
        for i, l in lsts.items():
            try:
                yield next(l)
            except StopIteration:
                exhausted.add(i)
        for i in exhausted:
            lsts.pop(i)


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        def reveal(deck, reveal_first=True):
            if len(deck) > 1:
                if reveal_first:
                    i = (len(deck) + 1) // 2
                    sub1 = deck[:i]
                    sub2 = reveal(deck[i:], (len(deck)+1) % 2)
                    yield from zip_all(sub1, sub2)
                else:
                    i = len(deck) // 2
                    sub1 = deck[:i]
                    sub2 = reveal(deck[i:], len(deck) % 2)
                    yield from zip_all(sub2, sub1)
            elif len(deck) == 1:
                yield deck[0]
        return list(reveal(deck))


@pytest.mark.parametrize('deck, expected', [
    ([17,13,11,2,3,5,7], [2,13,3,11,5,17,7]),
])
def test(deck, expected):
    assert expected == Solution().deckRevealedIncreasing(deck)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
