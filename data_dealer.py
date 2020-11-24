"""
txt文件数据读取与处理 + 运行
"""
from decimal import Decimal

from prettytable import PrettyTable

from Dijkstra import Dijkstra
from class_utils import Dist
from class_utils import Station
from convert_func import convert


def run(file_path: str, subwayStationNum: int, subwayIndex: int, subwayDict: dict, reverseSubwayDict: dict, D: list,
        orientation: str = "", destination: str = ""):
    res_tb = PrettyTable()
    res_route = ""
    with open(file_path, encoding='utf-8') as file_object:
        subwayLinesNum = int(file_object.readline())
        for i in range(subwayLinesNum):
            subwayLineInfo = file_object.readline().rstrip().split('，')
            subwayLineNo = subwayLineInfo[1]
            for j in range(3, len(subwayLineInfo), 2):
                if not subwayLineInfo[j] in subwayDict:
                    subwayDict[subwayLineInfo[j]] = subwayStationNum
                    reverseSubwayDict[subwayStationNum] = subwayLineInfo[j]
                    D.append(Dist(subwayStationNum, float("inf"), False, subwayLineNo, 0))
                    subwayStationNum += 1
                else:
                    continue

    subwayList = [[] for _ in range(max(subwayDict.values()) + 1)]

    with open(file_path, encoding='utf-8') as file_object:
        next(file_object)
        for i in range(subwayLinesNum):
            subwayLineInfo = file_object.readline().rstrip().split('，')
            for j in range(3, len(subwayLineInfo) - 2, 2):
                subwayList[subwayDict[subwayLineInfo[j]]].append(
                    Station(subwayDict[subwayLineInfo[j + 2]], subwayLineInfo[j + 2], float(subwayLineInfo[j + 1])))
                subwayList[subwayDict[subwayLineInfo[j + 2]]].append(
                    Station(subwayDict[subwayLineInfo[j]], subwayLineInfo[j], float(subwayLineInfo[j + 1])))

    num_orientation = subwayDict[orientation]
    route = [destination]
    if destination != "":
        num_destination = subwayDict[destination]

        Dijkstra(subwayList, D, num_orientation)
        i = num_destination
        while D[i].previousStationIndex != num_orientation:
            route.append(reverseSubwayDict[D[i].previousStationIndex])
            i = D[i].previousStationIndex

        route.append(orientation)
        route.reverse()
    else:
        Dijkstra(subwayList, D, num_orientation)

    res_tb.field_names = ["SubwayLine", "SubwayStation", "Price", "Distance"]
    for i in range(len(D)):
        res_tb.add_row([D[i].subwayLineNo, reverseSubwayDict[D[i].index], str(convert(D[i].length)),
                        str(Decimal(D[i].length).quantize((Decimal('0.000'))))])
    for i in range(len(route) - 1):
        res_route = res_route + route[i] + "->"
    res_route = res_route + route[len(route) - 1]

    if destination == "":
        return res_tb
    else:
        return res_route
