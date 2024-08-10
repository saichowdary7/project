n=int(input('Enter a Number '))
a=n%10
n=n//10
b=n%10
n=n//10
c=n%10
d=n//10

if d>c and d>b and d>a:
  print(d,'is big')
elif c>b and c>a:
  print(c,'is big')
elif b>a:
  print(b,'is big')
else:
  print(a,'is big')        

