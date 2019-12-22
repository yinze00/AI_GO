class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []

        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.stack) == 0:
            self.helper.append(x)
        else:
            if x <= self.helper[-1]:
                self.helper.append(x)

    def pop(self) -> None:
        num = self.stack.pop()
        

    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()