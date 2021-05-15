import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd

df=pd.read_csv('D:/rektorov_rad/programirano/Total_Population/96bf5c84-5efc-4802-b2b1-273550977004_Data.csv')
#print(df.iloc[:-5,2:-2])
df=df.iloc[:-5,2:-2]

df.columns=['Country Name', 'Country Code', '1990', '2000',
            '2011', '2012', '2013', '2014', '2015', '2016',
            '2017', '2018']

world = df[df['Country Name']=='World']
#print(world)
df=df.iloc[:-47,:]
#print(df.tail())

#print(df.shape)

def stringops(text):
    if text=='..':
        return None
    else:
        return text

for i in df.columns:
    df[i]=df[i].apply(stringops)

#df=df.dropna()

     
#print(df.isnull().sum())
#print(df[df['2018'].isnull()])

#print(df.shape)

lista=['1990', '2000',
            '2011', '2012', '2013', '2014', '2015', '2016',
            '2017', '2018']

for i in lista:
    df[i]=pd.to_numeric(df[i], errors='coerce')

print(df.dtypes)
print(df.isnull().sum())


df=df.sort_values(by='2018', ascending=False)
print(df.iloc[:10,:])

fig=px.bar(df.iloc[0:10],y='2018',x='Country Name',color='Country Name',
           text='2018',template='plotly_dark',title='(Highest) Population Density')
fig.show()

df=df.sort_values(by='2018', ascending=True)
print(df.iloc[:10,:])

fig=px.bar(df.iloc[:10],y='2018',x='Country Name',color='Country Name',
           text='2018',template='plotly_dark',title='(Lowest) Population Density')
fig.show()


# WORLD
for i in lista:
    world[i]=pd.to_numeric(world[i])

world=world.T
world=world.iloc[2:,:]
year=world.index.tolist()
data=world.iloc[:,0].tolist()
fig=px.bar(y=data,x=year,color=year,
       template='plotly_dark',title='World Population Density',
       labels=dict(x="Years", y="Population Density", color="Years"))
fig.show()
fig=px.line(y=data,x=year,
       template='plotly_dark',title='World Population Density',
       labels=dict(x="Years", y="Population Density"))
fig.show()


def specific_country(country_name):
    country_data = df[df['Country Name']==country_name]
    country_data=country_data.T
    country_data=country_data.iloc[2:,:]
    year=country_data.index.tolist()
    data=country_data.iloc[:,0].tolist()
    fig=px.bar(y=data,x=year,color=year,
           template='plotly_dark',title=country_name+' Population in largest city',
           labels=dict(x="Years", y="Population in largest city", color="Years"))
    fig.show()
    fig=px.line(y=data,x=year,
           template='plotly_dark',title=country_name+' Population in largest city',
           labels=dict(x="Years", y="Population in largest city"))
    fig.show()

a=input('Your Country Name: __ ')

try:
    specific_country(a)
except:
    print('Invalid Country Name')


df['19_90']=(df['2018']/df['1990'])-1
df=df.sort_values(by='19_90', ascending=False)

fig=px.bar(df.iloc[0:10],y='19_90',x='Country Name',color='Country Name',
           text='19_90',template='plotly_dark',title='(Highest) Growth of Total Population in %')
fig.show()

df=df.sort_values(by='19_90', ascending=True)

fig=px.bar(df.iloc[0:10],y='19_90',x='Country Name',color='Country Name',
           text='19_90',template='plotly_dark',title='(Lowest) Growth of Total Population in %')
fig.show()

world_map=gpd.read_file("D:/desktop_things/Diplomski/3/GeoViz/esej/World_Map.shp")

world_map.replace("The former Yugoslav Republic of Macedonia","North Macedonia",inplace=True)
world_map.replace("Democratic Republic of the Congo","Congo, Rep.",inplace=True)
world_map.replace("Lao People's Democratic Republic","Lao PDR",inplace=True)
world_map.replace("Republic of Moldova","Moldova",inplace=True)
world_map.replace("Micronesia, Federated States of","Micronesia, Fed. Sts.",inplace=True)
world_map.replace("Korea, Democratic People's Republic of","Korea, Dem. People's Rep.",inplace=True)
world_map.replace("Burma","Myanmar",inplace=True)
world_map.replace("Palestine","West Bank and Gaza",inplace=True)
world_map.replace("Korea, Republic of","Korea, Rep.",inplace=True)
world_map.replace("Yemen","Yemen, Rep.",inplace=True)
world_map.replace("Venezuela","Venezuela, RB",inplace=True)
world_map.replace("Russia","Russian Federation",inplace=True)
world_map.replace("Saint Kitts and Nevis","St. Kitts and Nevis",inplace=True)
world_map.replace("Macau","Macao SAR, China",inplace=True)
world_map.replace("United Republic of Tanzania","Tanzania",inplace=True)
world_map.replace("Cape Verde","Cabo Verde",inplace=True)
world_map.replace("Saint Vincent and the Grenadines","St. Vincent and the Grenadines",inplace=True)
world_map.replace("Libyan Arab Jamahiriya","Libya",inplace=True)
world_map.replace("Egypt","Egypt, Arab Rep.",inplace=True)
world_map.replace("Iran (Islamic Republic of)","Iran, Islamic Rep.",inplace=True)
world_map.replace("Iran (Islamic Republic of)","Iran, Islamic Rep.",inplace=True)
world_map.replace("Kyrgyzstan","Kyrgyz Republic",inplace=True)
world_map.replace("Western Sahara","South Sudan",inplace=True)
world_map.replace("Congo","Congo, Rep.",inplace=True)


##for i,r in df.iterrows():
##    if df.iloc[i,0] not in world_map['NAME'].to_list():
##        print(df.iloc[i,0])

df.columns=['NAME', 'Country Code', '1990', '2000',
            '2011', '2012', '2013', '2014', '2015', '2016',
            '2017', '2018','19_90']

merge=pd.merge(world_map, df, on='NAME', how='outer')
#print(merge)
merge=merge.set_geometry('geometry')
ax=merge.plot(column="2018",
              cmap="OrRd",
              figsize=(15,15),
              legend=True,
              scheme="user_defined",
              classification_kwds={"bins":[5,10,50,100,500,1000,
                                           2000,5000,10000,20000]},
              edgecolor="black",
              linewidth=0.5)
ax.set_title("Population Density 2018", fontdict={'fontsize':20})

ax.set_axis_off()

ax.get_legend().set_bbox_to_anchor((0.18, 0.6))

plt.show()
