import copy
from typing import List, Dict, Set


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        使用拓扑排序
        每次都在存在的节点里面找出没有前驱的节点，然后取出来作，直到为空
        """
        des_list: List[int] = []
        graph_adj_dic: Dict[int, Set[int]] = {i: set() for i in range(numCourses)}
        for trail_pre in prerequisites:
            graph_adj_dic[trail_pre[1]].add(trail_pre[0])

        nodes = set(graph_adj_dic.keys())
        have_no_pre: Set = copy.copy(nodes)
        while len(nodes) > 0:
            for item in nodes:
                for trail in graph_adj_dic[item]:
                    have_no_pre.discard(trail)
            if len(have_no_pre) == 0:
                return []
            for item in have_no_pre:
                des_list.append(item)
                nodes.remove(item)
                # 时间复杂度来自这里，下一个版本去掉了复制这个过程
            have_no_pre = copy.copy(nodes)
        return des_list


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    s = Solution()
    print(s.findOrder(numCourses, prerequisites))
