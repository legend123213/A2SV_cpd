class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for k in image:
            i = 0
            j = len(k)-1
            while i<=j:
                k[i],k[j] = abs(k[j]-1),abs(k[i]-1)
                i+=1
                j-=1
        return image
        