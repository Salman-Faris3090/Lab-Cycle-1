def triangle_sides():                        
  a=float(input("Enter First side:"))
  b=float(input("Enter Second side:"))
  c=float(input("Enter Third side:"))
  
  return a,b,c

def triangle_area(a,b,c):                    
  import math
  s=(a+b+c)/2
  area=math.sqrt(s*(s-a)*(s-b)*(s-c))
  return area

def totalarea_contribution(area1,area2):     
  Total_Area=(area1+area2)
  Contribution1=(area1*100)/Total_Area
  Contribution2=(area2*100)/Total_Area
  print("\nTotal Area of Triangles:",Total_Area)
  print("Contribution of First Triangle is:",Contribution1,"%")
  print("Contribution of Second Triangle is:",Contribution2,"%")
  
print("*******Triangle 1*******")
a1,b1,c1=triangle_sides()                        
area1=triangle_area(a1,b1,c1)
print("The Area of Triangle 1 is:",area1)


print("\n*******Triangle 2*******")
a2,b2,c2=triangle_sides()                        
area2=triangle_area(a2,b2,c2)
print("The Area of Triangle 2 is:",area2)

totalarea_contribution(area1,area2)              
