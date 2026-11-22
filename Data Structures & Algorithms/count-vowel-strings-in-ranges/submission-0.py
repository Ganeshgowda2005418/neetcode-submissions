class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n=len(queries)
        res=[0]*n
        vowels="aeiou"
        for i in range(n):
            start,end=queries[i][0],queries[i][1]
            count=0
            for char in range(start,end+1):
                if words[char][0] in vowels and words[char][-1] in vowels: 
                        count+=1
            res[i]=count

        return res