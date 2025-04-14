Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\Administrator\Desktop\RSXFSN.csv")
data.sort_values('observation_date', inplace=True)
print("First few rows of the raw data:")
First few rows of the raw data:
print(data.head())
    observation_date  RSXFSN  CPIAUCSL
96            1/1/00  213709     169.3
108           1/1/01  226791     175.6
120           1/1/02  230546     177.7
132           1/1/03  242271     182.6
144           1/1/04  252818     186.3
print()

data['date'] = pd.to_datetime(data['observation_date'], format='%m/%d/%y')
data = data.sort_values('date')
data_2024 = data[data['date'].dt.year == 2024]
print("\n2024 data count:", len(data_2024))

2024 data count: 12
if not data_2024.empty:
    last_record = data_2024.iloc[-1]
    print("\nLast CPI value in 2024:")
    print(f"Date: {last_record['observation_date']}")
    print(f"CPI value: {last_record['CPIAUCSL']}")
else:
    print("\nNo data found for 2024")
data_2024 = data[(data['observation_date'] >= '2024-01-01') & (data['observation_date'] < '2025-01-01')]
SyntaxError: invalid syntax
data['Real_Sales'] = data['RSXFSN'] * (baseCPI / data['CPIAUCSL'])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    data['Real_Sales'] = data['RSXFSN'] * (baseCPI / data['CPIAUCSL'])
NameError: name 'baseCPI' is not defined
data_2024 = data[data['date'].dt.year == 2024]
last_record_2024 = data_2024.iloc[-1]
baseCPI = last_record_2024['CPIAUCSL']
print(f"Base CPI (December 2024): {baseCPI}")
Base CPI (December 2024): 317.603
data['Real_Sales'] = data['RSXFSN'] * (baseCPI / data['CPIAUCSL'])
print("\nFirst 5 rows with Real Sales:")

First 5 rows with Real Sales:
print(data.head())
  observation_date  RSXFSN  CPIAUCSL       date     Real_Sales
0           1/1/92  130683     138.3 1992-01-01  300110.721974
1           2/1/92  131244     138.6 1992-02-01  300746.667619
2           3/1/92  142488     139.1 1992-03-01  325338.722243
3           4/1/92  147175     139.4 1992-04-01  335317.227582
4           5/1/92  152420     139.7 1992-05-01  346521.469291
data['Days_in_Month'] = data['observation_date'].dt.days_in_month
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    data['Days_in_Month'] = data['observation_date'].dt.days_in_month
  File "D:\py\python\Lib\site-packages\pandas\core\generic.py", line 6299, in __getattr__
    return object.__getattribute__(self, name)
  File "D:\py\python\Lib\site-packages\pandas\core\accessor.py", line 224, in __get__
    accessor_obj = self._accessor(obj)
  File "D:\py\python\Lib\site-packages\pandas\core\indexes\accessors.py", line 643, in __new__
    raise AttributeError("Can only use .dt accessor with datetimelike values")
AttributeError: Can only use .dt accessor with datetimelike values. Did you mean: 'at'?
data['Days_in_Month'] = data['date'].dt.days_in_monthdata['Days_in_Month'] = data['observation_date'].dt.days_in_month
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    data['Days_in_Month'] = data['observation_date'].dt.days_in_month
  File "D:\py\python\Lib\site-packages\pandas\core\generic.py", line 6299, in __getattr__
    return object.__getattribute__(self, name)
  File "D:\py\python\Lib\site-packages\pandas\core\accessor.py", line 224, in __get__
    accessor_obj = self._accessor(obj)
  File "D:\py\python\Lib\site-packages\pandas\core\indexes\accessors.py", line 643, in __new__
    raise AttributeError("Can only use .dt accessor with datetimelike values")
AttributeError: Can only use .dt accessor with datetimelike values. Did you mean: 'at'?
SyntaxError: multiple statements found while compiling a single statement
data['date'] = pd.to_datetime(data['observation_date'], format='%m/%d/%y')
data['Days_in_Month'] = data['date'].dt.days_in_month
print(data.dtypes)
observation_date            object
RSXFSN                       int64
CPIAUCSL                   float64
date                datetime64[ns]
Real_Sales                 float64
Days_in_Month                int32
dtype: object
df = data.set_index('observation_date').sort_index()
ts_data = df['Sales_per_Day'].asfreq('MS')
Traceback (most recent call last):
  File "D:\py\python\Lib\site-packages\pandas\core\indexes\base.py", line 3805, in get_loc
    return self._engine.get_loc(casted_key)
  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Sales_per_Day'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    ts_data = df['Sales_per_Day'].asfreq('MS')
  File "D:\py\python\Lib\site-packages\pandas\core\frame.py", line 4102, in __getitem__
    indexer = self.columns.get_loc(key)
  File "D:\py\python\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: 'Sales_per_Day'
data['Real_Sales'] = data['RSXFSN'] * (baseCPI / data['CPIAUCSL'])df = data.set_index('observation_date').sort_index()
ts_data = df['Sales_per_Day'].asfreq('MS')
Traceback (most recent call last):
  File "D:\py\python\Lib\site-packages\pandas\core\indexes\base.py", line 3805, in get_loc
    return self._engine.get_loc(casted_key)
  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Sales_per_Day'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    ts_data = df['Sales_per_Day'].asfreq('MS')
  File "D:\py\python\Lib\site-packages\pandas\core\frame.py", line 4102, in __getitem__
    indexer = self.columns.get_loc(key)
  File "D:\py\python\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: 'Sales_per_Day'df = data.set_index('date').sort_index()
SyntaxError: invalid syntax
df = data.set_index('date').sort_index()
ts_data = df['Sales_per_Day'].asfreq('MS')  # 'MS' means month start frequency
Traceback (most recent call last):
  File "D:\py\python\Lib\site-packages\pandas\core\indexes\base.py", line 3805, in get_loc
    return self._engine.get_loc(casted_key)
  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Sales_per_Day'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    ts_data = df['Sales_per_Day'].asfreq('MS')  # 'MS' means month start frequency
  File "D:\py\python\Lib\site-packages\pandas\core\frame.py", line 4102, in __getitem__
    indexer = self.columns.get_loc(key)
  File "D:\py\python\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: 'Sales_per_Day'
data['date'] = pd.to_datetime(data['observation_date'], format='%m/%d/%y')
data_2024 = data[data['date'].dt.year == 2024]
last_record_2024 = data_2024.iloc[-1]
baseCPI = last_record_2024['CPIAUCSL']
print(f"Base CPI (December 2024): {baseCPI}")
Base CPI (December 2024): 317.603
data['Real_Sales'] = data['RSXFSN'] * (baseCPI / data['CPIAUCSL'])
data['Days_in_Month'] = data['date'].dt.days_in_month
data['Sales_per_Day'] = data['Real_Sales'] / data['Days_in_Month']
df = data.set_index('date').sort_index()
ts_data = df['Sales_per_Day'].asfreq('MS')
print("\nFirst 5 rows of time series data:")

First 5 rows of time series data:
print(ts_data.head())
date
1992-01-01     9680.991031
1992-02-01    10370.574745
1992-03-01    10494.797492
1992-04-01    11177.240919
1992-05-01    11178.111913
Freq: MS, Name: Sales_per_Day, dtype: float64
ts_data.head(12)
date
1992-01-01     9680.991031
1992-02-01    10370.574745
1992-03-01    10494.797492
1992-04-01    11177.240919
1992-05-01    11178.111913
1992-06-01    11474.589090
1992-07-01    11126.569018
1992-08-01    11094.857732
1992-09-01    11116.330091
1992-10-01    11278.243258
1992-11-01    11534.733022
1992-12-01    13776.524209
Freq: MS, Name: Sales_per_Day, dtype: float64
print(ts_data)
date
1992-01-01     9680.991031
1992-02-01    10370.574745
1992-03-01    10494.797492
1992-04-01    11177.240919
1992-05-01    11178.111913
                  ...     
2024-10-01    20551.715478
2024-11-01    21476.333548
2024-12-01    22704.258065
2025-01-01    18496.247425
2025-02-01    19574.847262
Freq: MS, Name: Sales_per_Day, Length: 398, dtype: float64
plt.figure(figsize=(10, 4))
<Figure size 1000x400 with 0 Axes>
plt.plot(ts_data, label='Sales per Day (2017 $)')
[<matplotlib.lines.Line2D object at 0x0000020CD12BCA50>]
plt.title("Time Plot of Inflation-Adjusted, Day-Standardized Retail Sales")
Text(0.5, 1.0, 'Time Plot of Inflation-Adjusted, Day-Standardized Retail Sales')
plt.xlabel("Date")
Text(0.5, 0, 'Date')
plt.ylabel("Sales per Day")
Text(0, 0.5, 'Sales per Day')
plt.legend()
<matplotlib.legend.Legend object at 0x0000020CD168DF90>
plt.show()
ts_data_diff = ts_data.diff().dropna()
plt.figure(figsize=(10, 4))
<Figure size 1000x400 with 0 Axes>
plt.plot(ts_data_diff, color='orange', label='First Difference of Sales per Day')
[<matplotlib.lines.Line2D object at 0x0000020CD2234F90>]
plt.title("First-Differenced Series")
Text(0.5, 1.0, 'First-Differenced Series')
plt.xlabel("Date")
Text(0.5, 0, 'Date')
plt.ylabel("Diff(Sales per Day)")
Text(0, 0.5, 'Diff(Sales per Day)')
plt.legend()
<matplotlib.legend.Legend object at 0x0000020CD223D110>
plt.show()
import calendar
import seaborn as sns
df = ts_data_diff.to_frame(name='value')
df['month'] = df.index.month
df['year'] = df.index.year
df['month_name'] = df.index.month_name()
pivoted = df.pivot(index='month', columns='year', values='value')
pivoted.index = [calendar.month_name[m] for m in pivoted.index]
plt.figure(figsize=(10, 6))
<Figure size 1000x600 with 0 Axes>
for year in pivoted.columns:
    plt.plot(pivoted.index, pivoted[year], label=year)
plt.title("Seasonal Plot of Retail Sales")
SyntaxError: invalid syntax
     plt.title("Seasonal Plot of Retail Sales")
     
SyntaxError: unexpected indent
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
<Figure size 1000x600 with 0 Axes>
plt.title("Seasonal Plot of Retail Sales")
Text(0.5, 1.0, 'Seasonal Plot of Retail Sales')
plt.xlabel("Month")
Text(0.5, 0, 'Month')
plt.ylabel("Real Sales per Day")
Text(0, 0.5, 'Real Sales per Day')
plt.grid(True)
plt.plot(ts_data)
[<matplotlib.lines.Line2D object at 0x0000020CD78858D0>]
plt.show()
plt.title("Seasonal Plot of Retail Sales")
Text(0.5, 1.0, 'Seasonal Plot of Retail Sales')
plt.xlabel("Month")
Text(0.5, 0, 'Month')
plt.ylabel("Sales per Day")
Text(0, 0.5, 'Sales per Day')
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')

Warning (from warnings module):
  File "<pyshell#91>", line 1
UserWarning: No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
<matplotlib.legend.Legend object at 0x0000020CDAC0EAD0>
df = ts_data_diff.to_frame(name='value')Warning (from warnings module):
  File "<pyshell#91>", line 1
UserWarning: No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
<matplotlib.legend.Legend object at 0x0000020CDAC0EAD0>
SyntaxError: invalid syntax
if not pivoted.empty:
    plt.figure(figsize=(10, 6))
    for year in pivoted.columns:
        plt.plot(pivoted.index, pivoted[year], label=year)
        plt.title("Seasonal Plot of Retail Sales")
        plt.xlabel("Month")
        plt.ylabel("Sales per Day")
        plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()
    else:
        print("Pivoted DataFrame is empty, cannot plot.")
g = sns.FacetGrid(df, col='month_name', col_wrap=4, sharey=True, height=3)
SyntaxError: invalid syntax
g = sns.FacetGrid(df, col='month_name', col_wrap=4, sharey=True, height=3)
g.map_dataframe(sns.lineplot, x='year', y='value', marker='o')
<seaborn.axisgrid.FacetGrid object at 0x0000020CD7BF5990>
def plot_monthly_mean(data, **kwargs):
    plt.axhline(y=data['value'].mean(), color='black', linestyle='--', linewidth=1)
g.map_dataframe(plot_monthly_mean)
SyntaxError: invalid syntax
g.map_dataframe(plot_monthly_mean)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    g.map_dataframe(plot_monthly_mean)
NameError: name 'plot_monthly_mean' is not defined
def plot_monthly_mean(data, **kwargs):
    sns.lineplot(x='month', y='value', data=data, **kwargs)
g = sns.FacetGrid(df, col="year", col_wrap=4)
SyntaxError: invalid syntax
g = sns.FacetGrid(df, col="year", col_wrap=4)
g.map_dataframe(plot_monthly_mean)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    g.map_dataframe(plot_monthly_mean)
NameError: name 'plot_monthly_mean' is not defined
g.map_dataframe(plot_monthly_mean)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    g.map_dataframe(plot_monthly_mean)
NameError: name 'plot_monthly_mean' is not defined
print("Checking function existence:", 'plot_monthly_mean' in globals())
Checking function existence: False
import seaborn as sns
def plot_monthly_mean(data, **kwargs):
    print("Function plot_monthly_mean is running!")
    sns.lineplot(x='month', y='value', data=data, **kwargs)
print("Checking function existence:", 'plot_monthly_mean' in globals())
SyntaxError: invalid syntax
print("Checking function existence:", 'plot_monthly_mean' in globals())
Checking function existence: False
g.set_axis_labels("Year", "Sales per Day")
<seaborn.axisgrid.FacetGrid object at 0x0000020CA7479890>
g.set_titles("{col_name}")
<seaborn.axisgrid.FacetGrid object at 0x0000020CA7479890>
plt.tight_layout()
plt.show()
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(ts_data, model='additive', period=12)
fig = result.plot()
fig.set_size_inches(10, 8)
plt.tight_layout()
plt.show()
from statsmodels.graphics.tsaplots import plot_acf
>>> import scipy.stats as stats
>>> def check_residuals_snaive(residuals, method_name="Seasonal naive"):
...     if not isinstance(residuals, pd.Series):
...         residuals = pd.Series(residuals)
...     fig = plt.figure(figsize=(10, 6))
...     gs = fig.add_gridspec(2, 2, height_ratios=[2, 1])
...     ax1 = fig.add_subplot(gs[0, :])
...     ax1.plot(residuals, label='Residuals', color='black')
...     ax1.axhline(y=0, color='red', linestyle='--', linewidth=1)
...     ax1.set_title(f'Residuals from {method_name} method')
...     ax1.legend()
...     ax2 = fig.add_subplot(gs[1, 0])
...     plot_acf(residuals.dropna(), ax=ax2, lags=11)
...     ax2.set_title('ACF')
...     ax3 = fig.add_subplot(gs[1, 1])
...     sns.histplot(residuals, ax=ax3, color='gray', kde=False, stat='density')
...     mu, sigma = stats.norm.fit(residuals.dropna())
...     x = np.linspace(residuals.min(), residuals.max(), 100)
...     pdf = stats.norm.pdf(x, mu, sigma)
...     ax3.plot(x, pdf, 'r-', label=f'N({mu:.2f}, {sigma:.2f}^2)')
...     ax3.set_title('Histogram of Residuals')
...     ax3.legend()
...     plt.tight_layout()
...     plt.show()
... snaive_in_sample = ts_data.shift(12)
SyntaxError: invalid syntax
>>> snaive_in_sample = ts_data.shift(12)
>>> residuals_snaive_all = ts_data[12:] - snaive_in_sample[12:]
>>> check_residuals_snaive(residuals_snaive_all)
... 
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    check_residuals_snaive(residuals_snaive_all)
NameError: name 'check_residuals_snaive' is not defined
>>> check_residuals_snaive(residuals_snaive_all)
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    check_residuals_snaive(residuals_snaive_all)
NameError: name 'check_residuals_snaive' is not defined
