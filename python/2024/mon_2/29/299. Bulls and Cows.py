import collections
from typing import List, Set, Dict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        Input: secret = "1807"
               guess = "7810"

        Output: "1A3B"
        T(n): O(N)
        S(n): O(N - bull_cou)
        bull: same
        cow : which can be true by change it's plate


        实现思路:
                1. 首先遍历找到相同的，并且标记，得到的就是 bull_cou
                2. 遍历的过程中，不相同的部分，分别加入不同的集合中
                3. 判定不同的有多少个重合的得到的就是 cow_cou
        """
        cow_secret_set: Dict[str, int] = collections.defaultdict(lambda: 0)
        cow_guess_list: List[str] = []
        bull_cou = 0
        # 计算出相同的 bull_cou
        # 同时将不同的分别加入到集合中
        for i in range(len(secret)):
            if secret[i] != guess[i]:
                cow_secret_set[secret[i]] += 1
                cow_guess_list.append(guess[i])
            else:
                bull_cou += 1
        # 通过上面的集合判断合一 rearrange 得到正确位置的数量即为 cow_cou
        cow_cou = 0
        for item in cow_guess_list:
            if item in cow_secret_set and cow_secret_set[item] > 0:
                cow_secret_set[item] -= 1
                cow_cou += 1
        return f'{bull_cou}A{cow_cou}B'


if __name__ == "__main__":
    s = Solution()
    secret = "1122"
    guess = "2211"
    print(s.getHint(secret, guess))
