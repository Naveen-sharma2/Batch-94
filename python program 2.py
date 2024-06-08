#!/usr/bin/env python
# coding: utf-8

# In[3]:


#### ex-5 ####

l = int(input("Enter the Limit :"))
even=[]
odd=[]
for i in range(l):
    n = int(input("Enter the Values :"))
    if(n%2==0):
    even.append(n)
    else:
        odd.append(n)
print("Number of Even :",len(even))
print("Number of Odd :",len(odd))


# In[4]:


#### ex-6 ####

num = int(input("Enter the Number :"))
a=num
sum=0
while(num>0):
    rem=num%10
    sum=(sum*10)+rem
    num=num//10
print("Before Number :",a)
print("Reverse Number :",sum)


# In[5]:


#### ex-7 ####

"""
num = input("Enter the Binary Number :")
dec_number= int(num, 2)
print('The binary Number :', num)
print('The decimal Number :', dec_number)
"""
binary = input("Enter the Binary Number :")
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print('The binary Number :', binary)
print('The decimal Number :', decimal)


# In[6]:


#### ex-8 ####

"""
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end ="")
 
decimal = int(input("Enter the Decimal Number :"))
convertToBinary(decimal)
 
 
"""
decimal = int(input("Enter the Decimal Number :"))
binary = 0
ctr = 0
temp = decimal
while(temp > 0):
    binary = ((temp%2)*(10**ctr)) + binary
    temp = int(temp/2)
    ctr += 1
print("Decimal Number :",decimal)
print("Binary Number :",binary)


# In[7]:


#### ex-9 ####

f = int(input("Enter the Number :"))
fact = 1    
if(f< 0):    
   print("Factorial does not exist Negative Values")    
elif(f== 0):    
   print("The Factorial of 0 is 1")    
else:    
   for i in range(1,f + 1):    
       fact = fact*i    
   print("The Factorial",f,"is :",fact)


# In[8]:


#### ex-10 ####

n = int(input("Enter the Number :"))
n1, n2 = 0, 1
sum = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":",n1)
else:
   print("Fibonacci sequence:")
   while sum < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       sum += 1


# In[9]:


#### ex-11 ####

num = int(input("Enter the Number :"))
for i in range(1, num):
       if num % i == 0:
           print(i)


# In[10]:


#### ex-12 ####

num = 1000
for i in range(1, num):
       if num % i == 0:
           print(i)


# In[11]:


#### ex-13 ####

num = int(input("Enter the Number :"))
a=num
sum=0
while (num>0):
    rem=num%10;
    fact=1;
    for i in range(1,rem+1):
    fact=fact*i
    sum=sum+fact;
    num=num//10;
if (sum == a):
    print(a,"is Strong Number");
else:
    print(a ,"is not a Strong Number");


# In[12]:


#### ex-14 ####

base = int(input("Enter the Base Number :"))
pow = int(input("Enter the Power Number :"))
#res=(base**pow)
#print("Answer :",res)
res = 1
while pow != 0:
    res *= base
    pow-=1
 
print("Answer :",res)


# In[ ]:


#### ex-11 ####


