n=int(input())

rev=0
temp=n
order=len(str(n))
while temp>0:
         rem=temp%10
         rev+=rem**order
         temp=temp//10


if n==rev:
         print('armstrong number')

else:
         print('not armstrong')
