#factorial of a given number in python

def factorial(n):
         if n==0:
                  return 1
         else:
                  return n*factorial(n-1)
#recursion technique:- where function class itself to solve a problem.
         


print(factorial(int(input())))

