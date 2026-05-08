class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        arr=[]
        for s in strs:
            arr.append(str(len(s)))
            arr.append("#")
            arr.append(s)
        return "".join(arr)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            res.append(word)
            i = j + 1 + length
        return res
