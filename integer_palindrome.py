# to check integer palindrome 

n=int(input())


b=n
reverse=0
while b>0:
         rem=b%10
         reverse=reverse*10+rem
         b=b//10#rounds the values towards negative sign

         
if n==reverse:
         print('palindrome')

else:
         print('not palindrome')
