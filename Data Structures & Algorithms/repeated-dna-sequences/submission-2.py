class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen=set()
        repeated=set()
        for i in range(len(s)-9):
            sequance=s[i:i+10]
            if sequance in seen:
                repeated.add(sequance)
            else:
                seen.add(sequance)
        return list(repeated)