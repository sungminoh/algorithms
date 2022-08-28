#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

	Every adjacent pair of words differs by a single letter.
	Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
	sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:

	1 <= beginWord.length <= 5
	endWord.length == beginWord.length
	1 <= wordList.length <= 500
	wordList[i].length == beginWord.length
	beginWord, endWord, and wordList[i] consist of lowercase English letters.
	beginWord != endWord
	All the words in wordList are unique.
	The sum of all shortest transformation sequences does not exceed 105.
"""
import sys
import itertools
from collections import deque
from collections import defaultdict
from typing import Dict
from typing import List
import pytest


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """08/18/2018 00:24"""
        wl = list({beginWord, *wordList})
        try:
            e = wl.index(endWord)
        except ValueError:
            return []
        # s = self.wl.index(beginWord)

        ws = set(wl)
        ws.discard(beginWord)
        chars = [set(c) for c in zip(*wl)]

        def gen_adjacent_words(word):
            for i in range(len(word)):
                for c in chars[i]:
                    ret = word[:i] + c + word[i+1:]
                    if ret in ws:
                        yield ret

        def bfs_prev_word(s, e):
            from collections import deque, defaultdict
            depth = dict()
            queue = deque([(s, 1)])
            parents = defaultdict(set)
            visited = set()
            mindepth = float('inf')
            while queue:
                i, d = queue.popleft()
                if d >= mindepth: break
                for j in gen_adjacent_words(i):
                    if j not in visited:
                        if j == e:
                            mindepth = d+1
                        visited.add(j)
                        queue.append((j, d+1))
                        depth[j] = d+1
                    if d+1 <= depth[j]:
                        parents[j].add(i)
            return parents

        parents = bfs_prev_word(beginWord, endWord)

        def trackback_word(s, e):
            if s == e:
                return [[s]]
            return [x + [e] for i in parents[e] for x in trackback_word(s, i)]

        return trackback_word(beginWord, endWord)

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """08/19/2021 19:56
        BFS
        Time complexity: O(n^2 * m) where m is the length of word or bfs tc
        Space complexity: O(n^n)
        """
        graph = defaultdict(list)
        wordList = list(set(wordList + [beginWord]))
        n = len(wordList)
        for i in range(n):
            for j in range(i+1, n):
                if len([1 for x, y in zip(wordList[i], wordList[j]) if x != y]) == 1:
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        visited = set()
        queue = deque([[beginWord]])
        ret = []
        while queue:
            track = queue.popleft()
            visited.add(track[-1])
            if ret and len(ret[0]) <= len(track):
                break
            for w in graph.get(track[-1], []):
                if w == endWord:
                    ret.append(track + [w])
                if w not in visited:
                    queue.append(track + [w])

        return ret

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """08/28/2022 13:43"""
        missing_to_original_word = defaultdict(set)
        for w in itertools.chain(wordList, [beginWord]):
            for i in range(len(w)):
                missing_to_original_word[(w[:i], w[i+1:])].add(w)

        graph = defaultdict(set)
        for w in itertools.chain(wordList, [beginWord]):
            for i in range(len(w)):
                graph[w].update(missing_to_original_word[(w[:i], w[i+1:])])
                graph[w].discard(w)

        def dfs(dct, start, end):
            if start == end:
                return [[start]]

            ret = []
            for nxt in dct.get(start, {}):
                for lst in dfs(dct, nxt, end):
                    ret.append(lst + [start])
            return ret

        def bfs(start, end) -> List[List[str]]:
            if start == end:
                return [[start]]
            queue = {start}
            parents = defaultdict(set)
            while queue:
                new_queue = set()
                parents_to_update = defaultdict(set)
                for cur in queue:
                    for nxt in graph[cur]:
                        if nxt not in parents:
                            parents_to_update[nxt].add(cur)
                            new_queue.add(nxt)
                # next step
                for c, ps in parents_to_update.items():
                    parents[c].update(ps)
                queue = new_queue
                # break condition
                if end in parents_to_update:
                    break
            return dfs(parents, end, start)

        return bfs(beginWord, endWord)


@pytest.mark.parametrize('beginWord, endWord, wordList, expected', [
    ("hit", "cog", ["hot","dot","dog","lot","log","cog"], [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]),
    ("hit", "cog", ["hot","dot","dog","lot","log"], []),
    ("aaaaa", "ggggg", ["aaaaa","caaaa","cbaaa","daaaa","dbaaa","eaaaa","ebaaa","faaaa","fbaaa","gaaaa","gbaaa","haaaa","hbaaa","iaaaa","ibaaa","jaaaa","jbaaa","kaaaa","kbaaa","laaaa","lbaaa","maaaa","mbaaa","naaaa","nbaaa","oaaaa","obaaa","paaaa","pbaaa","bbaaa","bbcaa","bbcba","bbdaa","bbdba","bbeaa","bbeba","bbfaa","bbfba","bbgaa","bbgba","bbhaa","bbhba","bbiaa","bbiba","bbjaa","bbjba","bbkaa","bbkba","bblaa","bblba","bbmaa","bbmba","bbnaa","bbnba","bboaa","bboba","bbpaa","bbpba","bbbba","abbba","acbba","dbbba","dcbba","ebbba","ecbba","fbbba","fcbba","gbbba","gcbba","hbbba","hcbba","ibbba","icbba","jbbba","jcbba","kbbba","kcbba","lbbba","lcbba","mbbba","mcbba","nbbba","ncbba","obbba","ocbba","pbbba","pcbba","ccbba","ccaba","ccaca","ccdba","ccdca","cceba","cceca","ccfba","ccfca","ccgba","ccgca","cchba","cchca","cciba","ccica","ccjba","ccjca","cckba","cckca","cclba","cclca","ccmba","ccmca","ccnba","ccnca","ccoba","ccoca","ccpba","ccpca","cccca","accca","adcca","bccca","bdcca","eccca","edcca","fccca","fdcca","gccca","gdcca","hccca","hdcca","iccca","idcca","jccca","jdcca","kccca","kdcca","lccca","ldcca","mccca","mdcca","nccca","ndcca","occca","odcca","pccca","pdcca","ddcca","ddaca","ddada","ddbca","ddbda","ddeca","ddeda","ddfca","ddfda","ddgca","ddgda","ddhca","ddhda","ddica","ddida","ddjca","ddjda","ddkca","ddkda","ddlca","ddlda","ddmca","ddmda","ddnca","ddnda","ddoca","ddoda","ddpca","ddpda","dddda","addda","aedda","bddda","bedda","cddda","cedda","fddda","fedda","gddda","gedda","hddda","hedda","iddda","iedda","jddda","jedda","kddda","kedda","lddda","ledda","mddda","medda","nddda","nedda","oddda","oedda","pddda","pedda","eedda","eeada","eeaea","eebda","eebea","eecda","eecea","eefda","eefea","eegda","eegea","eehda","eehea","eeida","eeiea","eejda","eejea","eekda","eekea","eelda","eelea","eemda","eemea","eenda","eenea","eeoda","eeoea","eepda","eepea","eeeea","ggggg","agggg","ahggg","bgggg","bhggg","cgggg","chggg","dgggg","dhggg","egggg","ehggg","fgggg","fhggg","igggg","ihggg","jgggg","jhggg","kgggg","khggg","lgggg","lhggg","mgggg","mhggg","ngggg","nhggg","ogggg","ohggg","pgggg","phggg","hhggg","hhagg","hhahg","hhbgg","hhbhg","hhcgg","hhchg","hhdgg","hhdhg","hhegg","hhehg","hhfgg","hhfhg","hhigg","hhihg","hhjgg","hhjhg","hhkgg","hhkhg","hhlgg","hhlhg","hhmgg","hhmhg","hhngg","hhnhg","hhogg","hhohg","hhpgg","hhphg","hhhhg","ahhhg","aihhg","bhhhg","bihhg","chhhg","cihhg","dhhhg","dihhg","ehhhg","eihhg","fhhhg","fihhg","ghhhg","gihhg","jhhhg","jihhg","khhhg","kihhg","lhhhg","lihhg","mhhhg","mihhg","nhhhg","nihhg","ohhhg","oihhg","phhhg","pihhg","iihhg","iiahg","iiaig","iibhg","iibig","iichg","iicig","iidhg","iidig","iiehg","iieig","iifhg","iifig","iighg","iigig","iijhg","iijig","iikhg","iikig","iilhg","iilig","iimhg","iimig","iinhg","iinig","iiohg","iioig","iiphg","iipig","iiiig","aiiig","ajiig","biiig","bjiig","ciiig","cjiig","diiig","djiig","eiiig","ejiig","fiiig","fjiig","giiig","gjiig","hiiig","hjiig","kiiig","kjiig","liiig","ljiig","miiig","mjiig","niiig","njiig","oiiig","ojiig","piiig","pjiig","jjiig","jjaig","jjajg","jjbig","jjbjg","jjcig","jjcjg","jjdig","jjdjg","jjeig","jjejg","jjfig","jjfjg","jjgig","jjgjg","jjhig","jjhjg","jjkig","jjkjg","jjlig","jjljg","jjmig","jjmjg","jjnig","jjnjg","jjoig","jjojg","jjpig","jjpjg","jjjjg","ajjjg","akjjg","bjjjg","bkjjg","cjjjg","ckjjg","djjjg","dkjjg","ejjjg","ekjjg","fjjjg","fkjjg","gjjjg","gkjjg","hjjjg","hkjjg","ijjjg","ikjjg","ljjjg","lkjjg","mjjjg","mkjjg","njjjg","nkjjg","ojjjg","okjjg","pjjjg","pkjjg","kkjjg","kkajg","kkakg","kkbjg","kkbkg","kkcjg","kkckg","kkdjg","kkdkg","kkejg","kkekg","kkfjg","kkfkg","kkgjg","kkgkg","kkhjg","kkhkg","kkijg","kkikg","kkljg","kklkg","kkmjg","kkmkg","kknjg","kknkg","kkojg","kkokg","kkpjg","kkpkg","kkkkg","ggggx","gggxx","ggxxx","gxxxx","xxxxx","xxxxy","xxxyy","xxyyy","xyyyy","yyyyy","yyyyw","yyyww","yywww","ywwww","wwwww","wwvww","wvvww","vvvww","vvvwz","avvwz","aavwz","aaawz","aaaaz"], [['aaaaa', 'aaaaz', 'aaawz', 'aavwz', 'avvwz', 'vvvwz', 'vvvww', 'wvvww', 'wwvww', 'wwwww', 'ywwww', 'yywww', 'yyyww', 'yyyyw', 'yyyyy', 'xyyyy', 'xxyyy', 'xxxyy', 'xxxxy', 'xxxxx', 'gxxxx', 'ggxxx', 'gggxx', 'ggggx', 'ggggg']]),
    ("a", "c", ["a","b","c"], [["a","c"]]),
    ("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"], [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]),
    ("hot", "dog", ["hot","dog","dot"], [['hot', 'dot', 'dog']]),
    ("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"], [['qa', 'ma', 'me', 'se', 'sq'], ['qa', 'na', 'ne', 'se', 'sq'], ['qa', 'ya', 'ye', 'se', 'sq'], ['qa', 'ha', 'he', 'se', 'sq'], ['qa', 'ga', 'ge', 'se', 'sq'], ['qa', 'ra', 're', 'se', 'sq'], ['qa', 'la', 'le', 'se', 'sq'], ['qa', 'fa', 'fe', 'se', 'sq'], ['qa', 'ba', 'be', 'se', 'sq'], ['qa', 'la', 'ln', 'sn', 'sq'], ['qa', 'ra', 'rn', 'sn', 'sq'], ['qa', 'ma', 'mn', 'sn', 'sq'], ['qa', 'la', 'lo', 'so', 'sq'], ['qa', 'ha', 'ho', 'so', 'sq'], ['qa', 'ma', 'mo', 'so', 'sq'], ['qa', 'ga', 'go', 'so', 'sq'], ['qa', 'ta', 'to', 'so', 'sq'], ['qa', 'ya', 'yo', 'so', 'sq'], ['qa', 'pa', 'po', 'so', 'sq'], ['qa', 'na', 'no', 'so', 'sq'], ['qa', 'ca', 'co', 'so', 'sq'], ['qa', 'pa', 'pt', 'st', 'sq'], ['qa', 'ma', 'mt', 'st', 'sq'], ['qa', 'la', 'lt', 'st', 'sq'], ['qa', 'la', 'lr', 'sr', 'sq'], ['qa', 'fa', 'fr', 'sr', 'sq'], ['qa', 'ma', 'mr', 'sr', 'sq'], ['qa', 'ca', 'cr', 'sr', 'sq'], ['qa', 'ba', 'br', 'sr', 'sq'], ['qa', 'na', 'nb', 'sb', 'sq'], ['qa', 'ya', 'yb', 'sb', 'sq'], ['qa', 'pa', 'pb', 'sb', 'sq'], ['qa', 'ma', 'mb', 'sb', 'sq'], ['qa', 'ta', 'tb', 'sb', 'sq'], ['qa', 'ra', 'rb', 'sb', 'sq'], ['qa', 'ta', 'tc', 'sc', 'sq'], ['qa', 'pa', 'pi', 'si', 'sq'], ['qa', 'na', 'ni', 'si', 'sq'], ['qa', 'ca', 'ci', 'si', 'sq'], ['qa', 'ta', 'ti', 'si', 'sq'], ['qa', 'ma', 'mi', 'si', 'sq'], ['qa', 'ha', 'hi', 'si', 'sq'], ['qa', 'la', 'li', 'si', 'sq'], ['qa', 'ba', 'bi', 'si', 'sq'], ['qa', 'ra', 'rh', 'sh', 'sq'], ['qa', 'pa', 'ph', 'sh', 'sq'], ['qa', 'ta', 'th', 'sh', 'sq'], ['qa', 'ta', 'tm', 'sm', 'sq'], ['qa', 'pa', 'pm', 'sm', 'sq'], ['qa', 'ca', 'cm', 'sm', 'sq'], ['qa', 'fa', 'fm', 'sm', 'sq']]),
    ("cet", "ism", ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"], [['cet', 'cot', 'con', 'ion', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'ism'], ['cet', 'cat', 'can', 'ian', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'ism'], ['cet', 'get', 'gee', 'gte', 'ate', 'ats', 'its', 'ito', 'ibo', 'ibm', 'ism']]),
])
def test(beginWord, endWord, wordList, expected):
    actual = Solution().findLadders(beginWord, endWord, wordList)
    assert sorted(expected) == sorted(actual)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
