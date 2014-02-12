#!/usr/bin/env python
import time
import math

#Problem 21

start_time = time.time()

x = range(1,10000)
solution_dictionary = {}
amicable_numbers =[]

for number in x:
  factors = []
  max = number/2
  for each in range(1,max+1):
    if number % each == 0:
      factors.append(each)
  solution_dictionary[number] = sum(factors)

for key in solution_dictionary:
  factor_sum = solution_dictionary[key]
  try:
    new_key = solution_dictionary[factor_sum]
    if new_key == key and key < 10000 and factor_sum != key:
        amicable_numbers.append(key)
  except: continue

print sum(amicable_numbers)

end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))
