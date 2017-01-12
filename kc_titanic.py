
# coding: utf-8


# In[32]:

import pandas as pd
titanic_df = pd.read_csv('titanic_data.csv')
titanic_df.head()


# In[35]:

man_woman = {'male':'Man', 'female':'Woman'}
titanic_df['Man_Woman_Child'] = titanic_df['Sex'].map(man_woman)

titanic_df.loc[titanic_df['Age'] < 16, 'Man_Woman_Child'] = 'Child'

no_age_man_woman = {'male':'Male Unknown Age', 'female':'Female Unknown Age'}
titanic_df.loc[titanic_df['Age'].isnull(), 'Man_Woman_Child'] = titanic_df['Sex'].map(no_age_man_woman)

has_age_df = titanic_df[titanic_df['Age'].notnull()]


# In[38]:

pd.options.display.float_format = '{:,.0f}'.format
#new_titanic_df = pd.DataFrame({'count' : titanic_df.groupby( [ "Pclass", "Man_Woman_Child"] ).size()}).reset_index()

new_titanic_df = pd.DataFrame({'count' : has_age_df.groupby( [ "Pclass", "Man_Woman_Child"] ).size()}).reset_index()
for idx, record in new_titanic_df.iterrows():
    #print index
    #print row
    new_titanic_df.set_value(idx,'Survivors', int(len(titanic_df[(titanic_df['Pclass']==record['Pclass']) & 
                                     (titanic_df['Man_Woman_Child']==record['Man_Woman_Child']) & 
                                     (titanic_df['Survived']==1) ])) )
    new_titanic_df.set_value(idx,'Victims', int(len(titanic_df[(titanic_df['Pclass']==record['Pclass']) & 
                                     (titanic_df['Man_Woman_Child']==record['Man_Woman_Child']) & 
                                     (titanic_df['Survived']==0) ])) )
    Pclass_map = {1:" 1st Class", 2: " 2nd Class", 3:" 3rd Class"}
    new_titanic_df.set_value(idx, 'Demographic', record['Man_Woman_Child'] + Pclass_map[record['Pclass']] )
        
new_titanic_df


# In[40]:

new_titanic_df.to_csv('titanic_mortality.csv')


# In[41]:

print sum(new_titanic_df['count'])


# In[ ]:



