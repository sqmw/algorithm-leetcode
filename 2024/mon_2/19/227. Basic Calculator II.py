from typing import List, Union


class Solution:
    def calculate(self, s: str) -> int:
        """
        T(n): O(n)
        S(n): O(n)
        该算法实现了对一般表达式的求值，支持运算符 + - * / ^ 以及分界符号( )
        计算结果按照题目意思是 int, 如果需要将计算结果改为精度高的 float，需要去掉 cal_postfix_expression 里面的向零取证
        """
        expression: List[str] = s2infix_expression_list(s)
        postfix_expression = infix2postfix(expression)
        return cal_postfix_expression(postfix_expression)


precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def s2infix_expression_list(s: str) -> List[str]:
    """
    将 s 转化成 list 类型的中缀表达式
    """
    assert s is not None
    infix_expression: List[str] = []
    s = s.replace(' ', '')
    i = 0
    while i < len(s):
        if s[i] in precedence or s[i] == '(' or s[i] == ')':
            infix_expression.append(s[i])
            i += 1
        else:
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            infix_expression.append(s[i:j])
            i = j
    return infix_expression


def infix2postfix(infix: List[str]) -> List[str]:
    """
    将 list 类型的中缀表达式转化成 list 类型的后缀表达式
    栈 里面只存运算符和表达式
    扫描到 ( 直接入栈
    扫描到：运算符 + - * / ^
        栈顶为 ( 或者栈为空，直接入栈
        将栈里面的运算符弹出到栈顶运算符都比将要入栈的这个小
    """
    postfix_expression: List[str] = []
    operator_stack: List[str] = []

    for item in infix:
        if item.isdigit():
            postfix_expression.append(item)
        else:
            if item == ')':
                while operator_stack[-1] != '(':
                    postfix_expression.append(operator_stack.pop())
                operator_stack.pop()
            elif item == '(':
                operator_stack.append(item)
            # 表示 item 是运算符
            else:
                if len(operator_stack) == 0 or operator_stack[-1] == '(':
                    operator_stack.append(item)
                else:
                    while len(operator_stack) > 0 and operator_stack[-1] in precedence and \
                            precedence[item] <= precedence[operator_stack[-1]]:
                        postfix_expression.append(operator_stack.pop())
                    operator_stack.append(item)
    while len(operator_stack) > 0:
        postfix_expression.append(operator_stack.pop())

    return postfix_expression


def cal_postfix_expression(postfix_expression: List[str]) -> Union[float | int]:
    """
    计算后缀表达式的值(向零去整:int(str_item))
    """
    cal_stack: List[int] = []
    for item in postfix_expression:
        if item.isdigit():
            cal_stack.append(int(item))
        else:
            b = cal_stack.pop()
            a = cal_stack.pop()
            if item == '+':
                cal_stack.append(int(a + b))
            elif item == '-':
                cal_stack.append(int(a - b))
            elif item == '*':
                cal_stack.append(int(a * b))
            elif item == '/':
                cal_stack.append(int(a / b))
            elif item == '^':
                cal_stack.append(int(a ** b))
    return cal_stack[0]


if __name__ == "__main__":
    # 左边括号直接进入、右边括号弹出到遇到右括号
    expression_str = "3 + 5 / 2"
    s = Solution()
    print(s.calculate(expression_str))
