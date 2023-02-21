class Link:
    def __init__(self,url:str):
        self.url = url
        self.next = None
        self.previous = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Link(homepage)
        self.page = Link(homepage)


    def visit(self, url: str) -> None:
        newlink = Link(url)
    
        self.page.next = newlink
        newlink.previous = self.page
        self.page = newlink
     
    
        
    def back(self, steps: int) -> str:
        
        while self.page.previous and steps:
            self.page = self.page.previous
            steps -= 1
        return self.page.url    

    def forward(self, steps: int) -> str:
        while self.page.next and steps:
            self.page = self.page.next
            steps -= 1
        return self.page.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)