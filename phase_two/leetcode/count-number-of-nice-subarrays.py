class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        k_ind = []
        for i in range(len(nums)):
            if nums[i]%2!=0:
                k_ind.append(i)
        k_ind.append(len(nums))
        k_ind.insert(0,-1)
        ptr = 1
        ptr_f = k
        count = 0
        while ptr_f<len(k_ind)-1:
            nu = k_ind[ptr]-k_ind[ptr-1]
            ni = k_ind[ptr_f+1]-k_ind[ptr_f]
            count+=(nu*ni)
            ptr+=1
            ptr_f+=1
        return count
