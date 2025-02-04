from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        T(n): O(n)
        S(n): O(n)
        双指针
        这道题不是贪心算法，仅仅是数学思维考察
        我们先计算出 每一个 i 对应的 surplus[i] = gas[i] - cost[i]
            - gas[i] 表示的是在这个节点能够得到的
            - cost[i] 表示到  i + 1 需要花费的
        随机选定一个相同的终点 start = end = 0 [start, end]
            - 使用 surplus_now 表示当前的盈余，也就是油量
            - 一开始的起点和终点相同，如果 surplus_now < 0 那么想起按找，并且执行 surplus_now += surplus[--start]直到 surplus >= 0
            - 如果找到终点的前一个都不能 > 0, 那么直接 return -1 因为如果有着一个起点满足题目要求，必然能够往前找到 start 满足 surplus_now >= 0
            - 找到之后 surplus_now += surplus[++end] 如果发现 (end + 1) % len == start，则 return start
        :param gas:
        :param cost:
        :return:

        优化：surplus仅仅是为了方便理解，可以去掉 此时 S(n): O(1)
        """
        surplus: List[int] = [gas[i] - cost[i] for i in range(len(gas))]
        # 随便选一个点即可
        start = end = 0  # [start, end]
        surplus_now = surplus[0]
        while True:
            while surplus_now < 0:
                start = (start - 1) % len(gas)
                surplus_now += surplus[start]
                if start == end:
                    return -1
            end = (end + 1) % len(gas)
            surplus_now += surplus[end]
            if surplus_now >= 0 and (end + 1) % len(gas) == start:
                return start


if __name__ == "__main__":
    gas = [3, 1, 1]
    cost = [1, 2, 2]

    print(Solution().canCompleteCircuit(gas, cost))
