#numbers of transactions changed in individual years for each district
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
df = pd.read_csv('Property Sales of Melbourne City.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
year_count = df['Year'].value_counts().reset_index()

x2=df[['Year','Regionname']].value_counts().reset_index().rename(columns={'Year':'Year','Regionname':'Region', 0:'transactions'})

g = sns.barplot(data=x2,x='Region',y='transactions',hue='Year', palette='hot')
g.bar_label(g.containers[0])
g.bar_label(g.containers[1])
plt.xticks(rotation=90)
sns.move_legend(g, "upper left", bbox_to_anchor=(1, 1))
plt.show()