#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""
from datetime import datetime
from functools import wraps


def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f'Success. {end-start} taken for {func.__name__}')
        return result
    return wrapper


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        self.wl = list({beginWord, *wordList})
        try:
            e = self.wl.index(endWord)
        except ValueError:
            return []
        # s = self.wl.index(beginWord)

        self.ws = set(self.wl)
        self.ws.discard(beginWord)
        self.chars = [set(c) for c in zip(*self.wl)]

        self.prev = self.bfs_prev_word(beginWord, endWord)
        return self.trackback_word(beginWord, endWord)

        # self.mat = self.build_adjacent_list(self.wl)
        # self.prev = self.bfs_prev(s, e)
        # return self.trackback(s, e)
        # self.ret = []
        # self.visited = set()
        # self.min_length = self.bfs(s, e)
        # self.dfs(s, e, [])
        # return self.ret

    def gen_adjacent_words(self, word):
        for i in range(len(word)):
            for c in self.chars[i]:
                ret = word[:i] + c + word[i+1:]
                if ret in self.ws:
                    yield ret

    @timed
    def bfs_prev_word(self, s, e):
        from collections import deque, defaultdict
        depth = dict()
        prev = defaultdict(set)
        queue = deque([(s, 1)])
        visited = set()
        mindepth = float('inf')
        while queue:
            i, d = queue.popleft()
            if d >= mindepth: break
            for j in self.gen_adjacent_words(i):
                if j not in visited:
                    if j == e:
                        mindepth = d+1
                    visited.add(j)
                    queue.append((j, d+1))
                    depth[j] = d+1
                if d+1 <= depth[j]:
                    prev[j].add(i)
        return prev

    def trackback_word(self, s, e):
        if s == e:
            return [[s]]
        return [x + [e] for i in self.prev[e] for x in self.trackback_word(s, i)]

    @timed
    def build_adjacent_mat(self, lst):
        mat = [[False] * len(lst) for _ in lst]
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if sum(0 if a == b else 1 for a, b in zip(lst[i], lst[j])) == 1:
                    mat[i][j] = True
                    mat[j][i] = True
        return mat

    @timed
    def build_adjacent_list(self, lst):
        mat = [[] for _ in lst]
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if sum(0 if a == b else 1 for a, b in zip(lst[i], lst[j])) == 1:
                    mat[i].append(j)
                    mat[j].append(i)
        return mat

    @timed
    def bfs_prev(self, s, e):
        from collections import deque, defaultdict
        depth = dict()
        prev = defaultdict(set)
        queue = deque([(s, 1)])
        visited = set()
        mindepth = float('inf')
        while queue:
            i, d = queue.popleft()
            if d >= mindepth: break
            for j in self.mat[i]:
                if j not in visited:
                    if j == e:
                        mindepth = d+1
                    visited.add(j)
                    queue.append((j, d+1))
                    depth[j] = d+1
                if d+1 <= depth[j]:
                    prev[j].add(i)
        return prev

    def trackback(self, s, e):
        if s == e:
            return [[self.wl[s]]]
        return [x + [self.wl[e]] for i in self.prev[e] for x in self.trackback(s, i)]

    def dfs(self, s, e, p):
        p = p + [self.wl[s]]
        if len(p) > self.min_length:
            print(p)
            return
        if s == e:
            if len(p) < self.min_length:
                self.min_length = len(p)
                self.ret = []
            self.ret.append(p)
        self.visited.add(s)
        for i in self.mat[s]:
            if i not in self.visited:
                self.dfs(i, e, p)
        self.visited.remove(s)

    def bfs(self, s, e):
        from collections import deque
        queue = deque([(s, 1)])
        visited = set()
        while queue:
            i, d = queue.popleft()
            for j in self.mat[i]:
                if j not in visited:
                    if j == e:
                        return d+1
                    visited.add(j)
                    queue.append((j, d+1))
        return -1


def main():
    beginWord = input()
    endWord = input()
    wordList = input().split()

    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot","dot","dog","lot","log","cog"]

    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot","dot","dog","lot","log"]

    # beginWord = "hot"
    # endWord = "dog"
    # wordList = ["hot","dog","dot"]

    # beginWord = "qa"
    # endWord = "sq"
    # wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

    # beginWord = "cet"
    # endWord = "ism"
    # wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]

    print(len(wordList))
    print(Solution().findLadders(beginWord, endWord, wordList))


if __name__ == '__main__':
    main()
