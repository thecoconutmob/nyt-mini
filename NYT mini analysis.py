import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly.io as pio
from datetime import datetime




plt.style.use('seaborn-darkgrid')
data = pd.read_excel('/Users/marlinspike/Desktop/mini.xls', index_col = 'Day',
                     parse_dates = True)

columns = list(data)[1:]
working_df = data[columns]

rows = ['Average Time in Seconds', 'Number of Times Recorded', 'Best Time',
        'Worst Time', 'Times Shiv has beaten Rahul']

means, counts, mins, maxes = ([] for i in range(0,4))

for column, i in zip(working_df, range(len(columns))):
     means.append(data[column].mean())
     counts.append(data[column].count())
     mins.append(data[column].min())
     maxes.append(data[column].max())

win_count = 0
for i in range(len(data)):
    if data.iloc[i,2] < data.iloc[i,1]:
        win_count += 1

wins = [win_count, win_count, win_count, win_count, win_count]

values = [means, counts, mins, maxes, wins]


stats = pd.DataFrame(values, index=rows, columns=columns)
stats = stats.astype(float).round(1)

fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

ax.table(cellText=stats.values, colLabels=stats.columns,
         rowLabels = stats.index, loc='center')
fig.tight_layout()
plt.show()

data = data.fillna(data.mean())

df_long=pd.melt(data, id_vars=['Date'], value_vars=['Rahul', 'Priya', 'Shiv',
'Nick', 'Himi'])

fig = px.line(df_long, x='Date', y='value', color = 'variable')
fig.update_yaxes(title = 'Time (seconds)')
fig.update_layout({'legend_title_text':''})
pio.write_html(fig, file = 'index.html', auto_open=True)

