#!/usr/bin/env python
import time
import math

# Problem 10
start_time = time.time()

all_numbers = range(3,2000001,2)
primes_sum = 2

def prime_checker(n):
  max = int(math.sqrt(n)+1)
  for number in range(3,max,2):
    if n % number == 0: return 0
  return 1

for each in all_numbers:
  if prime_checker(each) == 1:
    primes_sum += each

end_time = time.time()
print end_time - start_time
print primes_sum
