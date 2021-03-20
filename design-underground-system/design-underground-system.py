class UndergroundSystem:

    def __init__(self):
        self.cust_loc = defaultdict(list)
        self.edge_times = defaultdict(list)
        

    def checkIn(self, cid: int, stationName: str, t: int) -> None:
        self.cust_loc[cid] = [stationName, t]


        
    def checkOut(self, cid: int, stationName: str, t: int) -> None:
        if self.cust_loc[cid]:
            self.edge_times[str(self.cust_loc[cid][0]) + '_' + stationName].append(t - self.cust_loc[cid][1])
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.edge_times[startStation + '_' + endStation]) / len(self.edge_times[startStation + '_' + endStation])