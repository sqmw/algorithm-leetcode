import threading

# 创建事件
event_a = threading.Event()
event_b = threading.Event()

is_a = True


def _print_a():
    global is_a
    t = 500000
    while True:
        if t > 0:
            if is_a:
                is_a = not is_a
                print("A")
                t -= 1
        else:
            break


def _print_b():
    global is_a
    t = 500000
    while True:
        if t > 0:
            if not is_a:
                is_a = not is_a
                print("B")
                t -= 1
        else:
            break


t_a = threading.Thread(target=_print_a)
t_b = threading.Thread(target=_print_b)

if __name__ == '__main__':
    t_a.start()
    t_b.start()
