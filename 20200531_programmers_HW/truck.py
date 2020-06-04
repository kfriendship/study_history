"""
대기 queue
다리 queue
다리위에 트럭 수 int
다리위에 트럭들의 무게 합 int
지나간 list

while 다리 지난 트럭의 길이가 트럭수와 같지 않고, 다리위에 트럭수가 0이 아니면 반복
다리에 있는 트럭중 현재 시간과 다리에 올라온 시간의 차가 다리의 길이보다 크면 pop
다리에 있는 트럭수가 다리 길이보다 작고
	다리에 있는 트럭들의 무게 합 + 대기하고 있는 맨앞 트럭의 무게 <= 다리 무게면
    	대기트럭에서 빼서 다리에 올리기
"""


def solution(bridge_length, weight, truck_weights):
    n = len(truck_weights)
    truck_weights = truck_weights[::-1]
    bridge, after = [], []
    truck_time = [0] * n

    i, j = 0, -1
    while len(after) < n:
        if len(truck_weights) and sum(bridge) + truck_weights[-1] <= weight:
            bridge.append(truck_weights.pop())
            j += 1

        truck_time[:j + 1] = [truck_time[z] + 1 for z in range(j + 1)]

        if truck_time[i] == bridge_length:
            after.append(bridge.pop(0))
            i += 1

    return truck_time[0] + 1
