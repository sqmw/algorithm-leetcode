import collections
from typing import List, Dict, Set


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        思路：构建 dict 不断查找，知道可以消除之间的所有字符达到目标字符如果遇到未出现过的字符，则返回 -1
        T(n): O(n*m) 大概
        S(n): O(n**2)
        """
        res: List[float] = []
        # 用来进行性能优化
        cache: Dict[str, Dict[str, float]] = collections.defaultdict(dict)
        for index, a_b in enumerate(equations):
            a, b = a_b
            cache[a][b] = values[index]
            cache[b][a] = 1 / values[index]

        val = 1
        # 1：已经找到了正确的路，0 路不通 -1 init
        done: int = -1
        visited: Set[str] = set()

        def traceback(x: str, y: str):
            # 需要避免出现环
            visited.add(x)
            nonlocal val, done
            if done != -1:
                return
            if x not in cache or y not in cache:
                val = -1
                done = 0
                return
            if x in cache and y in cache[x]:
                done = 1
                val *= cache[x][y]
                return
            for _x in cache[x]:
                if _x in visited:
                    continue
                val *= cache[x][_x]
                traceback(_x, y)
                if done != -1:
                    return
                val /= cache[x][_x]

        for query in queries:
            visited = set()
            done = -1
            val = 1
            a, b = query
            traceback(a, b)
            if done != 1:
                val = -1
            res.append(val)
        return res


if __name__ == '__main__':
    # [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    # [1.5, 0.5, -1, 0.25, -1]
    s = Solution()
    equations = [["a", "b"], ["c", "d"]]
    values = [1.0, 1.0]
    queries = [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]
    print(s.calcEquation(equations, values, queries))
