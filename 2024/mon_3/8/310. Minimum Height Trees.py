import collections
import sys
from typing import List, Dict, Set


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        :param n: 表示节点是 [0,n)
        :param edges: 表示的两两相连的边的节点
        :return: 返回可以形成一个最矮树的 root_list
        method1: 使用拓扑思想，重心思想，移除 degree 为 1 的点，直到最后的节点的数量不大于 2
        需要先构建邻接表，然后再逐渐移除

        T(n): O(n)
        S(n): O(n)
        """
        if n == 1:
            return [0]
        # 将 List 换成 Set 能够提升性能
        graph: Dict[int, List] = collections.defaultdict(lambda: [])
        degree: Dict[int, int] = collections.defaultdict(int)
        # 构造邻接表
        for item in edges:
            graph[item[0]].append(item[1])
            graph[item[1]].append(item[0])
            degree[item[0]] += 1
            degree[item[1]] += 1
        # 构建叶子 队列
        leaves_queue = collections.deque()
        for i in range(n):
            if degree[i] == 1:
                leaves_queue.append(i)
        remain_node_cou: int = n
        while remain_node_cou > 2:
            remain_node_cou -= len(leaves_queue)
            _now_len = len(leaves_queue)
            for _ in range(_now_len):
                _pop_leaf = leaves_queue.popleft()
                # 因为出队列的仅仅是叶子节点，因此度为 1 理论上，neighbor 也只有一个，但是需要我们自己删除 edge
                for neighbor in graph[_pop_leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves_queue.append(neighbor)
        return list(leaves_queue)


if __name__ == "__main__":
    # @formatter:off
    s = Solution()
    n = 2
    edges = []
    # @formatter:on
    print(s.findMinHeightTrees(n, edges))
