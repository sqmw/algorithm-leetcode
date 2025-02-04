from typing import List, Set, Optional, Dict


class GraphNode:
    def __init__(self, val=0, next_adj_arr: 'List[GraphNode]' = None):
        self.val = val
        self.next_adj_arr = next_adj_arr


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        读完题目感觉就是拓扑排序
        需要判断是否存在环
        使用广度优先遍历
        """
        graph_node_dic: Dict[int, GraphNode] = {i: GraphNode(i) for i in range(numCourses)}
        # 构建图
        for pre_trail in prerequisites:
            if graph_node_dic[pre_trail[0]].next_adj_arr is None:
                graph_node_dic[pre_trail[0]].next_adj_arr = []
            graph_node_dic[pre_trail[0]].next_adj_arr.append(graph_node_dic[pre_trail[1]])

        visited_set: Optional[Set[int]] = set()
        # 用来记录边，判断是否有环
        now_set: Optional[Set[tuple]] = None
        _queue: List[GraphNode] = []
        for graph_val in graph_node_dic.keys():
            if graph_val not in visited_set:
                now_set = set()
                _queue.append(graph_node_dic[graph_val])
                while len(_queue) > 0:
                    temp_queue = []
                    for graph_node in _queue:
                        if graph_node.next_adj_arr is not None:
                            for item in graph_node.next_adj_arr:
                                if (graph_node.val, item.val) in now_set:
                                    return False
                                else:
                                    temp_queue.append(item)
                                    now_set.add((graph_node.val, item.val))
                    _queue = temp_queue
        return True


if __name__ == "__main__":
    numCourses = 8
    prerequisites = [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]

    s = Solution()
    print(s.canFinish(numCourses, prerequisites))
