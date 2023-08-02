class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        #self.idx = 0
        self.tables = {x:i for i, x in enumerate(names)}
        self.columns = [[[0 for _ in range(columns[i])]] for i in range(len(columns))]
        self.exists = set()
        #print(self.columns)

    def insertRow(self, name: str, row: List[str]) -> None:
        self.exists.add((name, len(self.columns[self.tables[name]])))
        self.columns[self.tables[name]].append(row)
        #print(self.columns)
        
    def deleteRow(self, name: str, rowId: int) -> None:
        #print(self.exists)
        self.exists.remove((name, rowId))

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        #print(self.exists)
        #print(self.columns)
        columnId -= 1
        #print(name, rowId, columnId)
        if (name, rowId) in self.exists:
            return self.columns[self.tables[name]][rowId][columnId]
        else:
            return None


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)