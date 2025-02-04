import collections
from typing import List, Dict, Set


class Twitter:

    def __init__(self):
        # 表示每个人发布的推特，使用栈的形式来存储 tuple: (tId, twitterId)
        self._twitter_dic: Dict[int, List[tuple]] = collections.defaultdict(lambda: [])
        # 表示的事每个人关注的人，这里使用 set 来存储
        self._followings: Dict[int, Set[int]] = collections.defaultdict(lambda: set())
        # 表示 twitter 发布的时间,开始是 0 越大表示发布的时间越晚
        self._t_id = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 将发布的 twitter 增加到对应的人的下面
        self._twitter_dic[userId].append((self._t_id, tweetId))
        self._t_id += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        主要的时间复杂度来自这里
        这里其实也可以使用观察者模式的方法来实现，每次发布就去通知，类似消息的订阅和发布
        :param userId:
        """
        # 这里按道理会使用多路归并的思想，但是我这里为了方便就没有使用了
        # 使用多路归并的方法的实现的时间复杂度是 O(10 * following_len)

        # 按照道理上来讲，多路归并和使用观察者模式的设计思路的视线的时间复杂度是一个级别的，只是理解的方法有一点不一样
        possible_twitters: List[tuple] = self._twitter_dic[userId].copy()
        for followee in self._followings[userId]:
            possible_twitters.extend(self._twitter_dic[followee])
        possible_twitters.sort(key=lambda t: t[0], reverse=True)

        return [item[1] for item in possible_twitters[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self._followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._followings[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
