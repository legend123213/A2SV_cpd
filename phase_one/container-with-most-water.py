class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptr_f= 0
        ptr_l=len(height)-1
        MAX =0
        while ptr_l-ptr_f>=0:
            M = min(height[ptr_l],height[ptr_f])
            d= (ptr_l-ptr_f)
            MAX = max(MAX,M*d)

            if height[ptr_l]<height[ptr_f]:
                ptr_l-=1
            else:
                ptr_f+=1
        return MAX





        