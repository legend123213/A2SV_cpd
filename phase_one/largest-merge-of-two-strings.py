class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ptr_1 = 0
        ptr_2 = 0
        ls = []
        while ptr_1<len(word1) and ptr_2 <len(word2):
            MAX = max(word1[ptr_1:],word2[ptr_2:])
            if MAX == word1[ptr_1:]:
                ls.append(MAX[0])
                ptr_1+=1
            else:
                ls.append(MAX[0])
                ptr_2+=1
        ls+=word1[ptr_1:]
        ls+=word2[ptr_2:]
        return ''.join(ls)