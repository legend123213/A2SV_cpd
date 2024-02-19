class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex ==1:
            return [1,1]
        prev = self.getRow(rowIndex-1)
        cur_row = [prev[i]+prev[i+1] for i in range(len(prev)-1)]
        cur_row.append(1)
        cur_row.insert(0,1)
        return cur_row
        