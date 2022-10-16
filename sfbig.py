#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Code cell 1
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium 


# In[4]:


# code cell 2
# This should be a local path
dataset_path = 'C:\\Users\\ekinc\\OneDrive\\Masaüstü\\Map-Crime_Incidents-Previous_Three_Months.csv'

# read the original dataset (in comma separated values format) into a DataFrame
SF = pd.read_csv('C:\\Users\\ekinc\\OneDrive\\Masaüstü\\Map-Crime_Incidents-Previous_Three_Months.csv')


# In[5]:


get_ipython().system("head -n 5 'C:\\\\Users\\\\ekinc\\\\OneDrive\\\\Masaüstü\\\\Map-Crime_Incidents-Previous_Three_Months.csv'")


# In[6]:


pd.set_option('display.max_rows', 10) #Visualize 10 rows 
SF


# In[7]:


SF.columns


# In[8]:


len(SF)


# In[10]:


SF['Month'] = SF['Date'].apply(lambda row: int(row[0:2]))
SF['Day'] = SF['Date'].apply(lambda row: int(row[3:5]))


# In[11]:


print(SF['Month'][0:2])
print(SF['Day'][0:2])


# In[12]:


print(type(SF['Month'][0]))


# In[13]:


del SF['IncidntNum']


# In[14]:


SF.drop('Location', axis=1, inplace=True )


# In[15]:


SF.columns


# In[16]:


CountCategory = SF['Category'].value_counts()
print(CountCategory)


# In[17]:


SF['Category'].value_counts(ascending=True)


# In[18]:


print(SF['Category'].value_counts(ascending=True))


# In[19]:


print(SF['PdDistrict'].value_counts(ascending=True))


# In[20]:


AugustCrimes = SF[SF['Month'] == 8]
AugustCrimes


# In[21]:


AugustCrimes = SF[SF['Month'] == 8]
AugustCrimesB = SF[SF['Category'] == 'BURGLARY']
len(AugustCrimesB)


# In[22]:


Crime0704 = SF.query('Month == 7 and Day == 4')
Crime0704


# In[23]:


SF.columns


# In[24]:


plt.plot(SF['X'],SF['Y'], 'ro')
plt.show()


# In[25]:


pd_districts = np.unique(SF['PdDistrict'])
pd_districts_levels = dict(zip(pd_districts, range(len(pd_districts))))
pd_districts_levels


# In[26]:


SF['PdDistrictCode'] = SF['PdDistrict'].apply(lambda row: pd_districts_levels[row])


# In[27]:


plt.scatter(SF['X'], SF['Y'], c=SF['PdDistrictCode'])
plt.show()


# In[28]:


from matplotlib import colors
districts = np.unique(SF['PdDistrict'])
print(list(colors.cnames.values())[0:len(districts)])


# In[29]:


color_dict = dict(zip(districts, list(colors.cnames.values())[0:-1:len(districts)])) 
color_dict


# In[30]:


map_osm = folium.Map(location=[SF['Y'].mean(), SF['X'].mean()], zoom_start = 12)
plotEvery = 50
obs = list(zip( SF['Y'], SF['X'], SF['PdDistrict'])) 

for el in obs[0:-1:plotEvery]: 
    
    folium.CircleMarker(el[0:2], color=color_dict[el[2]], fill_color=el[2],radius=10).add_to(map_osm)
    


# In[31]:


map_osm


# In[ ]:




