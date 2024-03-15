class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        arr = []
        res = []
        for i in range(len(s)):
            if s[i] == "|":
                arr.append(i)
        for qu in queries:
            res_m = []
            for i in range(2):       
                l = 0
                r = len(arr)-1
                k = queries[0][1]
                while l<=r:
                    mid = l+(r-l)//2
                    if arr[mid] == qu[i]:
                        res_m.append(mid)
                        break
                    if qu[i] > arr[mid]:
                        l = mid+1
                    else:
                        r = mid-1
                else:
                    if i == 1:
                        res_m.append(r)
                    else:
                        res_m.append(l)
            if res_m[1] >= res_m[0]:
                res.append((arr[res_m[1]]-arr[res_m[0]]) - (res_m[1]-res_m[0]))
            else:
                res.append(0)
            
        return res