import csv
import pandas as pd
from pandas import DataFrame
import pandas as pd
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
import datetime
import codecs
import matplotlib.pyplot as plt
 
import warnings
warnings.filterwarnings("ignore")


#Open file columns
c=pd.read_csv('freedom_index.csv')
#print(c.head(100))

#Function to extract freedom_index/country

def freedom_country(f_index):
    print(f_index)
    

#freedom_country(f_index=c[c.Country=='Luxembourg'])
    
    #--------------------------------------------------Selecting data and parsing it for EU 2024 

#Creating a similar dataset with less columns so we can further process    
f=c[['Year','Country','Region','Government Integrity','Tax Burden','Fiscal Health','Property Rights','Judicial Effectiveness','Overall Score']]
#print(f)

#Taking only the 2024 dataset with less columns
fy=f[f.Year==2024]
#print(fy)



#Region EU and 2024
f_europe=fy[fy.Region=='Europe']
#print(f_europe.head(10))
#print(f_europe.columns)
df_europe=f_europe.rename(columns={'Government Integrity':'Government_Integrity','Fiscal Health':'Fiscal_Health','Property Rights':'Property_Rights','Overall Score':'Overall_Score','Judicial Effectiveness':'Judicial_Effectiveness','Tax Burden':'Tax_Burden'})
#print(df_europe.head(10))

# save data for EU 2024 to csv for further pbix processing 
#pass df to the desired dataset
# save it with a created name.csv
#print file 
df=f_europe
df.to_csv('f.csv',header = True)  
df.to_csv('f.csv')
print(df)


#Create a pivottable to count overall scores per region for 2024
pivot1=f_europe.pivot_table(index='Overall Score',columns='Country', aggfunc={'Region':'count'}).fillna(0)
pivot1['Max']=pivot1.idxmax(axis=1)
print(pivot1.tail(20))


#------------------------------------------------------graphs 

sns.violinplot(x=c["Region"], y=c["Overall Score"], palette="Blues")
plt.show()


plt.figure(figsize=(10,7))
sns.heatmap(f_europe.corr(), annot=True, cmap=sns.diverging_palette(100,200, as_cmap=True),center=0, linewidth=1,vmin=-1,vmax=1, yticklabels=True,xticklabels=True)
plt.show()


plt.figure(figsize=(8,5))
sns.boxplot(df_europe['Country'],color="y")
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(x=df_europe.Overall_Score, y=df_europe.Government_Integrity, s=100, marker='o',cmap='viridis')
plt.title("Customized Scatter Plot")
plt.xlabel("Government_Integrity")
plt.ylabel("Overall_Score")
plt.colorbar(label='Color Intensity')
plt.show()

