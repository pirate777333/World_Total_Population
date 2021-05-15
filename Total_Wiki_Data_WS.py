import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd

web_page = requests.get('https://en.wikipedia.org/wiki/World_population')

soup = BeautifulSoup(web_page.text, 'html.parser')

tables = soup.find_all('table')

#######################################################
#                                                     #
# TABLE 1 : World population (millions, UN estimates) #
#                                                     #
#######################################################

table1_cols = ['Nation', '2000','2015','2030']

table1=tables[0]

rows=table1.find_all('tr')

Nations = []
dnulte = []
dpetnaest = []
dtrideset = []

for row in rows[2:-2]:
    #print(row)
    table_data=row.find_all('td')
    nation=table_data[1].text.strip()
    nulte=table_data[2].text.strip()
    petnaest=table_data[3].text.strip()
    trideset=table_data[4].text.strip()
    Nations.append(nation)
    dnulte.append(nulte)
    dpetnaest.append(petnaest)
    dtrideset.append(trideset)
    
data4df={table1_cols[0]:Nations, table1_cols[1]:dnulte,
         table1_cols[2]:dpetnaest, table1_cols[3]:dtrideset}

df=pd.DataFrame(data4df)

df.to_csv('Top10most_populous_countries.csv',index=False)

#######################################################
#                                                     #
# TABLE 2 : Population by continent (2020 estimates)  #
#                                                     #
#######################################################

table2_cols = ['Continent', 'Density','Population',
               'Most_Populous_Country','Most_Populous_City']

table2=tables[1]

rows=table2.find_all('tr')

Continent = []
Density = []
Population = []
Country = []
City = []

for row in rows[1:-1]:
    #print(row)
    table_data=row.find_all('td')
    kontinent=table_data[0].text.strip()
    gustoca=table_data[1].text.strip()
    populacija=table_data[2].text.strip()
    drzava=table_data[3].text.strip()
    grad=table_data[4].text.strip()
    Continent.append(kontinent)
    Density.append(gustoca)
    Population.append(populacija)
    Country.append(drzava)
    City.append(grad)
    
data4df={table2_cols[0]:Continent, table2_cols[1]:Density,
         table2_cols[2]:Population, table2_cols[3]:Country,
         table2_cols[4]:City}

df=pd.DataFrame(data4df)

df.to_csv('PopulationByContinent.csv',index=False)

#######################################################
#                                                     #
# TABLE 3 : 10 most populous countries                #
#                                                     #
#######################################################

table3_cols = ['Nation', 'Population','World_Percentage']

table3=tables[4]

rows=table3.find_all('tr')

Nation = []
Population = []
World = []

for row in rows[1:]:
    #print(row)
    table_data=row.find_all('td')
    drzava=table_data[0].text.strip()
    populacija=table_data[1].text.strip()
    svjetska=table_data[2].text.strip()
    Nation.append(drzava)
    Population.append(populacija)
    World.append(svjetska)
    
data4df={table3_cols[0]:Nation, table3_cols[1]:Population,
         table3_cols[2]:World}

df=pd.DataFrame(data4df)

df.to_csv('Top10_2021.csv',index=False)

#####################################################################################
#                                                                                   #
# TABLE 4 : 10 most densely populated countries (with population above 5 million)   #
#                                                                                   #
#####################################################################################

table4_cols = ['Nation', 'Population','Area','Density']

table4=tables[5]

rows=table4.find_all('tr')

Nation = []
Population = []
Area = []
Density = []

for row in rows[1:]:
    #print(row)
    table_data=row.find_all('td')
    drzava=table_data[1].text.strip()
    populacija=table_data[2].text.strip()
    povrsina=table_data[3].text.strip()
    gustoca=table_data[4].text.strip()
    Nation.append(drzava)
    Population.append(populacija)
    Area.append(povrsina)
    Density.append(gustoca)
    
data4df={table4_cols[0]:Nation, table4_cols[1]:Population,
         table4_cols[2]:Area, table4_cols[3]:Density}

df=pd.DataFrame(data4df)

df.to_csv('Top10Density.csv',index=False)

#########################################################################################
#                                                                                       #
# TABLE 5 : Countries ranking highly in both total population and population density    #
#                                                                                       #
#########################################################################################

table5_cols = ['Nation', 'Population','Area','Density']

table5=tables[6]

rows=table5.find_all('tr')

Nation = []
Population = []
Area = []
Density = []

for row in rows[1:]:
    #print(row)
    table_data=row.find_all('td')
    drzava=table_data[1].text.strip()
    populacija=table_data[2].text.strip()
    povrsina=table_data[3].text.strip()
    gustoca=table_data[4].text.strip()
    Nation.append(drzava)
    Population.append(populacija)
    Area.append(povrsina)
    Density.append(gustoca)
    
data4df={table5_cols[0]:Nation, table5_cols[1]:Population,
         table5_cols[2]:Area, table5_cols[3]:Density}

df=pd.DataFrame(data4df)

df.to_csv('Top10Pop_Den.csv',index=False)

#######################################################
#                                                     #
# TABLE 6 : Global annual population growth           #
#                                                     #
#######################################################

table6_cols = ['Year', 'Population','Yearly_Change_Perc',
               'Yearly_Change_Num','Density',
               'Urban_Pop','Urban_Pop_Perc']

table6=tables[7]

rows=table6.find_all('tr')

Year = []
Population = []
YPerc = []
YNum = []
Density = []
Urban = []
UrbanPerc = []

for row in rows[2:]:
    #print(row)
    godina=row.find('th').text.strip()
    table_data=row.find_all('td')
    populacija=table_data[0].text.strip()
    godpost=table_data[1].text.strip()
    godbr=table_data[2].text.strip()
    gustoca=table_data[3].text.strip()
    urbano=table_data[4].text.strip()
    urbanperc=table_data[5].text.strip()
    Year.append(godina)
    Population.append(populacija)
    YPerc.append(godpost)
    YNum.append(godbr)
    Density.append(gustoca)
    Urban.append(urbano)
    UrbanPerc.append(urbanperc)
    
data4df={table6_cols[0]:Year, table6_cols[1]:Population,
         table6_cols[2]:YPerc, table6_cols[3]:YNum,
         table6_cols[4]:Density, table6_cols[5]:Urban,
         table6_cols[6]:UrbanPerc}

df=pd.DataFrame(data4df)

df.to_csv('Global_Annual_Pop_Growth.csv',index=False)

################################################################################
#                                                                              #
# TABLE 7 : World historical and predicted populations (in millions)           #
#                                                                              #
################################################################################

table7_cols = ['Regija', '1500','1600','1700','1750','1800','1850',
               '1900', '1950','1999','2008','2010','2012','2050',
               '2150',]

table7=tables[8]

rows=table7.find_all('tr')

Region = []
Pet = []
Sest = []
Sedam = []
Sedam5 = []
Osam = []
Osam5 = []
Devet = []
Devet5 = []
Devet9 = []
Dva8 = []
Dva10 = []
Dva12 = []
Dva5 = []
Dva15 = []

for row in rows[1:]:
    #print(row)
    reg=row.find('th').text.strip()
    table_data=row.find_all('td')
    
    petn=table_data[0].text.strip()
    sestn=table_data[1].text.strip()
    sedamn=table_data[2].text.strip()
    sedam50=table_data[3].text.strip()
    osamn=table_data[4].text.strip()
    osam50=table_data[5].text.strip()
    devetn=table_data[6].text.strip()
    devet50=table_data[7].text.strip()
    devet99=table_data[8].text.strip()
    dva08=table_data[9].text.strip()
    dva10=table_data[10].text.strip()
    dva012=table_data[11].text.strip()
    dvan50=table_data[12].text.strip()
    dva150=table_data[13].text.strip()
    
    Region.append(reg)
    Pet.append(petn)
    Sest.append(sestn)
    Sedam.append(sedamn)
    Sedam5.append(sedam50)
    Osam.append(osamn)
    Osam5.append(osam50)
    Devet.append(devetn)
    Devet5.append(devet50)
    Devet9.append(devet99)
    Dva8.append(dva08)
    Dva10.append(dva10)
    Dva12.append(dva012)
    Dva5.append(dvan50)
    Dva15.append(dva150)
    
data4df={table7_cols[0]:Region, table7_cols[1]:Pet,
         table7_cols[2]:Sest, table7_cols[3]:Sedam,
         table7_cols[4]:Sedam5, table7_cols[5]:Osam,
         table7_cols[6]:Osam5,
         table7_cols[7]:Devet, table7_cols[8]:Devet5,
         table7_cols[9]:Devet9, table7_cols[10]:Dva8,
         table7_cols[11]:Dva10, table7_cols[12]:Dva12,
         table7_cols[13]:Dva5,table7_cols[14]:Dva15}

df=pd.DataFrame(data4df)

df.to_csv('W_History_Pred_Pop_mil.csv',index=False)
