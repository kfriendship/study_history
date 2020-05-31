from collections import deque


def solution(heights):
    answer = [0] * len(heights)
    q = deque([(heights[-1], len(heights))])
    for i in range(len(heights) - 2, -1, -1):
        qsize = len(q)
        for j in range(qsize):
            now_h, idx = q.popleft()
            if heights[i] > now_h:
                answer[idx - 1] = i + 1
            else:
                q.append((now_h, idx))
        q.append((heights[i], i + 1))

    while q:
        now_h, idx = q.popleft()
        answer[idx - 1] = 0
    return answer
