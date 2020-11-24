"""
Dijkstra算法
"""


def Dijkstra(subwayList: list, D: list, s: int):
    for i in range(len(subwayList[s])):
        D[subwayList[s][i].stationNum].length = subwayList[s][i].distance
    for i in range(len(D)):
        D[i].previousStationIndex = s

    D[s].length = 0
    D[s].visited = True
    count = 1
    while count != len(subwayList):
        min_index = 0

        for i in range(len(subwayList)):
            if not D[i].visited and D[i].length != 0:
                min_index = i
                break

        for i in range(len(subwayList)):
            if not D[i].visited and D[i].length < D[min_index].length:
                min_index = i

        label = min_index
        D[label].visited = True
        for i in range(len(subwayList[label])):
            if not D[subwayList[label][i].stationNum].visited and subwayList[label][i].distance + D[label].length < D[
                subwayList[label][i].stationNum].length:
                D[subwayList[label][i].stationNum].length = subwayList[label][i].distance + D[label].length
                D[subwayList[label][i].stationNum].previousStationIndex = label

        count += 1
