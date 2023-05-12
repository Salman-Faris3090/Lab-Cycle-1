def gross_salary(bp,da,hra,ma):                             
  Gross_salary=bp+da+hra+ma                                                                       
  return Gross_salary                                                                             
                                                                                                  
                                                               
def deduction(pt,pf,it):                                                                          
  Deduction=pt+pf+it                                                                              
  return Deduction                                                                                
                                                                                                  
                                                                                                  
def net_salary(gs,d):                     
  NetSalary=gs-d
  return NetSalary


def pay_slip(name,code,basicPay):         
  if basicPay<10000:
    DA=(basicPay*5)/100
    HRA=(basicPay*2.5)/100
    MA=500
    PT=20
    PF=(basicPay*8)/100
    IT=0
    Gross_salary=gross_salary(basicPay,DA,HRA,MA)
    Deduction=deduction(PT,PF,IT)
    NetSalary=net_salary(Gross_salary,Deduction)


  elif basicPay>10000 and basicPay<30000:
    DA=(basicPay*7.5)/100
    HRA=(basicPay*5)/100
    MA=2500
    PT=60
    PF=(basicPay*8)/100
    IT=0
    Gross_salary=gross_salary(basicPay,DA,HRA,MA)
    Deduction=deduction(PT,PF,IT)
    NetSalary=net_salary(Gross_salary,Deduction)


  elif basicPay>30000 and basicPay<50000:
    DA=(basicPay*11)/100
    HRA=(basicPay*7.5)/100
    MA=5000
    PT=60
    PF=(basicPay*11)/100
    IT=(basicPay*11)/100
    Gross_salary=gross_salary(basicPay,DA,HRA,MA)
    Deduction=deduction(PT,PF,IT)
    NetSalary=net_salary(Gross_salary,Deduction)


  else:
    DA=(basicPay*25)/100
    HRA=(basicPay*11)/100
    MA=7000
    PT=80
    PF=(basicPay*12)/100
    IT=(basicPay*20)/100
    Gross_salary=gross_salary(basicPay,DA,HRA,MA)
    Deduction=deduction(PT,PF,IT)
    NetSalary=net_salary(Gross_salary,Deduction)


  print("\n*** PAYMENT SLIP ***")
  print("Employee name:",name)
  print("Employee code:",code)
  print("Employee basic pay:",basicPay)
  print("Employee DA:",DA)
  print("Employee HRA:",HRA)
  print("Employee MA:",MA)
  print("Employee PT:",PT)
  print("Employee PF:",PF)
  print("Employee IT:",IT)
  print("Employee Gross salary:",Gross_salary)
  print("Employee Deduction:",Deduction)
  print("Employee Net Salary:",NetSalary)



Name=input("Enter Employee Name:")
Code=int(input("Enter Employee code:"))
basicPay=int(input("Enter Employee basic pay:"))
pay_slip(Name,Code,basicPay)               
