import pandas as pd,matplotlib.pyplot as plt,numpy as np
df=pd.read_csv('Data/Data.csv')
df['percentage']=[round(i*100,2) for i in df['percentage']]

plt.style.use('seaborn')
fig,ax=plt.subplots(2,2)
fig.tight_layout(pad=3)
fig.suptitle('Population Census\nby Shakil Mahmud',color='blueviolet',size=14)

ax[0,0].set_title('Line Plot',color='deepskyblue',size=12)
ax[0,0].plot(df['census_round'],df['counted'],color='deepskyblue',marker='*',linewidth=1,label='Counted Population')
ax[0,0].plot(df['census_round'],df['population'],color='fuchsia',marker='*',linewidth=1,label='Total Population')
ax[0,0].plot(df['census_round'],df['percentage'],color='lime',marker='*',linewidth=1,label='Percentage')
ax[0,0].set_xlabel('Census Year',color='deepskyblue',size=10)
ax[0,0].set_ylabel('Counted and Total Population , Percentage',color='deepskyblue',size=10)
ax[0,0].legend()


x=np.arange(len(df))
ax[0,1].set_xticks(x)
ax[0,1].set_xticklabels(df['census_round'])
ax[0,1].set_title('Bar Plot',color='fuchsia',size=12)
ax[0,1].bar(x-0.3,df['counted'],color='deepskyblue',width=0.3,label='Counted Population')
ax[0,1].bar(x,df['population'],color='fuchsia',width=0.3,label='Total Population')
ax[0,1].set_xlabel('Census Year',color='fuchsia',size=10)
ax[0,1].set_ylabel('Counted and Total Population',color='fuchsia',size=10)
ax[0,1].legend()


new_df=df.iloc[0:7,]
new=[i for i in new_df['percentage']]
label=[i for i in new_df['census_round']]
color=['lime','deepskyblue','fuchsia','red','blueviolet','teal','deeppink']
explode=[0.05 for i in range(len(new))]
ax[1,0].set_title('Pie Plot',color='teal',size=12)
ax[1,0].pie(new,colors=color,explode=explode,labels=label,autopct='%1.2f%%',shadow=True)


ax[1,1].set_title('Scatter Plot',color='lime',size=12)
ax[1,1].scatter(df['census_round'],df['counted'],color='deepskyblue',marker='h',label='Counted Population')
ax[1,1].scatter(df['census_round'],df['population'],color='fuchsia',marker='H',label='Total Population')
ax[1,1].scatter(df['census_round'],df['percentage'],color='lime',marker='>',label='Percentage')
ax[1,1].set_xlabel('Census Year',color='lime',size=10)
ax[1,1].set_ylabel('Counted and Total Population , Percentage',color='lime',size=10)
ax[1,1].legend()

plt.show()

#visit the link
# https://datagy.io/split-pandas-dataframe/