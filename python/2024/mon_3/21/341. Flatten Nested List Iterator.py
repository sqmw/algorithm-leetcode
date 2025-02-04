# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        """
        为了方便这里直接使用了饿汉加载
        T(n): O(n/n) # n 表示的是实际的数字的数量
        S(n): O(n)
        """
        self._list = []

        # 这里使用递归直接一次性在初始化的时候完成所有的时间复杂度，后面的操作都是常数级别的时间复杂度
        def recurse_add(n_i: NestedInteger):
            if n_i.isInteger():
                self._list.append(n_i.getInteger())
            else:
                for _n_i in n_i.getList():
                    recurse_add(_n_i)

        for item in nestedList:
            recurse_add(item)
        self._now_cur = 0

    def next(self) -> int:
        self._now_cur += 1
        return self._list[self._now_cur - 1]

    def hasNext(self) -> bool:
        return self._now_cur < len(self._list)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

