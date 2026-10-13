class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = {}

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1

        maxheap = []

        for char, freq in hashmap.items():
            heapq.heappush(maxheap, [-freq, char])

        res = []
        prev = None

        while maxheap:
            freq, char = heapq.heappop(maxheap)
            freq = -freq

            res.append(char)
            freq -= 1

           
            if prev:
                prev_freq, prev_char = prev
                heapq.heappush(maxheap, [-prev_freq, prev_char])

            prev = (freq, char) if freq > 0 else None

        if len(res) != len(s):
            return ""

        return "".join(res)