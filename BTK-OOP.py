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


# In[50]:


class SuperKahraman():
    
    ozelGuc = "Görünmezlik"
    
    def __init__(self,isim,yas,meslek):
        print("init cagirilidi")
        self.isim = isim
        self.yas = yas
        self.meslek = meslek
        
        
    def ornekMethod(self):
        print(f"ben süperkahramanım ve meslegim: {self.meslek}")


# In[51]:


superman = SuperKahraman("Superman",30,"gazeteci")


# In[52]:


superman.isim = "Clark Kent"


# In[53]:


superman.isim


# In[54]:


superman.ozelGuc = "Uçabilirlik"


# In[55]:


superman.ozelGuc


# ## Methods

# In[56]:


superman.ornekMethod()


# In[101]:


class Kopek():
    
    yilCarpani = 7
    
    def __init__(self,yas=5):
        self.yas = yas
        self.insanYasinaCevrilmisAttribute = yas * 7
    
    def insanYasiniHesapla(self):
        return self.yas * Kopek.yilCarpani


# In[102]:


benimKopek = Kopek()


# In[103]:


benimKopek.yas


# In[104]:


benimKopek = Kopek(3)


# In[106]:


benimKopek.insanYasiniHesapla()

