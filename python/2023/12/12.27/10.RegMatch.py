def isSimpleChr(c: str):
    if c == '.' or c == '*':
        return False
    return True


def isMatch(self, s: str, p: str) -> bool:
    s_index = 0
    p_index = 0
    while True:
        # 表示结束
        if s_index > len(s) - 1:
            if p_index > len(p) - 1:
                return True
            else:
                start_index = p_index
                while True:
                    if start_index == len(p):
                        return True
                    if p[start_index] != '*':
                        return False
                    start_index += 1

        if s_index == len(s) - 1:
            if s[s_index] == p[p_index] or p[p_index] == '.':
                s_index += 1
                p_index += 1
            else:
                return False
        if p_index == len(p):
            if s_index > len(s) - 1:
                return True
            else:
                return False
        if p_index == len(p) - 1:
            if s_index < len(s) - 1:
                return False
            elif s_index == len(s) - 1:
                if s[s_index] == p[p_index] or p[p_index] == '.':
                    return True
                else:
                    return False
            else:
                if p[p_index] == '*':
                    return True
                else:
                    return False

        # 表示的是普通的字符
        if isSimpleChr(p[p_index]):
            # 判断下一个字符
            print(p_index)
            if p[p_index + 1] != '*':
                if s[s_index] != p[p_index]:
                    return False
                else:
                    s_index += 1
                    p_index += 1
            # p_index + 1 == *
            else:
                if p[p_index] == s[s_index]:
                    while True:
                        s_index += 1
                        if s_index == len(s) or s[s_index] != '*':
                            s_index += 1
                            break

                # 这个语句用来移动 p_index
                index_same_start = p_index + 1
                while index_same_start + 1 < len(p) and p[index_same_start] == p[index_same_start + 1]:
                    index_same_start += 1
                p_index = index_same_start + 1
        # 表示的是字符 .
        elif p[p_index] == '.':
            if p[p_index + 1] == '*':
                s_index = len(s)
            else:
                s_index += 1
            index_same_start = p_index + 1
            while index_same_start + 1 < len(p) and p[index_same_start] == p[index_same_start + 1]:
                index_same_start += 1
            p_index = index_same_start + 1
        # 不存在 * 的情况，因为前两个考虑进去了


print(isMatch(0, 'aaa', 'a.a'))
