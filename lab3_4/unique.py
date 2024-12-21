class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.seen = set()
        self.ignore_case = kwargs.get('ignore_case', False)

    def __next__(self):
        while True:
            item = next(self.items)
            if self.ignore_case and isinstance(item, str):
                item = item.lower()
            if item not in self.seen:
                self.seen.add(item)
                return item

    def __iter__(self):
        return self


import random

data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
print("Unique(data):")
for item in Unique(data):
    print(item)

data = (random.randint(1, 3) for _ in range(10))
print("\nUnique(gen_random(10, 1, 3)):")
for item in Unique(data):
    print(item)

data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
print("\nUnique(data):")
for item in Unique(data):
    print(item)

print("\nUnique(data, ignore_case=True):")
for item in Unique(data, ignore_case=True):
    print(item)
