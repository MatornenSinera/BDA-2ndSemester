import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from matplotlib.pyplot import figure

data=pd.read_csv('co2.csv', delimiter = ";", index_col="date")
print(data.index.dtype)
data.index=pd.to_datetime(data.index, errors = 'coerce')
data_after_1950=data[data.index.year>=1950]
print(data_after_1950)
data_mean_after_1950=((data_after_1950.groupby(data_after_1950.index.year).transform("mean")).iloc[::12])

plt.plot(data_mean_after_1950.index.year, data_mean_after_1950["data_mean_global"])
plt.plot(data_mean_after_1950.index.year, data_mean_after_1950["data_mean_nh"])
plt.plot(data_mean_after_1950.index.year, data_mean_after_1950["data_mean_sh"])
plt.legend(["Mean - Global",  "Mean - Northern Hemisphere",  "Mean - Southern Hemisphere"])
plt.title("Mean annual CO2 concentrations")
plt.ylabel("Parts per milion (ppm)")
plt.xlabel("Year")
plt.show()

#//BOXPLOTS
data_box_plots=data_after_1950
data_box_plots.index=data_box_plots.index.strftime("%B")
sns.boxplot(y="data_mean_global", x=data_box_plots.index, data=data_box_plots)
plt.title("Spread of monthly CO2 concentrations")
plt.ylabel("Parts per milion (ppm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#//BARPLOTS
data_bar_plots=data[data.index.year==1996]

data_bar_plots.index=data_bar_plots.index.strftime("%B")
data_bar_plots.plot.bar(y=['data_mean_nh', 'data_mean_sh'])
plt.title("Comparison of monthly CO2 concentrations in 1996")
plt.ylabel("Parts per milion (ppm)")
plt.legend(["Northern Hemisphere",  "Southern Hemisphere"], loc=1)
print(data_bar_plots)
x1,x2,y1,y2=plt.axis()
plt.axis((x1,x2, 300, 400))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

##PLOT MONTHLY CONCENTRATIONS
data_after_1950_subplot=data[data.index.year>=1950]
fix,ax=plt.subplots(2, figsize=(12,10))
ax[0].plot(data_after_1950_subplot.index, data_after_1950["data_mean_nh"])
ax[0].set_title("Northern Hemisphere")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("ppm")
ax[1].plot(data_after_1950_subplot.index, data_after_1950["data_mean_sh"])
ax[1].set_title("Southern Hemisphere")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("ppm")
plt.subplots_adjust(hspace=0.25)
plt.show()

data_northern= data_after_1950_subplot.loc[:,'data_mean_nh']
data_southern= data_after_1950_subplot.loc[:,'data_mean_sh']
data_global = data_after_1950_subplot.loc[:, "data_mean_global"]

fig, axes = plt.subplots(2,1, figsize=(12,10))
fig.suptitle("Autocorellation Function", fontsize=20)
fig = plot_acf(data_northern, lags= 730, ax=axes[0])
axes[0].set_title("Northern Hemisphere", fontsize=16)
axes[0].set_xlabel("Year", fontsize=12)
axes[0].set_ylabel("ppm", fontsize=12)
fig = plot_acf(data_southern, lags=730 , ax=axes[1])
axes[1].set_title("Southern Hemisphere", fontsize=16)
axes[1].set_xlabel("Year", fontsize=12)
axes[1].set_ylabel("ppm", fontsize=12)
plt.subplots_adjust(hspace=0.25)
plt.show()

fig, axes = plt.subplots(2,1, figsize=(12,10))
fig.suptitle("Partial Autocorellation Function", fontsize=20)
fig = plot_pacf(data_northern, lags= 15, ax=axes[0])
axes[0].set_title("Northern Hemisphere", fontsize=16)
axes[0].set_xlabel("Year", fontsize=12)
axes[0].set_ylabel("ppm", fontsize=12)
fig = plot_pacf(data_southern, lags= 15, ax=axes[1])
axes[1].set_title("Southern Hemisphere", fontsize=16)
axes[1].set_xlabel("Year", fontsize=12)
axes[1].set_ylabel("ppm", fontsize=12)
plt.subplots_adjust(hspace=0.25)
plt.show()

## DECOMPOSIOTION
print(data_northern)
result = seasonal_decompose(data_northern, model='additive', freq=12)
print(result.trend)
print(result.seasonal)
print(result.resid)
print(result.observed)
result.plot()
plt.xlabel("Year")

print(data_northern)
result = seasonal_decompose(data_southern, model='additive', freq=12)
print(result.trend)
print(result.seasonal)
print(result.resid)
print(result.observed)
result.plot()
plt.xlabel("Year")
plt.show()

print(data_northern)
result = seasonal_decompose(data_northern, model='multiplicative', freq=12)
print(result.trend)
print(result.seasonal)
print(result.resid)
print(result.observed)
result.plot()
plt.xlabel("Year")

print(data_northern)
result = seasonal_decompose(data_southern, model='multiplicative', freq=12)
print(result.trend)
print(result.seasonal)
print(result.resid)
print(result.observed)
result.plot()
plt.xlabel("Year")
plt.show()


