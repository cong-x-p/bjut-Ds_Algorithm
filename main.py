from data_dealer import run

orientation = input("")
destination = input("")

if __name__ == "__main__":
    print(run(file_path='BaseSubWayInfo.txt', subwayStationNum=0, subwayIndex=0, subwayDict={}, reverseSubwayDict={},
              D=[],
              orientation=orientation, destination=destination))
