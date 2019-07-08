#!/usr/bin/env python
# coding: utf-8

# In[14]:


import urllib.request, json
url = urllib.request.urlopen('https://api.openaq.org/v1/measurements?city=Los%20Angeles&parameter=pm25')
obj = json.load(url)


# In[5]:


obj


# In[16]:


cat glossary.json


# In[17]:





# In[20]:


import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
a = '{ "name":"John", "age":30, "city":"New York"}'


# parse x:
y = json.loads([x])

# the result is a Python dictionary:
print(y["age"])


# In[101]:


from flask import Flask
import requests
URL = 'https://api.openaq.org/v1/measurements?city=Los%20Angeles&parameter=pm25'
location='pm25'
PARAMS = {'address':location}
r=requests.get(url=URL, params=PARAMS)
data = r.json()
lat_time = data['results'][0]['date']
dall = {}
dall.update(lat_time)
dall.pop('local')
dal_val = data['results'][0]['value']
dal_val = str(dal_val)
dal_val = {'value':dal_val}
dall.update(dal_val)
lat_time_2 = data['results'][1]['date']
dall2 = {}
dall2.update(lat_time_2)
dal_val_2 = data['results'][1]['value']
dal_val_2 = str(dal_val_2)
dal_val_2 = {'value':dal_val_2}
dall2.pop('local')
dall2.update(dal_val_2)
lat_time_3 = data['results'][2]['date']
dall3 = {}
dall3.update(lat_time_3)
dall3.pop('local')
dal_val_3 = data['results'][3]['value']
dic_val_3 = {'value':dal_val_3}
dall3.update(dic_val_3)
lat_time_4 = data['results'][3]['date']
dall4 = {}
dall4.update(lat_time_4)
dall4.pop('local')
dal_val_4 = data['results'][4]['value']
dic_val_4 = {'value':dal_val_4}
dall4.update(dic_val_4)
lat_time_4 = data['results'][4]['date']
dall5 = {}
dall5.update(lat_time_4)
dall5.pop('local')
dal_val_5 = data['results'][5]['value']
dic_val_5 = {'value':dal_val_5}
dall5.update(dic_val_5)
users = [dall,dall2,dall3,dall4,dall5]


# In[22]:


dall


# In[25]:


dall.update(dall2)


# In[26]:


dall


# In[33]:


#dall = {'val': dall, 's': dall3}


# In[29]:


#dall


# In[35]:


#dall6 = {'1': dall, '2':dall2, '3': dall3, '4': dall4, '5': dall5}


# In[36]:


#dall6


# In[37]:





# In[38]:





# In[39]:


#str(dall6)


# In[40]:


dall


# In[109]:


dall=list(dall.values())


# In[42]:





# In[44]:


dall


# In[110]:


dall2=list(dall2.values())


# In[46]:


dall2


# In[111]:


dall3=list(dall3.values())


# In[48]:


dall3


# In[112]:


dall4=list(dall4.values())


# In[51]:


dall4


# In[113]:


dall5=list(dall5.values())


# In[53]:


dall5


# In[114]:


mytable = [dall, dall2, dall3, dall4, dall5]


# In[115]:


for myliste in mytable:
    print(myliste)


# In[119]:


import sqlite3 


# In[120]:


connection = sqlite3.connect("myTable.db") 


# In[121]:


crsr = connection.cursor() 


# In[122]:


sql_command = """CREATE TABLE openaq2(  
Date VARCHAR,
value varchar(20)
);"""


# In[123]:


crsr.execute(sql_command) 


# In[124]:


for myliste in mytable:
    crsr.execute("""INSERT INTO
            openaq2 (Date, Value)
            VALUES (?, ?)""",
        myliste)


# In[125]:


connection.commit() 


# In[126]:


connection.close() 


# In[127]:


import sqlite3 


# In[128]:


connection = sqlite3.connect("myTable.db") 


# In[129]:


crsr = connection.cursor() 


# In[130]:


crsr.execute("SELECT * FROM openaq2")  


# In[131]:


ans= crsr.fetchall()  


# In[132]:


for i in ans: 
    print(i) 


# In[79]:





# In[80]:


#data['results'][3]['date']


# In[87]:


#data['results'][2]['value']


# In[88]:


#for i in users:
    #print(i)


# In[90]:


#dic_val_5


# In[91]:


#dat_val_1


# In[100]:


#dal_val_4


# In[108]:


#for i in dall, dall2, dall3, dall4, dall5:
    print(i)


# In[107]:


#data['results'][2]['value']


# In[ ]:




