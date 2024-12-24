class stack:
    def __init__(self,matrix : list = []):
        self.matrix = matrix
    
    def __repr__(self) -> str:
        return f'{self.matrix}'
    
    def Push(self,other):
        if type(other) == list:
            self.matrix.extend(other)
        else:
            self.matrix.append(other)

    def Pop(self):
        if len(self.matrix)==0:
            raise ValueError("List Is Empty : ")
        else:
            return self.matrix.pop()
