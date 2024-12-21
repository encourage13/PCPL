import field
import gen_random
import unique
from print_result import print_result
import cm_timer
from time import sleep
import sort
import random
import sys
import os
from process_data import f1, f2, f3, f4
import json

# Тесты для field.py
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'title': None, 'price': 5300, 'color': None}
]

print("\n--- field.py tests ---")
print("field(goods, 'title'):")
for item in field.field(goods, 'title'):
    print(item)

print("\nfield(goods, 'title', 'price'):")
for item in field.field(goods, 'title', 'price'):
    print(item)

print("\nfield(goods, 'color'):")
for item in field.field(goods, 'color'):
    print(item)

# Тесты для gen_random.py
print("\n--- gen_random.py tests ---")
print("\ngen_random(5, 1, 3):")
for item in gen_random.gen_random(5, 1, 3):
    print(item)

# Тесты для unique.py
print("\n--- unique.py tests ---")
data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
print("\nUnique(data):")
for item in unique.Unique(data):
    print(item)

data = (random.randint(1, 3) for _ in range(10))
print("\nUnique(gen_random(10, 1, 3)):")
for item in unique.Unique(data):
    print(item)

data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
print("\nUnique(data):")
for item in unique.Unique(data):
    print(item)

print("\nUnique(data, ignore_case=True):")
for item in unique.Unique(data, ignore_case=True):
    print(item)

# Тесты для sort.py
print("\n--- sort.py tests ---")
data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
result = sort.sorted(data, key=abs, reverse=True)
print("\nsorted(data, key=abs, reverse=True):", result)
result_with_lambda = sort.sorted(data, key=lambda x: abs(x), reverse=True)
print("sorted(data, key=lambda x: abs(x), reverse=True):", result_with_lambda)

# Тесты для print_result.py
print("\n--- print_result.py tests ---")


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


test_1()
test_2()
test_3()
test_4()

# Тесты для cm_timer.py
print("\n--- cm_timer.py tests ---")
print("cm_timer_1:")
with cm_timer.cm_timer_1():
    sleep(1.5)

print("\ncm_timer_2:")
with cm_timer.cm_timer_2():
    sleep(0.5)

print("\n--- process_data.py tests ---")
data_file = "data_light.json"

if not os.path.exists(data_file):
    print(f"Error: data_light.json not found. Please create it in the same directory.")
    sys.exit(1)

try:
    with open(data_file, encoding="utf-8") as f:
        data = json.load(f)
    with cm_timer.cm_timer_1():
        f4(f3(f2(f1(data))))
except json.JSONDecodeError:
    print("Error: Invalid JSON data in data_light.json")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
