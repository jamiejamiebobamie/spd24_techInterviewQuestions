# this problem is from project Euler
# https://projecteuler.net/problem=25

# The Fibonacci sequence is defined by the recurrence relation:

#   Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

### PROBLEM STATEMENT ###

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


## Understand:
# input: None
# output: (int) index that fits criteria

## Match:
# Repetitve addition, recursive?

## Plan:

## to get the fib sequence
## start with 0 and 1
## add the last two terms to get the third term
## test how many digits the current term has - if over 1000, return the index of that term
## repeat

## Then, translate to code!

# O(n**2) time complexity
# O(1) space complexity
def fibonacci_1000():
  # 1,1,2,3,5...
  def fib(a,b):
    return a+b
  count = 2 # starting index is 2.
  answer = 1 
  a = 1 # first element
  b = 1 # second element
  while len(str(answer)) < 1000:
      a = b
      b = answer
      answer = fib(a,b)
      count+=1

  return count

print(fibonacci_1000())

# fibonacci(1) = 1
# fibonacci(2) = 1
# fibonacci(3) = 2
# fibonacci(4) = 3
# fibonacci(5) = 5
# fibonacci(6) = 8
# fibonacci(7) = 13
# fibonacci(8) = 21
# fibonacci(9) = 34
# fibonacci(10) = 55
# fibonacci(11) = 89
# fibonacci(12) = 144
