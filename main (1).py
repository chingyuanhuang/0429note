
# coding: utf-8

# In[1]:


import pandas as pd

dfs = pd.read_csv("ted_main.csv" , encoding = "utf-8")
dfs


# In[2]:


dfs.shape


# In[3]:


dfs.shape[0]


# In[4]:


dfs.T


# In[5]:


dfs_t = dfs.T
dfs_t


# In[7]:


dfs_t.to_csv("ted_main_transfrom.csv" , encoding = "utf-8")


# In[8]:


dfs["comments"]


# In[9]:


dfs[["comments" , "event" , "main_speaker"]]


# In[10]:


del dfs["duration"]
dfs


# In[11]:


dfs.iloc[0]


# In[12]:


dfs.iloc[0 : 10]


# In[13]:


dfs.head(10)


# In[14]:


dfs.tail(10)


# In[15]:


dfs.iloc[999:]


# In[17]:


dfs[["comments" , "description"]].iloc[1000:]


# In[20]:


fil = dfs["description"].str.contains("sir")
fil


# In[21]:


dfs[fil]


# In[22]:


dfs[fil].shape


# In[24]:


dfs[dfs["description"].str.contains(r"\bsir\b")]
dfs


# In[26]:


def flow(in_data):
    a = eval(in_data)
    result = 'children' in a
    return result
fil = dfs['tags'].apply(flow)
fil


# In[27]:


dfs[fil]


# In[ ]:




