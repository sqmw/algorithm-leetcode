from typing import List, Union


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_num(s: str) -> bool:
            try:
                float(s)
                return True
            except ValueError:
                return False

        _stack: List[Union[int | str]] = []
        for i in range(len(tokens)):
            if is_num(tokens[i]):
                _stack.append(int(tokens[i]))
            else:
                if tokens[i] == '+':
                    last = _stack.pop()
                    pre = _stack.pop()

                    _stack.append(pre + last)
                elif tokens[i] == '-':
                    last = _stack.pop()
                    pre = _stack.pop()

                    _stack.append(pre - last)
                elif tokens[i] == '*':
                    last = _stack.pop()
                    pre = _stack.pop()

                    _stack.append(int(pre * last))
                # 表示 /
                else:
                    last = _stack.pop()
                    pre = _stack.pop()

                    _stack.append(int(pre / last))
        return int(_stack[0])


if __name__ == '__main__':
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
