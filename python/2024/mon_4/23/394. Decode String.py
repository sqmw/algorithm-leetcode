class Solution:
    def decodeString(self, s: str) -> str:
        """
        用栈来实现，不用递归
        T(n): O(n)
        S(n): O(n)
        """
        _stack = []
        for i in range(len(s)):
            if s[i] == ']':
                inner_str = ''
                popped = _stack.pop()
                # 弹栈，并且获取其 中间的需要重复的字符串
                while popped != '[':
                    inner_str = popped + inner_str
                    popped = _stack.pop()

                cou_num_str = ''
                # 弹栈，并且获取其 中间的需要重复的字符串
                while len(_stack) > 0 and _stack[-1].isnumeric():
                    cou_num_str = _stack.pop() + cou_num_str

                cou = int(cou_num_str)
                _stack.append(inner_str * cou)

            else:
                _stack.append(s[i])
        return ''.join(_stack)


if __name__ == '__main__':
    s = Solution()
    print(s.decodeString("100[leetcode]"))
