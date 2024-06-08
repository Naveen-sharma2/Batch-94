#!/usr/bin/env python
# coding: utf-8

# In[1]:


#### Excercise 1 ####

# Python code to demonstrate string length 
# using len

str = "Tutor Joes"
print(len(str))


# In[6]:


#### Excercise 2 ####

# Define a function named char_frequency that takes one argument, str1.
def char_frequency(str1):
    
    # Initialize an empty dictionary named 'dict' to store character frequencies.
    dict = {}
    
    # Iterate through each character 'n' in the input string str1.
    for n in str1:
        # Retrieve the keys (unique characters) in the 'dict' dictionary.
        keys = dict.keys()
        
        # Check if the character 'n' is already a key in the dictionary.
        if n in keys:
            # If 'n' is already a key, increment its value (frequency) by 1.
            dict[n] += 1
        else:
            # If 'n' is not a key, add it to the dictionary with a frequency of 1.
            dict[n] = 1
    
    # Return the dictionary containing the frequency of each character in the input string.
    return dict

# Call the char_frequency function with the argument 'tutorjoes' and print the result.
print(char_frequency('tutorJoes'))


# In[10]:


#### Excercise 3 ####

str="tutor joes"
print("Given String :",str)
ch = str[0]
str = str.replace(ch, '@')
str = ch + str[1:]
print("After String :",str)


# In[9]:


#### Excercise 4 ####

a = 'abc'
b = 'xyz'
print("Before Swap :",a," ",b)
a1 = b[:2] + a[2:]
b1 = a[:2] + b[2:]
print("After Swap :",a1," ",b1)


# In[11]:


#### Excercise 5 ####

def remove_char(str, n):
      a = str[:n] 
      b = str[n+1:]
      return a + b
print(remove_char('Tutor Joes', 2))
print(remove_char('Tutor Joes', 7))


# In[15]:


#### Excercise 6 ####

"""
str = "Python"
print("Before Swap :",str)
res = str[-1:] + str[1:-1] + str[:1]
print("After Swap :",res)
"""
str = "Python"
print("Before Swap :",str)
s = str[0]
e = str[-1]
res = e + str[1:-1] + s
print("After Swap :",res)


# In[46]:


#### Excercise 7 ####

str="Computer Education"
res = ""
print("Original String :",str) 
for i in range(len(str)):
    if i % 2 == 0:
     res = res + str[i]
print("Remove Odd Index Char :",res)


# In[44]:


#### Excercise 8 ####

str = "To change the overall look your document. To change the look available in the gallery"
c = dict()
txt = str.split(" ")
for t in txt:
    if t in c:
        c[t] += 1
    else:
        c[t] = 1
print(c)


# In[47]:


#### Excercise 9 ####

str = input("Enter the String :")
print("Given String :",str)
print("UpperCase :"+ str.upper())
print("LowerCase :"+ str.lower())


# In[54]:


#### Excercise 10 ####

str=input("Enter the String :")
if len(str) % 4 == 0:
   print(''.join(reversed(str)))
else:
    print(str)


# In[57]:


#### Excercise 11 ####

str = input("Enter the String :")
num_upper = 0
for letter in str[:4]: 
    if letter.upper() == letter:
    num_upper += 1
if num_upper >= 2:
    print(str.upper())
print(str)

