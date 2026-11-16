class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        source=set()
        dest=set()
        for p in paths:
            source.add(p[0])
            dest.add(p[1])
        for city in dest:
            if city not in source:
                return city