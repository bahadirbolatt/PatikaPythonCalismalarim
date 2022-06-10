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

# In[2]:


superman.ornekMethod()


# In[3]:


class Kopek():
    
    yilCarpani = 7
    
    def __init__(self,yas=5):
        self.yas = yas
        self.insanYasinaCevrilmisAttribute = yas * 7
    
    def insanYasiniHesapla(self):
        return self.yas * Kopek.yilCarpani


# In[4]:


benimKopek = Kopek()


# In[5]:


benimKopek.yas


# In[6]:


benimKopek = Kopek(3)


# In[7]:


benimKopek.insanYasiniHesapla()


# ## inheritance

# In[8]:


class Hayvan():
    def __init__(self):
        print("hayvan sınıfı init çağırıldı.")
        
    def method1(self):
        print("hayvan sınıfı method1 çağırıldı.")
        
    def method2(self):
        print("hayvan sınıfı method2 çağırıldı.")


# In[9]:


benimHayvanim = Hayvan()


# In[10]:


benimHayvanim.method1()


# In[11]:


benimHayvanim.method2()


# In[22]:


class Kedi(Hayvan):
    def __init__(self):
        Hayvan.__init__(self)
        print("Kedi sınıfı init çağırıldı.")
    
    def miyavla(self):
        print("miyav")
    #override    
    def method1(self):
        print("kedi sınıfındaki method1 çağırıldı")


# In[23]:


benimKedim = Kedi()


# In[24]:


benimKedim.method1()


# In[25]:


benimKedim.method2()


# In[26]:


benimKedim.miyavla()


# In[27]:


digerHayvan = Hayvan()


# In[29]:


digerHayvan.method1()


# In[31]:


digerKedi = Kedi()


# In[32]:


digerKedi.method1()

