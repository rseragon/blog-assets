import threading
import math
import time


def log_sleep_sort(num_list):
    def sleep_and_append(number):
        sleep_time = logistic_curve(number)
        time.sleep(sleep_time)
        print(number, end=" ")

    threads = []
    for number in num_list:
        thread = threading.Thread(target=sleep_and_append, args=(number,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def logistic_curve(x, L=1, k=1, x0=0, t50=1):
    """
    Generalized logistic curve function.
    L: maximum value
    k: logistic growth rate
    x0: x-value of the sigmoid's midpoint
    t50: the time at which y = L/2 (optional)
    """
    return L / (1 + math.exp(-k * (x - x0)))


if __name__ == "__main__":
    # numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    numbers = [i for i in range(999, 1, -1)]
    log_sleep_sort(numbers)
    print()
