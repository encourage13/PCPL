import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print(f"time: {end - self.start}")


@contextmanager
def cm_timer_2():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"time: {end - start}")


from time import sleep

with cm_timer_1():
    sleep(5.5)

with cm_timer_2():
    sleep(2.2)
