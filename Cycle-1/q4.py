def check_happy(num):                                    
  for i in range (1,101):
    sum=0
    while num>0:
     r=num%10
     num=num//10
     sum=sum+(r*r)
    if sum==1:
      return True
    else:
      num=sum
      if(i==100):
        return False


def happy_range(lowlimit,upprlimit):                     
  for i in range(lowlimit,upprlimit):
    isHappy=check_happy(i)
    if isHappy:
      print(i,end=" ")

def printnumbers(n):
   count=1                           
                                    
   i=1
   while count<=n:
     total=check_happy(i)                 
     if total==1:                   
        print(i,end=" ")
        count+=1
     i=i+1
   print('') 


  
num = int(input("Enter the number : "))
result = check_happy(num)                              
if result:
  print(num,"Is a Happy Number")
else:
  print(num,"Is a Sad Number")

lower_limit=int(input("\nEnter the lower limit:"))
upper_limit=int(input("Enter the upper limit:"))
print("The Happy Numbers Within the given Range are:")
happy_range(lower_limit,upper_limit)
n=int(input("\n\nEnter how many Happy Numbers you want to print : "))
printnumbers(n)


                                     
