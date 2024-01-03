#fibonacci series in python
def fibonacci(n):
         if n==0:
                  return []
         elif n==1:
                  return [0]
         elif n==2:
                  return [0,1]
         else:
                  a=[0,1]
                  for i in range(2,n):
                           a.append(a[-1]+a[-2])

                  return a


print(fibonacci(int(input())))
