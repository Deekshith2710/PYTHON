def prime_factors(n):

         i=2
         l=[]
         while n>1:
                  while n%i==0:
                           l.append(i)
                           n//=i

                  i+=1

         return l
print(prime_factors(int(input())))
         
