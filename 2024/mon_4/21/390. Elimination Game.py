class Solution:
    def lastRemaining(self, n: int) -> int:
        """
        method1: 最直接、最简单的方法就是构造一个 LinkedList， 然后删除节点知道只剩下一个节点
            T(n): O(n)
            S(n): O(n)
        method2: 使用二分思想
            T(n): O(log(n))
            S(n): O(1)
        下面的算法是使用 method2 实现的
        """
        # [start, stop]
        # gap
        start = 1
        stop = n
        gap = 1
        now_num_cou: int = (stop + gap - start) // gap
        left2right: bool = True
        while stop > start:
            # 表示是偶数个数字
            if now_num_cou % 2 == 0:
                # 表示现在从 左开始往右
                if left2right:
                    start = start + gap
                    stop = stop
                    gap *= 2
                # 表示现在从 右开始往左
                else:
                    start = start
                    stop = stop - gap
                    gap *= 2
            # 表示是奇数个数字，从左往右和从右往左都是一样的
            else:
                start = start + gap
                stop = stop - gap
                gap *= 2
            left2right = not left2right
            now_num_cou = (stop + gap - start) // gap
        return start


if __name__ == "__main__":
    s = Solution()
    print(s.lastRemaining(6))
