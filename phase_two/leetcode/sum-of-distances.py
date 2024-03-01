from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dic = defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        for ky,val in dic.items():
            for i in range(1,len(val)):
                val[i]+=val[i-1]
            val.append(0)
            val.insert(0,0)
        for key,num in dic.items():
            ls = []
            for i in range(1,len(num)):
                front =((i-1)*(num[i]-num[i-1])) -  num[i-1] 
                back = (num[len(num)-2]-num[i])
                no  = (len(num)-(i+2)) * (num[i]-num[i-1])
                real_back = back-no
                ls.append(front+real_back)
            ls.pop()
            dic[key]=ls
        ls = []
        for i in range(len(nums)):
            ls.append(dic[nums[i]][0])
            dic[nums[i]].pop(0)
        return ls
        