# Last updated: 18/12/2025, 20:17:09
class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        # id -> (startStation , startTime)
        self.trips = {}
        #(startStation, endStation) : (total_time, entries)

        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkin.pop(id) # remove entry once used.
        timeelapsed = t - startTime
        route = (startStation, stationName)
        if route in self.trips:
            self.trips[route][0] += timeelapsed
            self.trips[route][1] +=1
        else:
            self.trips[route] = [timeelapsed, 1]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.trips.get((startStation, endStation), (0,0))
        if count == 0:
            return 0
        return total/count

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)