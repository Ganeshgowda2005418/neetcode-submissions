class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hashmap=Counter(chars)
        count=0
        for w in words:
            curr=Counter(w)
            currcount=0
            for i in w:
                if curr[i]<=hashmap[i]:
                    currcount+=1
                else:
                    currcount=0
                    break
            count+=currcount
        return count