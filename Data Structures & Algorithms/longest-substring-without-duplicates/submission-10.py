class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        r=0
        count=0
        for l in range(len(s)):
            while seen and s[l] in seen:
                seen.remove(s[r])
                r+=1
            count=max(l-r+1,count)
            seen.add(s[l])
        return count