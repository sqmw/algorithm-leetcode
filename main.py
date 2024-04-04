import heapq

if __name__ == "__main__":
    l = [2, 3, 4, 5, 6, 7, 1]
    heapq.heapify(l)
    while len(l) > 0:
        print(heapq.heappop(l))
