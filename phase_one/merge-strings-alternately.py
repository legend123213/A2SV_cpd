class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1=0
        ptr2=1
        wor1=[word1[i] for i in range(len(word1))]
        wor2=[word2[i] for i in range(len(word2))]
        while ptr1!=len(word1):
            wor2.insert(ptr2-1,wor1[ptr1])
            ptr1+=1
            ptr2+=2
        return "".join(wor2)

                
                
        