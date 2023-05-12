def sum(n):   
  s=0
  while n>0:
    r=n%10
    s=s+r
    n=n//10
  return s

def rev(n):   
  s=0
  i=1
  while n>0:
    r=n%10
    s=s*10+r
    n=n//10
  return s

def diff_pro(n): 
  p=1
  o=1
  e=1
  while n>0:
    r=n%10
    if p%2==0:  
      e=e*r
    else:
      o=o*r
    p=p+1
    n=n//10
  c=(o-e)*-1
  return c

z=int(input("Enter the four digit number:"))  
print("sum of digits of number:",sum(z))
print("Reverse of the given number is:",rev(z))                        
print("Difference between number based on position is:",diff_pro(z))   
