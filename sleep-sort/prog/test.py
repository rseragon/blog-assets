import threading
import math
import time


def sleep_sort(num_list):
    sorted_list = []

    def sleep_and_append(number):
        sleep_time = logistic_curve(number, L=5, k=0.1, x0=500, t50=200)
        time.sleep(sleep_time)
        sorted_list.append(number)

    threads = []
    for number in num_list:
        thread = threading.Thread(target=sleep_and_append, args=(number,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sorted_list


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
    numbers = list(range(999, 0, -1))
    sorted_numbers = sleep_sort(numbers)
    print("Sorted numbers:", sorted_numbers)
