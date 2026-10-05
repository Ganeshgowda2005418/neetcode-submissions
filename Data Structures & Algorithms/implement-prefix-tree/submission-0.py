class TreeNode():
    def __init__(self):
        self.children=[None]*26
        self.endOfworld=False
class PrefixTree:
    def __init__(self):
        self.root=TreeNode()

    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            ind=ord(c)-ord("a")
            if curr.children[ind]==None:
                curr.children[ind]=TreeNode()
            curr=curr.children[ind]
        curr.endOfworld=True

    def search(self, word: str) -> bool:
        curr=self.root
        for c in word:
            ind=ord(c)-ord("a")
            if curr.children[ind]==None:
                return False
            curr=curr.children[ind]
        return curr.endOfworld

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for s in prefix:
            ind=ord(s)-ord("a")
            if curr.children[ind]==None:
                return False
            curr=curr.children[ind]
        return True
        