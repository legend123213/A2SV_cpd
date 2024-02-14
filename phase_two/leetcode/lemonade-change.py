class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5:0,10:0,20:0}
        for i,val in enumerate(bills):
            dic[val]+=1
            if val ==10:
                dic[5]-=1
                if dic[5]<0:
                    return False
            if val == 20:
                if dic[10]>=1:
                    dic[10]-=1
                    dic[5]-=1
                    if dic[5]<0:
                        return False
                else:
                    if dic[5]>=3:
                        dic[5]-=3
                    else:return False
            print(dic)
        return True

                
                
            
