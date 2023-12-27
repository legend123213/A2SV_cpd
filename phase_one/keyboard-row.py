class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        test = [i.lower() for i in words]
        keyy = ["eiopqrtuwy","adfghjkls","bcmnvxz"]
        ls = {}
        l =[]
        for i in range(3):
            for j in keyy[i]:
                ls[j]=i
        for word in words:
            k = ls[word[0].lower()]
            for s in word:
                if k != ls[s.lower()]:
                    break
            else:
                l.append(word) 
        return l
           
        
        

        