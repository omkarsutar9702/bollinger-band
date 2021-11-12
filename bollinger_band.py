#import libraies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

#import dataset
df_new=pd.read_csv("D:/PYTHON/test/ETH-USD.csv")
df = df_new[:500]
df.info()
#calculate simple moving average standerd deviation  , upper and lower band
#get a time window(30days)
#simple moving average
df['SMA'] = df['Close'].rolling(window = 30).mean()
#standerd deviation
df["STD"] = df["Close"].rolling(window = 30).std()
#the upper band
df["Upper"] = df["SMA"]+(df["STD"]*2)
#the lower band
df["lower"] = df["SMA"]- (df["STD"]*2)
#list of column to keep
column_keep = ["Close" , "SMA" ,"Upper","lower"]
#plot the graph
df[column_keep].plot(figsize=(13,6))
plt.title("bollinger band ")
plt.xlabel("date")
plt.ylabel("price")
plt.show()

#plot and shade the area between the two bands
fig = plt.figure()
ax = fig.add_subplot(1,1,1)#no.rows , #no.columns , #no. index
#get index value kof data frame
x_axis = df.index
#plot and shade the area between upper and lower bands
ax.fill_between(x_axis,df["Upper"],df["lower"] , color = "#92d495" , alpha=0.5)
#plot the closing price and moving average
ax.plot(x_axis , df["Close"],lw=2,label="closing price")
ax.plot(x_axis , df["SMA"] , lw=2 , label="SMA")
ax.set_title("bollinger band")
ax.set_xlabel("date")
ax.set_ylabel("price")
ax.legend()
plt.show()
















