class BrowserHistory:

    def __init__(self, homepage: str):
        self.res=[homepage]
        self.p=0

    def visit(self, url: str) -> None:
        self.res=self.res[:self.p+1]
        self.res.append(url)
        self.p=len(self.res)-1

    def back(self, steps: int) -> str:
        self.p=max(0,self.p-steps)
        return self.res[self.p]

    def forward(self, steps: int) -> str:
        self.p=min(len(self.res)-1,self.p+steps)
        return self.res[self.p]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)