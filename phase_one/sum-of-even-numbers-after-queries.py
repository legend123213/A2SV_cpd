class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_s = 0
        re = [] 
        ls = nums
        for i in nums:
            if i %2 == 0 :
                even_s += i
        for i in range(len(queries)):
            if ls[queries[i][1]]%2==0 and (ls[queries[i][1]]+queries[i][0])%2==0: 
                ls[queries[i][1]] = ls[queries[i][1]] + queries[i][0]
                even_s+=queries[i][0]
                re.append(even_s)
            elif ls[queries[i][1]]%2!=0 and (ls[queries[i][1]]+queries[i][0])%2==0:
                ls[queries[i][1]] = ls[queries[i][1]] + queries[i][0]
                even_s+=ls[queries[i][1]]
                re.append(even_s)
                 
            elif ls[queries[i][1]]%2==0 and (ls[queries[i][1]]+queries[i][0])%2!=0:
                
                even_s -=ls[queries[i][1]]
                re.append(even_s)
                ls[queries[i][1]]= ls[queries[i][1]]+queries[i][0]
            else:
                ls[queries[i][1]]= ls[queries[i][1]]+queries[i][0]
                # even_s+=ls[queries[i][1]]
                re.append(even_s)
        return re










        