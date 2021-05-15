import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd
import plotly.graph_objects as go

##################################
# Top 10 Most Populous Countries #
##################################

df=pd.read_csv('D:/rektorov_rad/programirano/Total_Population/Top10most_populous_countries.csv')
#print(df)

def stripstring(text):
    return text.split('[')[0]

def replacestring(text):
    return text.replace(',','')

df['Nation']=df['Nation'].apply(stripstring)

for i in df.columns[1:]:
    df[i]=df[i].apply(replacestring)

for i in df.columns[1:]:
    df[i]=pd.to_numeric(df[i])

#print(df)

for i in df.columns[1:]:
    fig=px.bar(df,y=i,x='Nation',color='Nation',
           text=i,template='plotly_dark',title='Top 10 most populous countries in '+i)
    fig.show()

##################################
# Population by Continent        #
##################################


df=pd.read_csv('D:/rektorov_rad/programirano/Total_Population/PopulationByContinent.csv')
#print(df)
#print(df.columns)

#for i in df.columns[1:]:
#    print(df[i])

df['Continent']=df['Continent'].apply(stripstring)
df['Density']=pd.to_numeric(df['Density'])
df['Population']=df['Population'].apply(replacestring)
df['Population']=pd.to_numeric(df['Population'])

df2=df['Most_Populous_Country'].to_frame()
df2=df2.Most_Populous_Country.str.split('|',expand=True)
df2=df2.iloc[:,:-2]
df2['CName']=' '
df2['CNum']=' '
#print(df2)

for i,r in df2.iterrows():
    if i == 0:
        df2.iloc[i,-1]=df2.iloc[i,0]
        df2.iloc[i,-2]=df2.iloc[i,3]
    elif i == 5:
        df2.iloc[i,-1]=df2.iloc[i,2]
        df2.iloc[i,-2]=df2.iloc[i,3]
    else:
        df2.iloc[i,-1]=df2.iloc[i,1]
        df2.iloc[i,-2]=df2.iloc[i,2]

df2=df2.iloc[:,-2:]

for i, r in df2.iterrows():
    if i==0:
        pass
    else:
        df2.iloc[i,-1]=df2.iloc[i,-1][:-2]

df2['CNum']=df2['CNum'].apply(replacestring)
df2['CNum']=pd.to_numeric(df2['CNum'])    
#print(df2)
        
df=pd.concat([df,df2], axis=1)
df=df.drop('Most_Populous_Country',axis=1)
#print(df)
#print(df.columns)

df3=df['Most_Populous_City'].to_frame()
df3=df3.Most_Populous_City.str.split('|',expand=True)
df3=df3.iloc[:,[0,1,3]]

for i, r in df3.iterrows():
    df3.iloc[i,0]=df3.iloc[i,0][:-2]

df4=df3.iloc[:,0].str.split('/',expand=True)

#print(df3)
#print(df4)

df4.iloc[:,0]=df4.iloc[:,0].apply(replacestring)
df4.iloc[:,0]=pd.to_numeric(df4.iloc[:,0])
for i,r in df4.iterrows():
    if df4.iloc[i,1] != None:
        df4.iloc[i,1]=df4.iloc[i,1].replace(',','')
df4.iloc[:,0]=pd.to_numeric(df4.iloc[:,0], errors='coerce')

df3=df3.iloc[:,-2:]
df3.columns=['GCA','CA']
df4.columns=['GCAN','CAN']
#print(df3)
#print(df4)
df=pd.concat([df,df3], axis=1)
df=pd.concat([df,df4], axis=1)
df=df.drop('Most_Populous_City',axis=1)

df.columns=['Continent', 'Density', 'Population', 'Country', 'CntryNum', 'Gr_City',
            'City','GrC_Num', 'CityNum']

print(df.dtypes)

print(df)
print(df.columns)

fig=px.bar(df,y='Density',x='Continent',color='Continent',
       text='Density',template='plotly_dark',title='Continent density')
fig.show()

fig=px.bar(df,y='Population',x='Continent',color='Continent',
       text='Population',template='plotly_dark',title='Continent Population')
fig.show()

fig=px.bar(df,y='CntryNum',x='Country',color='Continent',
       text='CntryNum',template='plotly_dark',title='Most Populous Country of each Continent')
fig.show()

fig=px.bar(df,y='GrC_Num',x='Gr_City',color='Continent',
       text='GrC_Num',template='plotly_dark',title='Most Populous City of each Continent')
fig.show()

#######################################
# Top 10 Most Populous Countries 2021 #
#######################################

df=pd.read_csv('D:/rektorov_rad/programirano/Total_Population/Top10_2021.csv')
print(df)

df['Population']=df['Population'].apply(replacestring)
df['Population']=pd.to_numeric(df['Population'])

def stripperc(text):
    return text[:-1]

df['World_Percentage']=df['World_Percentage'].apply(stripperc)
df['World_Percentage']=pd.to_numeric(df['World_Percentage'])

print(df)

fig=px.bar(df,y='Population',x='Nation',color='Nation',
       text='Population',template='plotly_dark',title='Top 10 most populous countries')
fig.show()

fig=px.bar(df,y='World_Percentage',x='Nation',color='Nation',
       text='World_Percentage',template='plotly_dark',title='Percentage of world population')
fig.show()


###########################################
# Top 10 Densely populated Countries 2021 #
###########################################

df=pd.read_csv('D:/rektorov_rad/programirano/Total_Population/Top10Density.csv')
print(df)

for i in df.columns[1:]:
    df[i]=df[i].apply(replacestring)

for i in df.columns[1:]:
    df[i]=pd.to_numeric(df[i])

fig=px.bar(df,y='Population',x='Nation',color='Nation',
       text='Population',template='plotly_dark',title='Population Top 10 Densely populated Countries')
fig.show()

fig=px.bar(df,y='Area',x='Nation',color='Nation',
       text='Area',template='plotly_dark',title='Area Top 10 Densely populated Countries')
fig.show()

fig=px.bar(df,y='Density',x='Nation',color='Nation',
       text='Density',template='plotly_dark',title='Top 10 Densely populated Countries')
fig.show()


###########################################
# Top 10 Countries (Pop+Dens)             #
###########################################

df=pd.read_csv('D:/rektorov_rad/programirano/Total_Population/Top10Pop_Den.csv')
print(df)

for i in df.columns[1:]:
    df[i]=df[i].apply(replacestring)

for i in df.columns[1:]:
    df[i]=pd.to_numeric(df[i])

fig=px.bar(df,y='Population',x='Nation',color='Nation',
       text='Population',template='plotly_dark',title='Population Top 10 Countries')
fig.show()

df=df.sort_values(by='Area', ascending=False)

fig=px.bar(df,y='Area',x='Nation',color='Nation',
       text='Area',template='plotly_dark',title='Area Top 10 Countries')
fig.show()

df=df.sort_values(by='Density', ascending=False)

fig=px.bar(df,y='Density',x='Nation',color='Nation',
       text='Density',template='plotly_dark',title='Density Top 10 Countries')
fig.show()


###########################################
# World History                           #
###########################################

df=pd.read_csv('D:/rektorov_rad/programirano/Total_Population/Global_Annual_Pop_Growth.csv')

print(df)
print(df.columns)
print(df.dtypes)

df['Population']=df['Population'].apply(replacestring)
df['Yearly_Change_Num']=df['Yearly_Change_Num'].apply(replacestring)
df['Urban_Pop']=df['Urban_Pop'].apply(replacestring)
df['Yearly_Change_Perc']=df['Yearly_Change_Perc'].apply(stripperc)
df['Urban_Pop_Perc']=df['Urban_Pop_Perc'].apply(stripperc)

df['Population']=pd.to_numeric(df['Population'])
df['Yearly_Change_Num']=pd.to_numeric(df['Yearly_Change_Num'])
df['Urban_Pop']=pd.to_numeric(df['Urban_Pop'])
df['Yearly_Change_Perc']=pd.to_numeric(df['Yearly_Change_Perc'])
df['Urban_Pop_Perc']=pd.to_numeric(df['Urban_Pop_Perc'])

print(df.dtypes)

for i in df.columns[1:]:
    fig=px.line(df,y=i,x='Year',
       template='plotly_dark',title='Global change over years '+i)
    fig.show()

###########################################
# World History and Prediction            #
###########################################

df=pd.read_csv('D:/rektorov_rad/programirano/Total_Population/W_History_Pred_Pop_mil.csv')
df['Regija']=df['Regija'].apply(stripstring)

for i in df.columns[6:]:
    df[i]=df[i].apply(replacestring)

for i in df.columns[6:]:
    df[i]=pd.to_numeric(df[i])

stupci=df.Regija
df=df.T
df.columns=stupci
df=df.iloc[1:,:]
print(df)
print(df.columns)
print(df.index)

fig=px.line(df,y=df.columns,x=df.index,
   template='plotly_dark',title='Global Population change over years in mil')
fig.show()


for i in range(len(df.columns)):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df.index[:-2],
        y=df.iloc[:-2,i],
        name = 'History',
        mode='lines'
    ))
    fig.add_trace(go.Scatter(
        x=df.index[-3:],
        y=df.iloc[-3:,i],
        name='Prediction',
        mode='lines'       
    ))
    fig.update_layout(template='plotly_dark', title=df.columns[i])
    fig.show()



##fig=px.line(df,y=df.World,x=df.index,
##   template='plotly_dark',title='Global Population change over years in mil')
##fig.add_trace(go.Scatter(
##    x=df.index[-3:],
##    y=df.iloc[-3:,0],
##    name='Prediction'
##))
##fig.show()
