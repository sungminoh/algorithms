#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter()

# User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5)

# User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1)

# User 1 follows user 2.
twitter.follow(1, 2)

# User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6)

# User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1)

# User 1 unfollows user 2.
twitter.unfollow(1, 2)

# User 1's news feed should return a list with 1 tweet id -> [5],
# since user 1 is no longer following user 2.
twitter.getNewsFeed(1)
"""

import pytest
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cnt = 0
        self.follow_map = defaultdict(set)
        self.posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.cnt += 1
        self.posts[userId].append((self.cnt, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        users = {userId, *self.follow_map[userId]}
        return self.merge([self.posts[user] for user in users if len(self.posts[user]) > 0], 10)

    def merge(self, posts: List[List], n: int) -> List[int]:
        index_posts = list(map(list, zip([-1] * len(posts), posts)))
        ret = []
        while len(ret) < 10 and index_posts:
            latest_cnt = -1
            latest_i = None
            latest_tweet = None
            empty_posts = []
            for i, (idx, pst)in enumerate(index_posts):
                if len(pst) + idx >= 0:
                    if latest_cnt < pst[idx][0]:
                        latest_cnt, latest_tweet = pst[idx]
                        latest_i = i
                else:
                    empty_posts.append(i)
            if latest_i is None:
                break
            index_posts[latest_i][0] -= 1
            ret.append(latest_tweet)
            for j in empty_posts:
                index_posts.pop(j)
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)


@pytest.mark.parametrize('commands, args, expected', [
    (["Twitter","postTweet","follow","postTweet", "getNewsFeed", "unfollow", "getNewsFeed"],
     [[],[1,5],[1,2],[2, 6], [1], [1, 2], [1]],
     [None, None, None, None, [6, 5], None, [5]]),
    (["Twitter","postTweet","unfollow","getNewsFeed"],
     [[],[1,5],[1,1],[1]],
     [None, None, None, [5]]),
    (["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed"],
     [[],[1,5],[1,3],[1,101],[1,13],[1,10],[1,2],[1,94],[1,505],[1,333],[1,22],[1,11],[1]],
     [None,None,None,None,None,None,None,None,None,None,None,None,[11,22,333,505,94,2,10,13,101,3]])
])
def test(commands, args, expected):
    print()
    twitter = Twitter()
    ret = [None]
    for cmd, arg in zip(commands[1:], args[1:]):
        ret.append(getattr(twitter, cmd)(*arg))
        print(ret[-1])
    assert expected == ret
