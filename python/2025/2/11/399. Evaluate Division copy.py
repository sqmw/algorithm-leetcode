from collections import defaultdict
from typing import List, Dict, Set


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        计算除法表达式的结果
        
        Args:
            equations: 表达式列表，每个表达式形如 ["a", "b"] 表示 a/b
            values: 对应表达式的值
            queries: 需要计算的查询列表
            
        Returns:
            List[float]: 查询结果列表，如果无法计算则返回 -1.0
            
        Time: O(Q * (V + E)) 其中 Q 是查询数量，V 是变量数量，E 是方程数量
        Space: O(V^2) 用于存储图的邻接表
        """
        # 构建图的邻接表
        graph: Dict[str, Dict[str, float]] = defaultdict(dict)
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0 / value

        def dfs(start: str, target: str, visited: Set[str]) -> float:
            """深度优先搜索计算结果"""
            # 处理特殊情况
            if start not in graph or target not in graph:
                return -1.0
            if start == target:
                return 1.0
            if target in graph[start]:
                return graph[start][target]

            visited.add(start)
            # 遍历所有可能的路径
            for next_node, value in graph[start].items():
                if next_node not in visited:
                    result = dfs(next_node, target, visited)
                    if result != -1.0:
                        # 这个充分利用了题目的条件，我的之前的代码更具有普适性
                        return value * result
            visited.remove(start)
            return -1.0

        # 处理所有查询
        return [dfs(start, target, set()) for start, target in queries]


def test_solution():
    """测试用例"""
    test_cases = [
        (
            [["a", "b"], ["c", "d"]],
            [1.0, 1.0],
            [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]],
            [-1.0, -1.0, 1.0, 1.0]
        ),
        (
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            [6.0, 0.5, -1.0, 1.0, -1.0]
        )
    ]
    
    solution = Solution()
    for i, (equations, values, queries, expected) in enumerate(test_cases, 1):
        result = solution.calcEquation(equations, values, queries)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed!")


if __name__ == '__main__':
    test_solution()