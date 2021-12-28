#!/usr/bin/env python
# coding: utf-8

# In[1]:

# importing required python libraries
import numpy as np
import matplotlib
from matplotlib import pyplot as plt


# In[2]:

# It loads a data from dataset into file_name.
file_name = np.genfromtxt(r"C:\Users\dksin\Dropbox\My PC (LAPTOP-E383CH2K)\Desktop\heart.CSV", delimiter=',', skip_header=True, dtype=int)


# In[3]:

# It retrieves whole dataset values.
print(file_name)


# In[4]:

# It gives min age group with heart stroke.
min_age= np.min(file_name[:,0])
print("min age group with heart attack", min_age)


# In[5]:

# It gives max age group with heart stroke.
max_age= np.max(file_name[:,0])
print("max age group with heart attack in this dataset", max_age)


# In[6]:

# Vertical bar graph for Age Vs Cholestrol.
age=file_name[:,0]
cholestrol=file_name[:,4]
plt.title("Age vs Cholestrol", color="blue")
plt.xlabel("Age", color="red")
plt.ylabel("Cholestrol", color="red")
plt.bar(age, cholestrol, color='green')
plt.show()


# In[7]:

# Finding which age groups are often tested to electro cardiographic testing using Horizantal bar chart.
age = file_name[:,0]
cardiographic_res = file_name[:,6]
plt.title("Age vs Electro_Cardiographic_testing")
plt.xlabel("cardiographic_result", color="blue")
plt.ylabel("age", color="red")
colors=['red','blue','lime','black','pink','orange','green']
plt.barh(age, cardiographic_res, color=colors)
plt.show()


# In[8]:

# Finding frequency of chest pains as per age groups using scatter plot.
chest_pain = file_name[:,2]
Gender = file_name[:,0]     
plt.title("Chest_pain vs Age")
plt.scatter(chest_pain, Gender)
plt.xlabel("Frequency of chest pain as per age", color="green")
plt.ylabel("Age", color="green")
plt.show()


# In[9]:

# Finding average cholestrol level, mean and Standard Deviation of resting Blood Pressure for all age groups in combined. 
avg_chol=np.average(file_name[:,4])
chol=file_name[:,4]
resting_BP=file_name[:,3]
Gender=file_name[:,1]
mean_resting_BP=np.mean(file_name[:,3])
SD = np.std(file_name[:,3])
print("avg_chol:   ",avg_chol)
print("mean_resting_BP:   ",mean_resting_BP)
print("Standard_Deviation_resting_BP:   ",SD)





# In[10]:

# Multi plot line graph for cholestrol, age and age, resting Blood Pressure

Age=file_name[:,0]
plt.plot(chol, Age)
plt.plot(Age, resting_BP)

