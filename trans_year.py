#values of transactions changed in individual years for each district
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
df = pd.read_csv('Property Sales of Melbourne City.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
year_count = df['Year'].value_counts().reset_index()

x=df.groupby(['Year','Regionname'])['Price'].mean().reset_index()

print("Mean price of transactions in Regions during the years (in mln)")
g = sns.barplot(data=x,x='Regionname',y=df['Price']/1000000,hue='Year', palette='hot')
g.bar_label(g.containers[0])
g.bar_label(g.containers[1])
plt.xticks(rotation=90)
sns.move_legend(g, "upper left", bbox_to_anchor=(1, 1))
plt.show()