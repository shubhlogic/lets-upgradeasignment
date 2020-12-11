#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # assignments 3

# Use IF ELSE and ELIF to write a program in python for your Report Cards.
# 

# In[10]:


a=22
b=22
if a>b:
    print(f'{a} is greater no')
elif b>a:
    print(f'{b} is greater no')
else:
    print('both r same')
    


# Use For Loop to Print Prime Numbers in between 1 to 1000

# In[38]:



for i in range(1,1000):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)


# Write a program for printing the tables from 1,10 using Nested For Loop

# In[43]:


for num1 in range(1, 11):
    for num2 in range(1,11):
        print(num1*num2,end=' ')
    print('\n')
       


# Write a program to Print X Prime Numbers using While Loop starting from 0, and take the INput of X from
# the user

# In[47]:


no=int(input('Enter no'))
i=2
flag=0
while i<no:
    if no%i==0:
        flag=flag+1
    i=i+1
if flag == 0:
    print("Your number is a prime number!");


# In[ ]:





# In[ ]:




