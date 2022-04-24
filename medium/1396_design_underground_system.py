class UndergroundSystem:

    def __init__(self):
        self.users = {}
        self.records = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.users[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.users[id][0]
        key = f'{startStation}-{stationName}'
        self.records[key] = self.records.get(
            key, []) + [t - self.users[id][1]]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = f'{startStation}-{endStation}'
        length = len(self.records[key])
        avg = sum(self.records[key]
                  ) / length if length else 0
        return avg

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
