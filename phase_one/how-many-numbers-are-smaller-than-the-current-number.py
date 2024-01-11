class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr =sorted(nums)
        ls = [0]
        for i in range(1,len(nums)):
            if arr[i-1] == arr[i]:
                ls.append(ls[i-1])
            else:
                ls.append(i)
        dic = {}
        for j in range(len(arr)):
            dic[arr[j]]=ls[j]
        ls = [dic[k] for k in nums]
        return ls