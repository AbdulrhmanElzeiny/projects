#!/usr/bin/env python
# coding: utf-8

# > **Tip**: Welcome to the Investigate a Dataset project! You will find tips in quoted sections like this to help organize your approach to your investigation. Once you complete this project, remove these **Tip** sections from your report before submission. First things first, you might want to double-click this Markdown cell and change the title so that it reflects your dataset and investigation.
# 
# # Project: Investigate a Dataset - [No Show appointements]
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# >This dataset collects information
# from 100k medical appointments in
# Brazil and is focused on the question
# of whether or not patients show up
# for their appointment. A number of
# characteristics about the patient are
# included in each row.
# 
# >● ‘ScheduledDay’ tells us on
# what day the patient set up their
# appointment. 
# 
# >● ‘Neighborhood’ indicates the
# location of the hospital.
# 
# >● ‘Scholarship’ indicates
# whether or not the patient is
# enrolled in Brasilian welfare
# program Bolsa Família.
# 
# >● Be careful about the encoding
# of the last column: it says ‘No’ if
# the patient showed up to their
# appointment, and ‘Yes’ if they
# did not show up.
# 
# 
# ### Question(s) for Analysis
# >**Tip**: Clearly state one or more questions that you plan on exploring over the course of the report. You will address these questions in the **data analysis** and **conclusion** sections. Try to build your report around the analysis of at least one dependent variable and three independent variables. If you're not sure what questions to ask, then make sure you familiarize yourself with the dataset, its variables and the dataset context for ideas of what to explore.
# 
# > **Tip**: Once you start coding, use NumPy arrays, Pandas Series, and DataFrames where appropriate rather than Python lists and dictionaries. Also, **use good coding practices**, such as, define and use functions to avoid repetitive code. Use appropriate comments within the code cells, explanation in the mark-down cells, and meaningful variable names. 

# In[2]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.

# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')



# <a id='wrangling'></a>
# ## Data Wrangling
# 
# > **Tip**: In this section of the report, you will load in the data, check for cleanliness, and then trim and clean your dataset for analysis. Make sure that you **document your data cleaning steps in mark-down cells precisely and justify your cleaning decisions.**
# 
# 
# ### General Properties
# > **Tip**: You should _not_ perform too many operations in each cell. Create cells freely to explore your data. One option that you can take with this project is to do a lot of explorations in an initial notebook. These don't have to be organized, but make sure you use enough comments to understand the purpose of each code cell. Then, after you're done with your analysis, create a duplicate notebook where you will trim the excess and organize your steps so that you have a flowing, cohesive report.

# In[3]:


# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.
#lets load our data and explor it
df=pd.read_csv('noshowappointments-kagglev2-may-2016.csv')
df.head()


# >incorrect spell Hypertension and we need to replace no-show too .

# In[4]:


#how many rows that data have  
df.shape


# In[5]:


#wow its a big data , lets to see if it have dup;icated info 
df.duplicated().sum()


# In[6]:


#nice no duplicate , what about missing value 
df.info()


# In[7]:


#greet no missing value , what about dscribe
df.describe()


# > min Age = -1 and that is no wright , i will remove it .
# most of pepole not suffer from desase and that is good . 
# 
# 

# In[8]:


#finaly lets see unique value 
df.nunique()


# >umm we have 62299 ID as a unique if we subscrat from AppointmentID 110527 so we have 48228 duplicate for ID

# 
# ### Data Cleaning
# > **Tip**: Make sure that you keep your reader informed on the steps that you are taking in your investigation. Follow every code cell, or every set of related code cells, with a markdown cell to describe to the reader what was found in the preceding cell(s). Try to make it so that the reader can then understand what they will be seeing in the following cell(s).
#  

# In[9]:


#lets clean our data , at frist lets to remove unnessery data 
df.drop(['PatientId','AppointmentID','ScheduledDay','AppointmentDay'] , axis=1,inplace=True)


# In[10]:


#check it 
df.head()


# In[11]:


#now lets rename a coloumn and correct spell 
df.rename(columns={'Hipertension':'Hypertension'}, inplace=True)
df.rename(columns={'No-show':'No_show'}, inplace=True)
df.head()


# In[12]:


#nice , now lets fix Age=-1 at frist how much rows have this error?
erorr=df.query('Age==-1')
erorr


# In[13]:


#only one , lets remove it . my data no affect by remove
df.drop(index=99832 , inplace=True)


# In[14]:


#lets check now 
df.describe()


# >now we have a clean data ^_^

# In[15]:


df.head()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > **Tip**: Now that you've trimmed and cleaned your data, you're ready to move on to exploration. **Compute statistics** and **create visualizations** with the goal of addressing the research questions that you posed in the Introduction section. You should compute the relevant statistics throughout the analysis when an inference is made about the data. Note that at least two or more kinds of plots should be created as part of the exploration, and you must  compare and show trends in the varied visualizations. 
# 
# 
# 
# > **Tip**: - Investigate the stated question(s) from multiple angles. It is recommended that you be systematic with your approach. Look at one variable at a time, and then follow it up by looking at relationships between variables. You should explore at least three variables in relation to the primary question. This can be an exploratory relationship between three variables of interest, or looking at how two independent variables relate to a single dependent variable of interest. Lastly, you  should perform both single-variable (1d) and multiple-variable (2d) explorations.
# 
# 
# 

# In[16]:


# lets take a genral look .
df.hist(figsize=(18,8));


# * parents taking care about their children as number of young pepole is more than number of old , as we see number of patient decrase while pepole get elder .
# 
# * number of pepole who receive sms is half number of pepole who didnt.
# 
# * most of pepole didnt suffer from chronic disease and handcap but pepole suffer from hypertension more than diabetes.

# ### Research Question 1 (dose attendace affected by age ? )

# In[17]:


#we need to split No_show column to show and notshow
show = df.No_show == 'No'
notshow = df.No_show == 'Yes'


# In[18]:


df[show].count() , df[notshow].count() 


# In[19]:


#now lets answer 
df.Age[show].value_counts() 


# *it see by age increase attendance decrase 

# In[20]:


#let visluze it and compere between showed and age
plt.figure(figsize=(15,5))
df.Age[show].hist(alpha=.5,bins=10, label='Show')
df.Age[notshow].hist(alpha=.5, bins=10,label='Not Show')
plt.legend()
plt.title('Age affect attendance and compere bt Show or not')
plt.xlabel('Age')
plt.ylabel('Patiant nm');


# 
# 
# * as we see Age from 0 to 10 are the most showing , then from 45 to 55 , then decrase till the last.
# 
# >parents taking care about their children as number of young pepole is more than number of old , number of patient decrase while pepole get elder . 

# ### Research Question 2  (Dose attendance affect by gender ?)

# In[21]:


#lets answer frist and then visulaize our answer
df.Gender[show].value_counts(),df.Gender[notshow].value_counts()


# In[22]:


#showed by gender
def attandance (df,col_name,attended,abesnt):
    plt.figure(figsize=[10,5])
    df[col_name][show].value_counts(normalize=True).plot(kind='pie' , label= 'Show')
    plt.legend()
    plt.title('compere between Gender to attendance ')
    plt.xlabel('Gender')
    plt.ylabel('Patiant nm');
attandance (df ,'Gender' ,show ,notshow)


# * number of female patient showed more than number of men showed by about 75%

# In[23]:


#notshowed by gender
def attandance (df,col_name,attended,abesnt):
    plt.figure(figsize=[10,5])
    df[col_name][notshow].value_counts(normalize=True).plot(kind='pie' , label= 'Not Show')
    plt.legend()
    plt.title('compere between Gender to attendance ')
    plt.xlabel('Gender')
    plt.ylabel('Patiant nm');
attandance (df ,'Gender' ,show ,notshow)


# * number of female not showed more than man by same last presentage too .

# In[24]:


plt.figure(figsize=(10,5))
df.Gender[show].hist(alpha=.5, label='Show')
df.Gender[notshow].hist(alpha=.5, label='Not Show')
plt.legend()
plt.title('compere between Gender to attendance ')
plt.xlabel('Gender')
plt.ylabel('Patiant nm');


# * Female more than male in show and not show too.
# 
# >so gender not affect in attendance

# ### Research Question 3  (Dose attendance affect by Scholarship ?)

# In[25]:


#let answer about scholarship
df.Scholarship[show].value_counts(),df.Scholarship[notshow].value_counts()


# In[26]:


plt.figure(figsize=(10,5))
df.Scholarship[show].hist(alpha=.5, label='Show')
df.Scholarship[notshow].hist(alpha=.5, label='Not Show')
plt.legend()
plt.title('compere between Scholarship to attendance ')
plt.xlabel('Scholarship')
plt.ylabel('Patiant nm');


# * Few pepole who registred in Scholarship and not affect on attendance .

# ### Research Question 4  (Dose attendance affect by chorinc disease (Hypertension + Diabetes  ?)
# 

# In[27]:


#lets answer
df[show].groupby('Hypertension').Diabetes.value_counts() , df[notshow].groupby('Hypertension').Diabetes.value_counts()


# In[28]:


#vis
plt.figure(figsize=(10,5))
df[show].groupby('Hypertension').Diabetes.value_counts().plot(kind='bar', label = 'Show' )
df[notshow].groupby('Hypertension').Diabetes.value_counts().plot(kind='bar', label = 'Not Show' ,color='blue')
plt.legend()
plt.title('compere between chorinc disease to attendance ')
plt.xlabel('chorinc disease')
plt.ylabel('Patiant nm');


# * so chorinic disaese not affected on attendes 

# In[29]:


df.head()


# ### Research Question 4  (Dose attendance affect by  SMS_received ?)
# 

# In[30]:


df.SMS_received[show].value_counts() , df.SMS_received[notshow].value_counts()


# In[31]:


plt.figure(figsize=(10,5))
df.SMS_received[show].hist(alpha=.5, label='Show')
df.SMS_received[notshow].hist(alpha=.5, label='Not Show')
plt.legend()
plt.title('compere between SMS_received to attendance ')
plt.xlabel('SMS_received')
plt.ylabel('Patiant nm');


# > number of showed by recive sms less than showed by not recive sms ( must rethinking about our sms )

# ## Research Question 4 (Dose attendance affect by Neighbourhood )?

# In[32]:


df.Neighbourhood[show].value_counts()


# In[33]:


df.Neighbourhood[notshow].value_counts()


# In[35]:


plt.figure(figsize=(20,6))
df.Neighbourhood[show].value_counts().plot(kind='bar', alpha=.8 ,  label='Show')
df.Neighbourhood[notshow].value_counts().plot(kind='bar', alpha=.5,color='blue'   , label='Not Show')
plt.legend()
plt.title('showing by Neighbourhood')
plt.xlabel('Neighbourhood')
plt.ylabel('patient nm');


# * JARDIM CAMBURI most Neighbourhood in show and not show too .
# * so in some Neighbourhood rate more than else , so we have significant there . 

# <a id='conclusions'></a>
# ## Conclusions
# 
# * Number of showed pepole is great but not affeted by any of disease (Hypertension and Diabetes)
# 
# * Neighbourhood reating is differ from palce to another , JARDIM CAMBURI most Neighbourhood in show and not show too .
# 
# * Sms center must change the sms plane  to get more showed patient .
# 
# * number of pepole registerd in scolahrship is small , we can use sms to awarened pepole about its profit to them. 
# 
# * number of female more than men at all .
# ## limitations :
# 
# * There is no correlation between ( Age , Gender , Sms_recive , scholarship and chronic disease ) and attendding .
# 
# 
# 

# In[34]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:




