class Counter:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self  # Make the object iterable and return the iterator itself
    
    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


# Using while loop with iterator
it = iter(Counter(5))  # calls Counter(5).__iter__()
while True:
    try:
        count = next(it)  # calls Counter(5).__next__()
        print(count)
    except StopIteration:
        break  # Exit the loop when iterable is exhausted
