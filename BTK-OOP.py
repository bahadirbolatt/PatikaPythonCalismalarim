#!/usr/bin/env python
# coding: utf-8

# In[1]:


myList = list()


# In[2]:


type(myList)


# ## instance ve attribute

# In[3]:


superKahramanAdi = "Superman"
superKahramanYasi = 30


# In[18]:


class SuperKahraman():
    def __init__(self,isim,yas,meslek):
        print("init cagirilidi")
        self.isim = isim
        self.yas = yas
        self.meslek = meslek


# In[19]:


superman = SuperKahraman("Superman",30,"gazeteci")


# In[20]:


superman.isim = "Clark Kent"


# In[21]:


superman.isim


# In[ ]: