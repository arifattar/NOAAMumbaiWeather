import pandas as pd
import numpy as np
from numpy import nanmean

#colaba_df = pd.read_csv('IN012070300.csv')

santacruz_df = pd.read_csv('IN012070800.csv')
print(santacruz_df)
#print(santacruz_df.columns)

santacruz_df = santacruz_df[['STATION', 'DATE', 'PRCP', 'TMAX', 'TMIN', 'TAVG']]
print(santacruz_df)

year = list()
month = list()
date = list()
for day in santacruz_df['DATE']:
    split_date = day.split('-')
    year.append(split_date[0])
    month.append(split_date[1])
    date.append(split_date[2])



santacruz_df['YEAR'] = year
santacruz_df['MONTH'] = month
santacruz_df['DAY'] = date
print(santacruz_df)


santacruz_df = santacruz_df[(santacruz_df['YEAR'] >= '1971')]
print(santacruz_df)


#Plotting yearly average temperature from 1971-2019

yearly_avg_temp = santacruz_df.groupby(['YEAR'])['TAVG'].agg(AVERAGE = 'mean')
print(yearly_avg_temp)



from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
fig = Figure()
canvas = FigureCanvas(fig)

ax = fig.add_subplot(111)

ax.scatter(yearly_avg_temp.index, yearly_avg_temp.values)

for ticks in ax.get_xticklabels():
    ticks.set_rotation(90)



labels = ['26.0', '26.5', '27.0', '27.5', '28.0', '28.5', '29.0']
ax.set_yticklabels(labels)

# add a label to the x axis
#ax.set_xlabel('Year')
# add a label to the y axis
ax.set_ylabel('Temperature in Celsius')
# add a title
ax.set_title('Yearly Average Temperatures measured in Santacruz, Bombay for the years 1973-2019')

[s.set_visible(False) for s in ax.spines.values()]


DefaultSize = fig.get_size_inches()

fig.set_size_inches( (DefaultSize[0]*1.5, DefaultSize[1]*1.5) )



fig.savefig('weatherplot.png')


#Plotting daily average temperatures over different decades

santacruz_df80s = santacruz_df[(santacruz_df['YEAR'] >='1980') & (santacruz_df['YEAR'] < '1990')]
print(santacruz_df80s)

santacruz_df80s = santacruz_df80s.drop(santacruz_df80s[(santacruz_df80s['MONTH'] == '02') & (santacruz_df80s['DAY'] == '29')].index)

daily_avg_80s = santacruz_df80s.groupby(['MONTH', 'DAY'])['TAVG'].agg(AVERAGE = 'mean').reset_index()
print(daily_avg_80s)


santacruz_df90s = santacruz_df[(santacruz_df['YEAR'] >='1990') & (santacruz_df['YEAR'] < '2000')]
print(santacruz_df90s)

santacruz_df90s = santacruz_df90s.drop(santacruz_df90s[(santacruz_df90s['MONTH'] == '02') & (santacruz_df90s['DAY'] == '29')].index)

daily_avg_90s = santacruz_df90s.groupby(['MONTH', 'DAY'])['TAVG'].agg(AVERAGE = 'mean').reset_index()
print(daily_avg_90s)



santacruz_df00s = santacruz_df[(santacruz_df['YEAR'] >='2000') & (santacruz_df['YEAR'] < '2010')]
print(santacruz_df00s)

santacruz_df00s = santacruz_df00s.drop(santacruz_df00s[(santacruz_df00s['MONTH'] == '02') & (santacruz_df00s['DAY'] == '29')].index)

daily_avg_00s = santacruz_df00s.groupby(['MONTH', 'DAY'])['TAVG'].agg(AVERAGE = 'mean').reset_index()
print(daily_avg_00s)


fig1 = Figure()
canvas1 = FigureCanvas(fig1)

ax1 = fig1.add_subplot(111)

ax1.plot(daily_avg_80s['AVERAGE'], label = 'Daily average temperature 1980-1989')
#ax1.plot(daily_avg_90s['AVERAGE'])
ax1.plot(daily_avg_00s['AVERAGE'], label = 'Daily average temperature 2000-2009')


ax1.set_xlabel('Day of the Year')
# add a label to the y axis
ax1.set_ylabel('Temperature in 10th of Celsius')
# add a title
ax1.set_title('Daily Average Temperatures measured in Santacruz, Bombay for the years 1980-1989 and 2000-2009')

[s.set_visible(False) for s in ax1.spines.values()]

ax1.legend(loc='best', frameon = False, fontsize='small')

DefaultSize = fig1.get_size_inches()

fig1.set_size_inches( (DefaultSize[0]*1.5, DefaultSize[1]*1.5) )



fig1.savefig('dailyaveragedecade.png')


#Plotting monthly average precipitation over 3 different decades

daily_pavg_80s = santacruz_df80s.groupby(['MONTH', 'DAY'])['PRCP'].agg(AVERAGE = 'mean').reset_index()
daily_pavg_80s = daily_pavg_80s.groupby(['MONTH'])['AVERAGE'].agg(PAVERAGE = 'mean').reset_index()
daily_pavg_80s = daily_pavg_80s.set_index(['MONTH'])
print(daily_pavg_80s)

daily_pavg_90s = santacruz_df90s.groupby(['MONTH', 'DAY'])['PRCP'].agg(AVERAGE = 'mean').reset_index()
daily_pavg_90s = daily_pavg_90s.groupby(['MONTH'])['AVERAGE'].agg(PAVERAGE = 'mean').reset_index()
daily_pavg_90s = daily_pavg_90s.set_index(['MONTH'])
print(daily_pavg_90s)

daily_pavg_00s = santacruz_df00s.groupby(['MONTH', 'DAY'])['PRCP'].agg(AVERAGE = 'mean').reset_index()
daily_pavg_00s = daily_pavg_00s.groupby(['MONTH'])['AVERAGE'].agg(PAVERAGE = 'mean').reset_index()
daily_pavg_00s = daily_pavg_00s.set_index(['MONTH'])
print(daily_pavg_00s)




fig2 = Figure()
canvas2 = FigureCanvas(fig2)

ax2 = fig2.add_subplot(111)

#ax1.plot(daily_avg_80s['AVERAGE'], label = 'Daily average temperature 1980-1989')
#ax1.plot(daily_avg_90s['AVERAGE'])

ax2.plot(daily_pavg_80s, label = 'Daily average precipitation 1980-1989')

ax2.plot(daily_pavg_90s, label = 'Daily average precipitation 1990-1999')

ax2.plot(daily_pavg_00s, label = 'Daily average precipitation 2000-2009')


ax2.set_xlabel('Month of the Year')
# add a label to the y axis
ax2.set_ylabel('Precipitation in 10ths of mm')
# add a title
ax2.set_title('Monthly Average Precipitation measured in Santacruz, Bombay for the three different decades')

[s.set_visible(False) for s in ax2.spines.values()]

ax2.legend(loc='best', frameon = False, fontsize='small')

DefaultSize = fig2.get_size_inches()

fig2.set_size_inches( (DefaultSize[0]*1.5, DefaultSize[1]*1.5) )

fig2.savefig('dailyprecaveragedecade.png')
