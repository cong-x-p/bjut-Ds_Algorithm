class Station:
    def __init__(self, stationNum: int, StationName: str, distance: float):
        self.stationNum = stationNum
        self.StationName = StationName
        self.distance = distance


class Dist:
    def __init__(self, index: int, length: float, visited: bool, subwayLineNo: str, previousStationIndex: int):
        self.index = index
        self.length = length
        self.visited = visited
        self.subwayLineNo = subwayLineNo
        self.previousStationIndex = previousStationIndex
