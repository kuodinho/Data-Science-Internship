#Distance from the property to Melbourne central business district (CBD) in kilometers compare to price
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Property Sales of Melbourne City.csv')
df['pricetodist'] = df['Price']/((df['Distance'])+1)

x=df[['Distance','Price', 'pricetodist','Longtitude' ,'Lattitude']]

plt.figure(figsize=(20,20))
sns.scatterplot(x='Longtitude',y='Lattitude',data=x,hue='pricetodist')
