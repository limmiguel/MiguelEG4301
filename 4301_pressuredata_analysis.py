# -*- coding: utf-8 -*-
"""4301_PressureData.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qWSjygOddxsssb9AVa004IJc4lPLGEER
"""
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from scipy.signal import savgol_filter

# Load data into a pandas DataFrame
data = pd.read_csv('miguel_data_log_2023-10-12_19-24.csv',index_col=False)

data
#%%

#df_time = pd.to_datetime(data["Date/Time"]).dt.second
#data = data.drop(data[data.LB > 500].index)
#data = data.drop(data[data.RB > 500].index)

lm = data['LL']
mm = data['ML']
rm = data['RL']

#lm = data['LM'] #original
#mm = data['MM']
#rm = data['RM']

lu = data['LU']
mu = data['MU']
ru = data['RU']

lb = data['LB']
mb = data['MB']
rb = data['RB']


#df_time

#%%
"""# Pressure Data Analysis"""

# Extract the columns that we want to plot
figure(figsize=(20, 8), dpi=100)


# Calculate some basic statistics on the data
mean_lb = np.mean(lb)
mean_rb = np.mean(rb)
mean_lm = np.mean(lm)
mean_rm = np.mean(rm)
mean_lu = np.mean(lu)
mean_ru = np.mean(ru)
std_dev_lb = np.std(lb)
std_dev_rb = np.std(rb)
std_dev_lm = np.std(lm)
std_dev_rm = np.std(rm)
std_dev_lu = np.std(lu)
std_dev_ru = np.std(ru)

# Create a scatter plot of the data
plt.plot(data.index, lb,label="LB")
plt.plot(data.index, mb,label="MB")
plt.plot(data.index, rb,label="RB")
plt.plot(data.index, lm,label="LM")
plt.plot(data.index, mm,label="MM")
plt.plot(data.index, rm,label="RM")
plt.plot(data.index, lu, label="LU")
plt.plot(data.index, mu,label="MU")
plt.plot(data.index, ru, label="RU")
plt.title('Scatter Plot')
plt.xlabel('Time (s)')
plt.ylabel('Pressure')

# Calculate and plot a linear regression line
#m, b = np.polyfit(lb, df_time, 1)
#plt.plot(lb, m*lb + b, color='red')

# Display some statistics on the plot
textstr = (f'Mean LB: {mean_lb:.2f}\nMean RB: {mean_rb:.2f}\nMean LM: {mean_lm:.2f}\nMean RM: {mean_rm:.2f}\nMean LU: {mean_lu:.2f}\nMean RU: {mean_ru:.2f}\n'
f'Std Dev LB: {std_dev_lb:.2f}\nStd Dev RB: {std_dev_rb:.2f}\nStd Dev LM: {std_dev_lm:.2f}\nStd Dev RM: {std_dev_rm:.2f}\nStd Dev LU: {std_dev_lu:.2f}\nStd Dev RU: {std_dev_ru:.2f}\n')
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.grid(True)
# Save the plot to a file
plt.savefig('scatter_plot.png')
plt.legend(loc="upper left")
# Show the plot
plt.show()
# %%
#Plot filtered
window_size = 100
order = 3

lb_filtered = savgol_filter(lb,window_size,order)
mb_filtered = savgol_filter(mb,window_size,order)
rb_filtered = savgol_filter(rb,window_size,order)
lm_filtered = savgol_filter(lm,window_size,order)
mm_filtered = savgol_filter(mm,window_size,order)
rm_filtered = savgol_filter(rm,window_size,order)
lu_filtered = savgol_filter(lu,window_size,order)
mu_filtered = savgol_filter(mu,window_size,order)
ru_filtered = savgol_filter(ru,window_size,order)

plt.plot(data.index,lb_filtered,label='LB')
plt.plot(data.index,mb_filtered,label='MB')
plt.plot(data.index,rb_filtered,label='RB')
plt.plot(data.index,lm_filtered,label='LM')
plt.plot(data.index,mm_filtered,label='MM')
plt.plot(data.index,rm_filtered,label='RM')
plt.plot(data.index,lu_filtered,label='LU')
plt.plot(data.index,mu_filtered,label='MU')
plt.plot(data.index,ru_filtered,label='RU')
plt.grid(b=True)
plt.legend(loc='upper left')
plt.show()


#%%
# Extract the columns that we want to plot



# Calculate some basic statistics on the data
mean_x = np.mean(lb)
mean_y = np.mean(rb)
std_dev_x = np.std(lb)
std_dev_y = np.std(rb)

# Create a scatter plot of the data

data.reset_index().plot.scatter(x="index",y='LB')
#plt.scatter(data.index, rb)
plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Calculate and plot a linear regression line
#m, b = np.polyfit(lb, df_time, 1)
#plt.plot(lb, m*lb + b, color='red')

# Display some statistics on the plot
textstr = (f'Mean X: {mean_x:.2f}\nMean Y: {mean_y:.2f}\n'
           f'Std Dev X: {std_dev_x:.2f}\nStd Dev Y: {std_dev_y:.2f}')
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

# Save the plot to a file
plt.savefig('scatter_plot.png')

# Show the plot
plt.show()
# %%

#Apply filter

