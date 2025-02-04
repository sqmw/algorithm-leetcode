import collections
from typing import List


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        method1(使用字典):
            T(n): O(n)
            S(n): O(distinct char_in_s)
        method2(没有显式使用字典，但是使用了字典的性质):
            因为每个字母都是映射一个对应的 ASCII 码，并且是递增的，因此就可以使用一个长度为 26
            的 list 来存储，这个时候就可以直接映射了，数组存储的值就是对应的出现的次数
            T(n): O(n)
            S(n): O(distinct char_in_s)
        method3: 使用队列来实现，因为是第一个，符合队列额特点，维护一个 set 如果队列的前面出现了多次出现的
            就出队列，否则进入队列，这样就可以得到最终的结果
            官方的所谓的使用队列来实现，实际上和上面的这种是一样的

        """
        # char  ABCDEFG ...
        # index 0123456 ...
        # a: 97
        arr_as_set: List[int] = [0] * 26
        _queue: collections.deque = collections.deque()
        for i, char in enumerate(s):
            # 表示仅仅目前才出现过
            if arr_as_set[ord(char) - ord('a')] == 0:
                # char, i
                arr_as_set[ord(char) - ord('a')] += 1
                _queue.append((char, i))
            # 表示之前已经出现了一次
            else:
                arr_as_set[ord(char) - ord('a')] += 1
                while len(_queue) > 0 and arr_as_set[ord(_queue[0][0]) - ord('a')] > 1:
                    _queue.popleft()
        return _queue[0][1] if len(_queue) > 0 else -1


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar('loveleo'))
