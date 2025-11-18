class ListIterator:
    def __init__(self,data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >=len(self.data):
            raise StopIteration
        value=self.data[self.index]
        self.index+=1
        return value



class MyIterable:
    def __init__(self,data):
        self.data = data
    
    def __iter__(self):
        return ListIterator(self.data)
    

it1 = iter(MyIterable([10,20,30]))
it2 = iter(MyIterable([40,50,60]))

print(next(it1))
print(next(it2))