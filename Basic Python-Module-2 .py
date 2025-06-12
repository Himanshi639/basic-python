#!/usr/bin/env python
# coding: utf-8

# # Task1
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
# In[26]:


a= input("enter the first number:")
b= input("enter the second number:")
Addition= int(a) + int(b)
Subtraction= int(a) -int(b)
Multiplication = int(a) * int(b)
Division = float(a)/ float(b)


print("Addition:", Addition)
print("Subtraction", Subtraction)
print("Multiplocation:",  Multiplication)
print("Division:" , Division)


# # Task 2
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.

# In[30]:


first= input("Enter the first name:")
last= input("enter the last name:")


# In[33]:


print("Hello,", first + last+'!' ,"Welcome to the Python Program" )   # + concatenation happens


# In[ ]:




