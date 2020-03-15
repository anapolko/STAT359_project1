#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pymongo
import datetime
import dnspython
pymongo.version
from pymongo import MongoClient


# In[7]:


client = MongoClient("mongodb+srv://poana:<password>@cluster0-ljlqv.gcp.mongodb.net/test?retryWrites=true&w=majority")


# In[8]:


db = client.gettingStarted
people = db.people


# In[9]:


personDocument = {
  "name": { "first": "Alan", "last": "Turing" },
  "birth": datetime.datetime(1912, 6, 23),
  "death": datetime.datetime(1954, 6, 7),
  "contribs": [ "Turing machine", "Turing test", "Turingery" ],
  "views": 1250000
}


# In[10]:


people.insert_one(personDocument)


# In[11]:


personDocument2 = {
  "name": { "first": "John", "last": "Smith" },
  "birth": datetime.datetime(2000, 6, 23),
  "contribs": [ "Good Muffins", "Tasty Cake", "Chewy Cookies" ],
  "views": 1250000
}


# In[12]:


people.insert_one(personDocument2)


# In[13]:


myquery = {"name":{"first": "Alan", "last": "Turing"}}
people.delete_one(myquery)


# In[ ]:




