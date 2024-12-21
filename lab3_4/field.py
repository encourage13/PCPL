def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            value = item.get(args[0])
            if value is not None:
                yield value
        else:
            result = {}
            all_none = True
            for arg in args:
                value = item.get(arg)
                if value is not None:
                    result[arg] = value
                    all_none = False
            if not all_none:
                yield result


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'title': None, 'price': 5300, 'color': None}
]

print("field(goods, 'title'):")
for item in field(goods, 'title'):
    print(item)

print("\nfield(goods, 'title', 'price'):")
for item in field(goods, 'title', 'price'):
    print(item)

print("\nfield(goods, 'color'):")
for item in field(goods, 'color'):
    print(item)
