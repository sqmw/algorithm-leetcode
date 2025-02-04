"""
时间复杂度 O(n)，但是判断比较复杂，没有进行优化，因此性能有一些差距，同时没有使用高级语言的一些特性
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        des_str: str = ''
        i = 0
        while i < len(path):
            # 表示开始是 /
            if path[i] == '/':
                if (des_str != '' and des_str[len(des_str) - 1] != '/') or des_str == '':
                    des_str += '/'
                i += 1
                for j in range(i, len(path)):
                    if j != '/':
                        i = j
                        break
            elif path[i] == '.':
                if i + 1 < len(path):
                    if path[i + 1] == '/':
                        if i == 0 or path[i - 1] == '/':
                            i += 2
                        else:
                            des_str += './'
                            i += 2
                    elif path[i + 1] == '.':
                        if i == 0:
                            if i + 2 >= len(path):
                                return '/'
                            else:  # ..?
                                if path[i + 2] == '/':
                                    des_str += '/'
                                    i += 3
                                else:
                                    temp_str = '..'
                                    for j in range(i + 2, len(path)):
                                        if path[j] == '/':
                                            des_str += temp_str
                                            break
                                        else:
                                            temp_str += path[j]
                        # 表示遇到了 /../ 或者 /.. 需要回退
                        elif i > 0 and path[i - 1] == '/' and (i + 2 == len(path) or path[i + 2] == '/'):
                            i += 2
                            is_first = True
                            for j in range(len(des_str) - 1, -1, -1):
                                if des_str[j] == '/':
                                    if not is_first:
                                        des_str = des_str[:j + 1]
                                        break
                                    else:
                                        is_first = False
                        else:
                            temp_str = '..'
                            i += 2
                            for j in range(i, len(path)):
                                if path[j] != '.':
                                    i = j
                                    break
                                else:
                                    temp_str += path[j]
                            des_str += temp_str
                    else:
                        temp_str = '.'
                        i += 1
                        for j in range(i, len(path)):
                            if path[j] == '/':
                                i = j
                                break
                            else:
                                temp_str += path[j]
                                i += 1
                        des_str += temp_str
                else:
                    i += 1
            else:
                des_str += path[i]
                i += 1
        for i in range(len(des_str) - 1, -1, -1):
            if des_str[i] != '/':
                des_str = des_str[:i + 1]
                break
        return des_str


if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath("/hello./world/"))  # "/a//b////c/d//././/.."
