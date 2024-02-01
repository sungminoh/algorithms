from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a food rating system that can do the following:

	Modify the rating of a food item listed in the system.
	Return the highest-rated food item for a type of cuisine in the system.

Implement the FoodRatings class:

	FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.

		foods[i] is the name of the ith food,
		cuisines[i] is the type of cuisine of the ith food, and
		ratings[i] is the initial rating of the ith food.

	void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
	String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

Example 1:

Input
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
Output
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

Explanation
FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
                                    // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
                                      // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // Both "sushi" and "ramen" have a rating of 16.
                                      // However, "ramen" is lexicographically smaller than "sushi".

Constraints:

	1 <= n <= 2 * 104
	n == foods.length == cuisines.length == ratings.length
	1 <= foods[i].length, cuisines[i].length <= 10
	foods[i], cuisines[i] consist of lowercase English letters.
	1 <= ratings[i] <= 108
	All the strings in foods are distinct.
	food will be the name of a food item in the system across all calls to changeRating.
	cuisine will be a type of cuisine of at least one food item in the system across all calls to highestRated.
	At most 2 * 104 calls in total will be made to changeRating and highestRated.
"""
import pytest
import sys
sys.path.append('../')
from exercise.tree import TreeNode


class BiTreeNode(TreeNode):
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def set_left(self, node):
        self.left = node
        if node:
            node.parent = self

    def set_right(self, node):
        self.right = node
        if node:
            node.parent = self


class KeyedTree:
    def __init__(self):
        self.d = {}
        self.root = None

    def insert(self, key, val):
        assert key not in self.d
        if self.root is None:
            self.d[key] = self.root = BiTreeNode(val)
        else:
            node = self.root
            while node:
                if val < node.val:
                    if node.left is None:
                        self.d[key] = BiTreeNode(val, parent=node)
                        node.left = self.d[key]
                        break
                    node = node.left
                else:
                    if node.right is None:
                        self.d[key] = BiTreeNode(val, parent=node)
                        node.right = self.d[key]
                        break
                    node = node.right

    @classmethod
    def _max_node(cls, node) -> BiTreeNode:
        while node and node.right:
            node = node.right
        return node

    def max(self):
        return self._max_node(self.root).val

    def delete(self, key):
        def connect_parent(node, child):
            if node.parent:
                if id(node.parent.left) == id(node):
                    node.parent.set_left(child)
                else:
                    node.parent.set_right(child)
            else:
                self.root = child
                if self.root:
                    self.root.parent = None

        node = self.d.pop(key)
        if not node.left:
            connect_parent(node, node.right)
        else:
            lm = self._max_node(node.left)
            if id(lm) != id(node.left):
                lm.parent.set_right(lm.left)
                lm.set_left(node.left)
            lm.set_right(node.right)
            connect_parent(node, lm)
            del node


def encode(s):
    return tuple(-ord(c) for c in s)


def decode(code):
    return ''.join(chr(-x) for x in code)


class FoodRatings:
    """Jan 29, 2024 01:22"""
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.trees = {}
        self.food_cuisines = {}
        for c, f, r in zip(cuisines, foods, ratings):
            self.trees.setdefault(c, KeyedTree()).insert(f, (r, encode(f)))
            self.food_cuisines[f] = c

    def changeRating(self, food: str, newRating: int) -> None:
        tree = self.trees[self.food_cuisines[food]]
        tree.delete(food)
        tree.insert(food, (newRating, encode(food)))

    def highestRated(self, cuisine: str) -> str:
        return decode(self.trees[cuisine].max()[1])


@pytest.mark.parametrize('args', [
    ((["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"],
      [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]],
      [None, "kimchi", "ramen", None, "sushi", None, "ramen"])),
    ((["FoodRatings","changeRating","highestRated","changeRating","changeRating","highestRated"],
      [[["czopaaeyl","lxoozsbh","kbaxapl"],["dmnuqeatj","dmnuqeatj","dmnuqeatj"],[11,2,15]],["czopaaeyl",12],["dmnuqeatj"],["kbaxapl",8],["lxoozsbh",5],["dmnuqeatj"]],
      [None,None,"kbaxapl",None,None,"czopaaeyl"])),
    ((["FoodRatings","highestRated","changeRating","changeRating","highestRated","changeRating","highestRated","changeRating","changeRating","changeRating","changeRating","changeRating","changeRating","changeRating","highestRated","changeRating","highestRated"],
      [[["xxdcg","wfqdeytt","jqmfm","ukqbjikyx","aymciznrnw","qhjjrvr","wzcinxg","ikxj"],["lruhtqy","lruhtqy","lruhtqy","lruhtqy","lruhtqy","lruhtqy","lruhtqy","lruhtqy"],[8,6,1,17,20,2,17,14]],["lruhtqy"],["wfqdeytt",17],["aymciznrnw",9],["lruhtqy"],["ukqbjikyx",10],["lruhtqy"],["xxdcg",11],["ikxj",15],["aymciznrnw",10],["wfqdeytt",10],["xxdcg",16],["ikxj",2],["aymciznrnw",16],["lruhtqy"],["wzcinxg",12],["lruhtqy"]],
      [None,"aymciznrnw",None,None,"ukqbjikyx",None,"wfqdeytt",None,None,None,None,None,None,None,"wzcinxg",None,"aymciznrnw"])),
    ((["FoodRatings","changeRating","changeRating"],
      [[["biihw"],["okxsrcqn"],[13]],["biihw",9],["biihw",6]],
      [None, None, None])),
])
def test(args):
    commands, arguments, expecteds = args
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    actual = []
    for cmd, arg in zip(commands, arguments):
        actual.append(getattr(obj, cmd)(*arg))
    assert expecteds[1:] == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
