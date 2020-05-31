def solution(heights):
    answer = [0] * len(heights)
    stack = [(heights[-1], len(heights))]
    for i in range(len(heights) - 2, -1, -1):
        for j in range(len(stack)):
            now_h, idx = stack.pop()
            if heights[i] > now_h:
                answer[idx - 1] = i + 1
            else:
                stack.append((now_h, idx))
        stack.append((heights[i], i + 1))

    return answer
