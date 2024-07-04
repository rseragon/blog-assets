#!/usr/bin/env python3
from asyncio import Future, run, sleep, wait, Task
from sys import argv
import math


async def f(n, t):
    await sleep(t)
    print(n)


def my_func(n, max):
    return math.sqrt(n) / max


async def runner():
    # numbers = [int(i) for i in argv[1:]]
    numbers = [1, 100, 231, 444, 555, 766]

    print(numbers)
    maximum = max(numbers)
    reduced_numbers = [my_func(i, maximum) for i in numbers]
    print(reduced_numbers)
    tasks = [Task(f(n, t)) for n, t in zip(numbers, reduced_numbers)]
    await wait(tasks)


if __name__ == "__main__":
    run(runner())
