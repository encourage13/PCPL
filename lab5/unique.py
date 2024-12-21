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




