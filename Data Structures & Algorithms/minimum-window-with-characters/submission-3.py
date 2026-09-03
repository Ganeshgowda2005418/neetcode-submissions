class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counT,window={},{}
        for c in t:
            counT[c]=1+counT.get(c,0)
        l=0
        need,have=len(counT),0
        res,reslen=[-1,-1],float("inf")
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            if c in counT and window[c]==counT[c]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                window[s[l]]-=1
                if s[l] in counT and window[s[l]]<counT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!="inf" else ""
