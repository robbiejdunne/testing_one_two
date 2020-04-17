#!/usr/bin/env python
# coding: utf-8

# In[297]:


import pandas as pd
import seaborn as sns
from scipy.stats import linregress
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import matplotlib.patches as patches
import matplotlib.gridspec as grid_spec


# In[2]:


case1 = pd.read_csv('kingcasemiro.csv')


# In[3]:


case1.sort_values('TklW', ascending=False, inplace=True)
case1.head()


# In[28]:


case1.columns


# In[31]:


plt.scatter(case1['Tkl'], case1['Tkl Vs Dribbles'])


# In[381]:


fig = plt.figure(figsize=(12,4), facecolor='black', edgecolor='black')

ax1 = plt.Axes(fig=fig, rect=[0,0,0.75,0.75], facecolor='black')
fig.add_axes(ax1)
plt.rcParams['font.sans-serif'] = 'Futura'

sns.stripplot(x=case1['Press'], color='white', s=5, jitter=0.01)
plt.scatter(494, 0, color='red', s=120, alpha=0.8, zorder=1000)

plt.yticks(color='white', size=14)
plt.xticks(color='white', size=14)
plt.ylabel('Pressures', color='white', fontsize=18)
plt.xlabel('', color='white', fontsize=18)

ax1.spines['bottom'].set_color('white')
ax1.spines['top'].set_color('white')
ax1.spines['left'].set_color('white')
ax1.spines['right'].set_color('white')

plt.axvline(148.2303263, linewidth=2, color='white', alpha=0.9)

ax1.text(0, -0.03, "LaLiga total pressures", color='white', fontsize=16)

style="Simple,tail_width=0.01,head_width=4,head_length=5"
kw = dict(arrowstyle=style, color="white")


ax1.text(150,0.025, "Average", size=10, color='white', rotation=90)


b = patches.FancyArrowPatch((400,0.02), (494,0), connectionstyle="arc3,rad=0.4", **kw,zorder=1000,lw=1) #curved arrow

ax1.text(340,0.021, "Casemiro", size=12, color='white')

#straight arrow
ax1.add_patch(b)


# In[424]:


case1.head()

case2 = pd.read_csv('passmiro.csv')
case2.sort_values('totaldistance', ascending=True, inplace=True)

case2


# In[555]:


fig = plt.figure(figsize=(16,8), facecolor='black', edgecolor='black')
plt.rcParams['font.sans-serif'] = 'Futura'

ax1 = plt.Axes(fig=fig, rect=[0,0,0.45,0.5], facecolor='black')
ax2 = plt.Axes(fig=fig, rect=[0,0.7,0.45,0.5], facecolor='black')
ax3 = plt.Axes(fig=fig, rect=[0.6,0,0.4,1.2], facecolor='black')


ax1.scatter(case1['Tkl'], case1['TklW'], color='white')
ax1.scatter(98, 67, color='red')

ax2.scatter(case1['Press'], case1['Succ Press'], color='white')
ax2.scatter(494, 189, color='red')

ax3.barh(case2['Player'], case2['totaldistance'], color='white', zorder=100)
ax3.barh(8, 25872, color='red', zorder=100)

fig.add_axes(ax1)
fig.add_axes(ax2)
fig.add_axes(ax3)

plt.rcParams['font.sans-serif'] = 'Futura'

ax1.spines['bottom'].set_color('white')
ax1.spines['top'].set_color('white')
ax1.spines['left'].set_color('white')
ax1.spines['right'].set_color('white')

ax2.spines['bottom'].set_color('white')
ax2.spines['top'].set_color('white')
ax2.spines['left'].set_color('white')
ax2.spines['right'].set_color('white')

ax3.spines['bottom'].set_color('white')
ax3.spines['top'].set_color('white')
ax3.spines['left'].set_color('white')
ax3.spines['right'].set_color('white')

ax1.set_xlabel('Players Tackled', color='white', fontsize=18)
ax2.set_xlabel('Pressures', color='white', fontsize=18)
ax1.set_ylabel('Tackles Won', color='white', fontsize=18)
ax2.set_ylabel('Successful Pressures', color='white', fontsize=18)

plt.yticks(color='white', size=14)
plt.xticks(color='white', size=14)
plt.ylabel('Player', color='white', fontsize=18)
plt.xlabel('Total Passing Yards', color='white', fontsize=18)

ax1.text(0, 75, "Tackling Success", color='white', fontsize=23)
ax2.text(0, 250, "Pressure vs Successful Pressure", color='white', fontsize=24)
ax3.text(0, 21, "LaLiga's Top 20 players in passing distance", color='white', fontsize=24)


# In[432]:


case1.sort_values('Tkl', ascending=False)


# In[538]:


fig = plt.figure(figsize=(12,4), facecolor='black', edgecolor='black')

ax1 = plt.Axes(fig=fig, rect=[0,0,0.75,0.75], facecolor='black')
fig.add_axes(ax1)
plt.rcParams['font.sans-serif'] = 'Futura'

sns.stripplot(x=case1['Tkl'], color='white', s=5)

plt.yticks(color='white', size=14)
plt.xticks(color='white', size=14)
#plt.ylabel('', color='white', fontsize=18)
plt.xlabel('', color='white', fontsize=18)

ax1.spines['bottom'].set_color('white')
ax1.spines['top'].set_color('white')
ax1.spines['left'].set_color('white')
ax1.spines['right'].set_color('white')

#plt.axvline(148.2303263, linewidth=2, color='white', alpha=0.9)

ax1.text(0, -0.65, "Number of players tackled", color='white', fontsize=22)
ax1.text(0, -0.55, "LaLiga 2019-20", color='white', fontsize=14)


#ax1.text(150,0.025, "Average", size=10, color='white', rotation=90)



ax1.text(93,0.001, "Casemiro", size=12, color='white')


# In[539]:


case1.head()


# In[548]:


new_case = case1[(case1['Tkl'] > 50) & (case1['Int'] > 30)]


# In[549]:


plt.barh(new_case['Player'], new_case['Tkl'] + new_case['Int'])


# In[563]:


new_case.iloc[1:5]


# In[ ]:




