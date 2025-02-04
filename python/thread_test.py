import asyncio
import threading

val = 1


async def task_a():
    global val
    val += 1
    await asyncio.sleep(2)
    print('task_a')


def task_b():
    print('task_b')


if __name__ == '__main__':
    thread_a = threading.Thread(target=lambda: asyncio.run(task_a()))
    thread_a.start()

    thread_b = threading.Thread(target=task_b)
    thread_b.start()

    # thread_b.join()
    # thread_a.join()
    print('test')
