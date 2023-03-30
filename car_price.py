#how numbers of carspots affects price of property taking into account the distance from the Melbourne business district. 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
df = pd.read_csv('Property Sales of Melbourne City.csv')
car_price_dist = df.groupby(['Car','Regionname'])['Price'].mean().reset_index().fillna(0)              

print('Carspots affection on price in Melbournes Regions')
plt.figure(figsize=(20,10))
x = sns.pointplot(data=car_price_dist,x='Car',y='Price',hue='Regionname')
plt.show()

west=df[df['Regionname']== 'Western Metropolitan']
west_best=west[['Suburb','Address','Price', 'Distance','Car','Rooms']]              
westbestsort=west_best.sort_values(['Price','Distance', 'Car'], ascending=[False, False , False]).head(10)  
print('The cheapest region is:')
print(westbestsort.head(30)) 
plt.figure(figsize=(10,10))
plt.subplot(2,1,1)
y = sns.barplot(data=westbestsort,x='Car',y='Price',hue='Suburb')

south=df[df['Regionname']== 'Southern Metropolitan']
south_best=south[['Suburb','Address','Price', 'Distance','Car','Rooms']].fillna(0)               
southbestsort=south_best.sort_values(['Price','Distance', 'Car'], ascending=[False, False , False]).head(10) 
print('\n The most expensive region is:')
print(southbestsort)
plt.subplot(2,1,2)
z = sns.barplot(data=southbestsort,x='Car',y='Price',hue='Suburb')
sns.move_legend(y, "upper left", bbox_to_anchor=(1, 1))
sns.move_legend(z, "upper left", bbox_to_anchor=(1, 1))