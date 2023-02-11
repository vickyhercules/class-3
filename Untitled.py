#!/usr/bin/env python
# coding: utf-8

# In[20]:


a=input()
print(len(a))
print(a[10-1])


# In[16]:


a=[["hello","hi"],["demo","try"]]
print(a[1][0])


# In[6]:


print(a[1][1])


# In[7]:


print(a[0][1])


# In[8]:


print(a[0][0])


# In[10]:


print(a[0][1][0])


# In[14]:


print(a)


# In[31]:


a="viratkohli"
a.index(("i"),a.index("i")+1)


# In[28]:


a=[1,2,3]
b=[4,5,6]
a.append(b)
print(a)


# In[29]:


a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)


# In[32]:


a=[1,2,3]
b=[4,5,6]
b.append(a)
print(b)


# In[33]:


a=[1,2,3]
b=[4,5,6]
b.extend(a)
print(b)


# In[37]:


a=[1,2,3]#this process is called shared memory
b=a# in this process both variables namely a n b shares same memory
a.append(4)# so if we append anything in a it also make changes in b.
print(a)
print(b)


# In[43]:


a=[1,2,3]#this is called different memory.
b=a.copy()#in this both variables a n b has different memory.
a.append(4)#So if we append anything in a it will not make any changes in b.
print(a)
print(b)


# In[42]:


a=[1,2,3]
a=b
a.append(5)
print(a)


# In[50]:


a=(1,2,3)#tuple is another data type.
print(type(a))#list are mutable means it can be edited
print(isinstance(a,tuple))#tuples are non mutable, means tuples cannpot be edited.
a.append(4)
print(a)
print(min(a))


# In[52]:


a=(1,2,3)
print(min(a))
print(max(a))
print(sorted(a))


# In[54]:


a=(1,2,3)
a.index(2)


# In[57]:


a=(1,2,3)
a.rindex


# In[59]:


a=(1,2,3)
print(a[0])
print(a[::-1])


# In[60]:


a={1,2,3}
print(type(a))


# In[61]:


a={1,2,3}
print(isinstance(a,set))


# In[64]:


a={1,1,1,2,2,3,3}#set is a another data type
print(a)#set used to remove duplicates


# In[65]:


a={1,2,3}
a=list(set(a))
print(a)


# In[66]:


a=[1,2,3]
a=set(list(a))
print(a)


# In[67]:


a={1,2,3}
print(min(a))
print(max(a))
print(sorted(a))


# In[72]:


a={1,2,3}#no index,rindex,find,rfind for set. it will show error.
a.index#output of set will be in list.


# In[73]:


a={1,2,3}
a.rindex[2]
a.find(2)


# In[74]:


a={1,2,3}
a.add(4)
print(a)


# In[79]:


a={1,10,20,3,4,200,2000}
print(a)


# In[76]:


a="1,2,3"
print(sorted(a))


# In[81]:


a="test"
print(a.split("s"))


# In[82]:


#there are 4 types of data.
#1 string-this type of datas will be within the quatation Eg: "vicky"
#2 list-this type of dats will be within the square bracket eg:["hi","hello"]
#3 tuple-this type of dtas are immutable and this type of datas will be given in closed brackets eg:(hi)
#4 set- this type of datas will be within {} flower brackets.


# In[84]:


a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))


# In[87]:


a={1,2}
b={1,2,3,4}
print(a.issuperset(b))
print(a.issubset(b))
print(b.issuperset(a))
print(b.issubset(a))


# In[88]:


a={1,2,3}
b={3,4,5}
print(a-b)


# In[90]:


a=[1,2,3]
b=[4,5,6]
print(a+b)


# In[ ]:




