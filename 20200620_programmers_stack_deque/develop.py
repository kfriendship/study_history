from math import ceil

def solution(progresses, speeds):
    answer = []
    max_day, day_cnt = ceil((100-progresses[0])/speeds[0]), 1
    for p, s in zip(progresses[1:], speeds[1:]):
        day = ceil((100-p)/s)
        if day > max_day:
            answer.append(day_cnt)
            max_day, day_cnt = day, 1
        else:
            day_cnt += 1
    answer.append(day_cnt)
    return answer
