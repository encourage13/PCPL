import json
from unique import Unique
from print_result import print_result
import cm_timer
from gen_random import gen_random
import random


@print_result
def f1(arg):
    return sorted(list(Unique(map(lambda x: x['job-name'].lower(), arg), ignore_case=True)))


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    if not arg:
        return []
    salaries = list(gen_random(len(arg), 100000, 200000))
    result = [f"{specialty}, зарплата {salary} руб" for specialty, salary in zip(arg, salaries)]
    return result
