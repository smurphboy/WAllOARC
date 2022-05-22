#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ctyparser
import gspread as gs
import matplotlib
import os
import pandas as pd
import re
from ipyleaflet import Map, basemaps, basemap_to_tiles


# In[2]:


if os.environ.get('NETLIFY'):
    credentialkeys = ['type', 'project_id', 'private_key_id', 'private_key', 'client_email',
                     'client_id', 'auth_url', 'token_uri', 'auth_provider_x509_cert_url', 'client_x509_cert_url']
    credentials = {}
    for key in credentialkeys:
        credentials['key'] = os.environ.get(key)
    gc = gs.service_account_from_dict(credentials)
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1dpciJGykIvwxHWgWrw_KTVi10EisyUZ6cah962oaStI/edit?usp=sharing')
    ws = sh.worksheet('Form responses 1')
else:
    gc = gs.service_account(filename='../workedalloarc-72453018052d.json')
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1dpciJGykIvwxHWgWrw_KTVi10EisyUZ6cah962oaStI/edit?usp=sharing')
    ws = sh.worksheet('Form responses 1')


# In[3]:


df = pd.DataFrame(ws.get_all_records())
df.head(10)


# In[4]:


# Next we clean the callsigns up and find any prefix / suffix and the DXCC
regex = re.compile('^([A-Z0-9]+[\/])?([A-Z][0-9]|[A-Z]{1,2}|[0-9][A-Z])([0-9]|[0-9]+)([A-Z]+)([\/][A-Z0-9]+)?')
df['Your Callsign Clean'] = df['Your Callsign'].str.upper().str.replace(' ', '').str.replace('Ø', '0')
df['Your DXCC'] = df['Your Callsign Clean'].str.extract(regex, expand=True)[1]
df['Your Prefix'] = df['Your Callsign Clean'].str.extract(regex, expand=True)[0]
df['Your Suffix'] = df['Your Callsign Clean'].str.extract(regex, expand=True)[4]
df['Their Callsign Clean'] = df['Their Callsign'].str.upper().str.replace(' ', '').str.replace('Ø', '0')
df['Their DXCC'] = df['Their Callsign Clean'].str.extract(regex, expand=True)[1]
df['Their Prefix'] = df['Their Callsign Clean'].str.extract(regex, expand=True)[0]
df['Their Suffix'] = df['Their Callsign Clean'].str.extract(regex, expand=True)[4]
df.head(10)


# In[5]:


# Check the DXCC is valid
cty = ctyparser.BigCty()
cty.import_dat('cty.dat')
#df['Valid Your DXCC'] = df['Your DXCC'].isin(cty.keys())
#df['Valid Their DXCC'] = df['Their DXCC'].isin(cty.keys())
#print(cty['VK'])
#dxccs = {}
#for dx in cty.items():
#    dxccs[dx[0]] = dx[1]['entity']
#df['Full Your DXCC'] = df['Your DXCC'].map(dxccs)
#df['Full Their DXCC'] = df['Their DXCC'].map(dxccs)
#df.head(10)


# In[6]:


#print(cty['IW9'])
search_key = 'IW9AAB'
for idx in range(len(search_key)):
    if idx == 0:
        short_key = search_key
    else:
        short_key = search_key[:-(idx)]
    print(short_key)
    res = [val for key, val in cty.items() if short_key in key]
    if res != []:
        a_key = 'entity'
        values_of_key = [a_dict[a_key] for a_dict in res]
        break
print(values_of_key)


# In[7]:


bandplot = df['Band'].value_counts().plot(kind = 'bar')
bandplot.set_title('QSOs by Band')
bandplot.set_xlabel('Count')
bandplot.set_ylabel('Band')


# In[8]:


modeplot = df['Mode'].value_counts().plot(kind = 'bar')
modeplot.set_title('QSOs by Mode')
modeplot.set_xlabel('Count')
modeplot.set_ylabel('Mode')


# In[9]:


callplot = df['Your Callsign Clean'].value_counts().plot(kind = 'bar')
callplot.set_title('QSOs by Callsign')
callplot.set_xlabel('Count')
callplot.set_ylabel('Callsign')


# In[10]:


bandmodeplot = df.groupby(['Band','Mode']).size().reset_index(name='count').plot.scatter(x='Band', y='Mode', s='count')


# In[11]:


callsignmodeplot = df.groupby(['Your Callsign Clean','Mode']).size().reset_index(name='count').plot.scatter(x='Your Callsign Clean', y='Mode', s='count')


# In[12]:


m = Map(
    basemap=basemap_to_tiles(basemaps.OpenStreetMap.Mapnik),
    center=(48.204, 350.121),
    zoom=3
    )
m

