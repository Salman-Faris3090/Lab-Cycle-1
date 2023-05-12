def substring(s):                              
  print("\nSubstrings","\n",s)
  for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
       print(s[i:j])    
  print()


def lengthsubstring(s,k):
   print("Substrings of length :",k,"\n",end="")
   for i in range(len(s)+1):
    for j in range(len(s)+1): 
        if len(s[i:j])==k:
            print(s[i:j],end=" ")


def substringdistinct(s,k,n):            
   print("Substrings of length ",k," with ",n,end="")
   print(" distinct characters\n",end="")
   count=0
   for i in range(len(s)+1):
    for j in range(len(s)+1):
        if len(s[i:j])==k:
           sets=set(s[i:j])              
           if len(sets)==n:
             print(s[i:j],end=" ")
             count=1
   if count==0:
      print("There is no substrings with ",n," distinct characters in ",end=" ")
      print(k,"length substring")
   print()

   
def substringmaxlength(s,n):
   count=0
   temp2=0
   string=[]
   for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):            
      if len(set(s[i:j]))==n:
        string.append(s[i:j])
   for i in range(len(string)):
     if(len(string[i])>len(string[-1])):
         print(string[i],end=" ")
         count=1                
   if count==0:
      print("There is no substrings with ",n," distinct characters ",end="")
      print("with max length substring")
   print()

   
def palindrome(s):
    st=str(input("Enter The String: "))
    j = -1
    flag = 0 
    for i in st:
        if i != st[j]:
            flag = 1
            break
        j = j - 1
    if flag == 1:
        print("The String is not a Palindrome")
    else:
        print("The Palindrome String is: ",st)


def call():
  string=str(input("Enter the String:"))
  substring(string)
  length=int(input("\nEnter the length:"))
  lengthsubstring(string,length)
  terms=int(input("\n\nEnter the number of distinct characters:"))      
  substringdistinct(string,length,terms)
  print("\nSubstring of length maximum with ",terms," distinct characters\n",end="")
  substringmaxlength(string,terms)
  palindrome(string)
call()

