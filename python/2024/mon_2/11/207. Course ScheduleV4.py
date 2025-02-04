from typing import List, Dict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        使用深度优先遍历实现
        这道题目描述有问题
        节点为 [0, numCourses)
        """
        graph: Dict[int, List[int]] = {i: [] for i in range(numCourses)}
        for pre_trail in prerequisites:
            graph[pre_trail[0]].append(pre_trail[1])

        visited_dic: Dict = {i: 0 for i in range(numCourses)}

        def depth_first_search(node: int):
            nonlocal can_finish
            visited_dic[node] = 1
            for neighbor_node in graph[node]:
                if visited_dic[neighbor_node] == 0:
                    depth_first_search(neighbor_node)
                elif visited_dic[neighbor_node] == 1:
                    can_finish = False
            visited_dic[node] = 2

        can_finish = True

        for i in range(numCourses):
            if visited_dic[i] == 0:
                depth_first_search(i)

        return can_finish


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]

    s = Solution()
    print(s.canFinish(numCourses, prerequisites))
