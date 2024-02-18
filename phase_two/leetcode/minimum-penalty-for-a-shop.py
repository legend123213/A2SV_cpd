class Solution:
    def bestClosingTime(self, customers: str) -> int:
        arr_y = [0]
        arr_n = [0]
        min_ = float("inf")
        res = 0
        for i in customers:
            if i =="Y":
                arr_y.append(1)
                arr_n.append(0)
            else:
                arr_y.append(0)
                arr_n.append(1)
        for i in range(1,len(arr_y)):
            arr_y[i]+=arr_y[i-1]
            arr_n[i]+=arr_n[i-1]
        for i in range(len(arr_y)):
            k = arr_y[len(arr_y)-1]-arr_y[i]
            if k + arr_n[i] < min_:
                min_ =  k + arr_n[i]
                res = i
        return res

        