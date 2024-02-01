class Solution:
    def isValid(self, s: str) -> bool:
        brackets_dic = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        left = ('(', '[', '{')
        # right = (')', ']', '}')
        stack_brackets = []
        for i in s:
            # 左括号，入栈
            if i in left:
                stack_brackets.append(i)
            # 右括号，出栈
            else:
                if len(stack_brackets) < 1 or stack_brackets.pop() != brackets_dic.get(i):
                    return False
        if len(stack_brackets) != 0:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("["))
