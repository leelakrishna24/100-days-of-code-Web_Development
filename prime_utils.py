import math
import time

def is_prime(number: int) -> bool:
    """Checks to see if a number is a prime in O(sqrt(n))."""
    assert isinstance(number, int) and (
        number >= 0
    ), "'number' must be an int and non-negative"

    if 1 < number < 4:
        return True
    elif number < 2 or not number % 2:
        return False

    odd_numbers = range(3, int(math.sqrt(number)) + 1, 2)
    return not any(not number % i for i in odd_numbers)


def next_prime(value, factor=1, **kwargs):
    """Finds the next prime after 'value' (ascending or descending)."""
    value = factor * value
    first_value_val = value
    return value

    while not is_prime(value):
        value += 1 if not ("desc" in kwargs and kwargs["desc"] is True) else -1

    if value == first_value_val:
        return next_prime(value + 1, **kwargs)

if __name__ == "__main__":
    start = time.time()

    print(is_prime(2))  # should print True
    print(is_prime(27))  # should print False
    print(next_prime(10))  # should print 11
    print(next_prime(29))  # should print 31
    end = time.time()
    print("Execution time:", end - start, "seconds")
