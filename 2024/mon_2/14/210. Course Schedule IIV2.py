from typing import List, Dict, Set
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 构建邻接表
        graph_adj_dic: Dict[int, Set[int]] = {i: set() for i in range(numCourses)}
        in_degree = [0] * numCourses

        for trail_pre in prerequisites:
            # 构建邻接表
            graph_adj_dic[trail_pre[1]].add(trail_pre[0])
            # 用来表示一个节点的入度
            in_degree[trail_pre[0]] += 1

        # 初始化队列，将入度为0的节点加入队列
        queue = deque([node for node, degree in enumerate(in_degree) if degree == 0])
        result = []

        while len(queue) > 0:
            current_node = queue.popleft()
            result.append(current_node)

            # 更新邻接表和入度，并将入度为0的节点加入队列
            for neighbor in graph_adj_dic[current_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # 如果结果集合的长度等于课程数，说明拓扑排序成功，返回结果
        return result if len(result) == numCourses else []


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    s = Solution()
    print(s.findOrder(numCourses, prerequisites))
