n=int(input('enter a number to check for prime number'))

if n<=1:
         print('not prime number')

else:
         a=True
         for i in range(2,n):
                  if n%i==0:
                           a=False
                           break

         if a:
                  print('prime number')

         else:
                  print('not a prime number')
         





























