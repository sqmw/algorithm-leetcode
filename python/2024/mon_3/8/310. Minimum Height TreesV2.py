import collections
import sys
from typing import List, Dict, Set, Optional


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        :param n: 表示节点是 [0,n)
        :param edges: 表示的两两相连的边的节点
        :return: 返回可以形成一个最矮树的 root_list
        method2: 通过找到树的直径，直径的中点就是需要找的 roots(同样也是method1的平衡思想、重心思想)
                 实现方法是广度优先遍历
        T(n): O(n)
        S(n): O(n)
        """
        if n == 1:
            return [0]
        # 将 List 换成 Set 能够提升性能
        graph: Dict[int, List] = collections.defaultdict(lambda: [])
        # 构造邻接表
        for item in edges:
            graph[item[0]].append(item[1])
            graph[item[1]].append(item[0])

        parent: List[int] = [0] * n

        # 通过广度优先遍历找到距离 _root 最远的端点(不唯一)
        def bfs_get_longest(_root: int) -> int:
            nonlocal parent
            visited_nodes: List[bool] = [False] * n
            _depth_node_info: List[tuple] = []
            _queue = collections.deque()
            _queue.append(_root)
            _depth: int = 1  # 表示的事当前的 _root
            while len(_queue) > 0:
                _len_before = len(_queue)
                # 将队列目前的所有节点出队列
                for _ in range(_len_before):
                    popped_node: int = _queue.popleft()
                    visited_nodes[popped_node] = True
                    if len(graph[popped_node]) == 1:
                        _depth_node_info.append((popped_node, _depth))
                    for child in graph[popped_node]:
                        # 表示没有访问过
                        if visited_nodes[child] is False:
                            parent[child] = popped_node
                            _queue.append(child)
                _depth += 1
            return _depth_node_info[-1][0]

        start = bfs_get_longest(0)
        stop = bfs_get_longest(start)
        des_path: Optional[List[int]] = []
        t = stop
        while t != start:
            des_path.append(t)
            t = parent[t]
        des_path.append(t)
        # 使用深度优先遍历查找路径

        return [des_path[len(des_path) // 2 - 1], des_path[len(des_path) // 2]] if len(des_path) % 2 == 0 else [
            des_path[len(des_path) // 2]]


if __name__ == "__main__":
    # @formatter:off
    s = Solution()
    n = 10
    edges = [[0,3],[1,3],[2,3],[4,3],[5,3],[4,6],[4,7],[5,8],[5,9]]
    # @formatter:on
    print(s.findMinHeightTrees(n, edges))
