class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n=len(words)
        res=[0]*len(queries)
        count=[0]*(n+1)
        vowels=set("aeiou")
        prev=0
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prev+=1
            count[i+1]=prev
        for i,q in  enumerate(queries):
            res[i]=count[q[1]+1]-count[q[0]]
        return res