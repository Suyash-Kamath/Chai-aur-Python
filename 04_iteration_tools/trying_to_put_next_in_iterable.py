class BadIterable:
    def __init__(self, data):
        self.data = data
        self.index = 0
        
    def __iter__(self):
        return self  # returns itself 😬

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value


x = BadIterable([10, 20, 30,40,50,60,70])

it1 = iter(x)
it2 = iter(x)

print(next(it1))  # 10
print(next(it2))  # 20  <-- WHAT?!
print(next(it1))  # 10
print(next(it2))  # 20  <-- WHAT?!
print(next(it1))  # 10
print(next(it2))  # 20  <-- WHAT?!

print(id(it1))
print(id(it2))
