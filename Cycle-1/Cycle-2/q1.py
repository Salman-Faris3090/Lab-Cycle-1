def rabbit_pairs(n):
  x=0
  y=1
  z=0
  print("\nMonths\t|\tNo.of pairs of Rabbits")
  for i in range(1,n+1):
    if (i==1):
      print(i,"\t|\t",y)
    else:
      z=x+y
      x=y
      y=z
      print(i,"\t|\t",z)
n=int(input("Enter the number of months: "))
rabbit_pairs(n)