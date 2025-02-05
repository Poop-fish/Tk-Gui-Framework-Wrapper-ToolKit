
#!------ Enumerate iterable -----------

def GTGenumerate(iterable):
    index = 0
    for item in iterable:
        yield index, item
        index += 1
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# for i, day in GTGenumerate(days):
#     print(f"Index: {i}, Day: {day}")

#!------ Range Generator iterable ----------- 

def GTG_range(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step

# for num in GTG_range(0, 10, 2):
#     print(num)  # Output: 0, 2, 4, 6, 8


#!------ Fibonacci Sequence Generator iterable ----------- 

def GTG_fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# for num in GTG_fibonacci(50):
#     print(num)  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

#!------Prime Number Generator iterable ----------- 

def GTG_primes(limit):
    primes = []
    for num in GTG_range(2, limit):
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
            yield num

# for prime in GTG_primes(30):
#     print(prime)  # Output: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 

#!------  Cartesian Product Generator iterable ----------- 
from itertools import product
def GTG_cartesian_product(*iterables):
    for combination in product(*iterables):
        yield combination

# for combo in GTG_cartesian_product([1, 2], ['A', 'B']):
#     print(combo)  # Output: (1, 'A'), (1, 'B'), (2, 'A'), (2, 'B') 


#!------  Even Numbers Generator iterable ----------- 

def GTG_even_numbers(start, stop):
    for num in GTG_range(start, stop):
        if num % 2 == 0:
            yield num

# for num in GTG_even_numbers(0, 10):
#     print(num)  # Output: 0, 2, 4, 6, 8

#!------  Custom String Generator iterable ----------- 

def GTG_string(s):
    for char in s:
        yield char

# for char in GTG_string("poop"):
#     print(char)  # Output: p, o, o, p


#!------  Countdown Generator iterable ----------- 

def GTG_countdown(start):
    while start >= 0:
        yield start
        start -= 1

# for num in GTG_countdown(25):
#     print(num)  # Output: 5, 4, 3, 2, 1, 0

#!------  Shuffling Generator iterable ----------- 

import random 
def GTG_shuffle(iterable):
    shuffled = list(iterable)
    random.shuffle(shuffled)
    for item in shuffled:
        yield item

# for item in GTG_shuffle([1, 2, 3, 4, 5]):
#     print(item)  # Output will be shuffled every time you run it


#!------ Repeating Values Generator iterable ----------- 

def GTG_repeat(value, times):
    for _ in range(times):
        yield value

# for value in GTG_repeat("hello", 8):
#     print(value)  # Output: hello, hello, hello



#!------ Square Numbers Generator iterable ----------- 

def GTG_squares(limit):
    for num in range(limit):
        yield num ** 2

# for num in GTG_squares(10):
#     print(num)  # Output: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81


#!------ Infinite Counter Generator iterable ----------- 

def GTG_infinite_counter(start=0, step=1):
    while True:
        yield start
        start += step

# counter = GTG_infinite_counter(5, 2)
# for _ in range(10):
#     print(next(counter))  # Output: 5, 7, 9, 11, 13, ...


#!------ Unique Permutations Generator iterable ----------- 
from itertools import permutations

def GTG_permutations(iterable):
    for perm in permutations(iterable):
        yield perm

# for perm in GTG_permutations("abc"):
#     print(perm)  # Output: ('a', 'b', 'c'), ('a', 'c', 'b'), ...


#!------ Triangle Numbers Generator iterable ----------- 

def GTG_triangle_numbers(limit):
    num = 1
    total = 0
    while num <= limit:
        total += num
        yield total
        num += 1

# for num in GTG_triangle_numbers(10):
#     print(num)  # Output: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55


#!------ Collatz Sequence Generator iterable ----------- 

def GTG_collatz(n):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield 1

# for num in GTG_collatz(7):
#     print(num)  # Output: 7, 22, 11, 34, 17, 52, 26, 13, 40, ...


#!------ Powers of Two Generator iterable ----------- 

def GTG_powers_of_two(limit):
    num = 1
    while num <= limit:
        yield num
        num *= 2

# for num in GTG_powers_of_two(100):
#     print(num)  # Output: 1, 2, 4, 8, 16, 32, 64


#!------ Reverse Iterable Generator ----------- 

def GTG_reverse(iterable):
    for item in reversed(iterable):
        yield item

# for num in GTG_reverse([1, 2, 3, 4, 5]):
#     print(num)  # Output: 5, 4, 3, 2, 1


#!------ Yielding Digits of a Number ----------- 

def GTG_digits(n):
    for digit in str(n):
        yield int(digit)

# for digit in GTG_digits(12345):
#     print(digit)  # Output: 1, 2, 3, 4, 5


#!------ Yielding Factorial Numbers ----------- 

def GTG_factorial(limit):
    fact = 1
    for num in range(1, limit + 1):
        fact *= num
        yield fact

# for num in GTG_factorial(10):
#     print(num)  # Output: 1, 2, 6, 24, 120, 720, ...


#!------ Infinite Alternating Sign Generator ----------- 

def GTG_alternating_sign():
    num = 1
    while True:
        yield num
        yield -num
        num += 1

# alternator = GTG_alternating_sign()
# for _ in range(10):
#     print(next(alternator))  # Output: 1, -1, 2, -2, 3, -3, ...



