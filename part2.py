Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
import joblib
sns.set_style("whitegrid")
gdp = pd.read_csv("GDPC1.csv", parse_dates=["observation_date"])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    gdp = pd.read_csv("GDPC1.csv", parse_dates=["observation_date"])
  File "D:\py\python\Lib\site-packages\pandas\io\parsers\readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "D:\py\python\Lib\site-packages\pandas\io\parsers\readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "D:\py\python\Lib\site-packages\pandas\io\parsers\readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "D:\py\python\Lib\site-packages\pandas\io\parsers\readers.py", line 1880, in _make_engine
    self.handles = get_handle(
  File "D:\py\python\Lib\site-packages\pandas\io\common.py", line 873, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'GDPC1.csv'
gdp = pd.read_csv(r"C:\Users\Administrator\Desktop\GDPC1.csv", parse_dates=["observation_date"])
gdp.rename(columns={"observation_date": "Date", "GDPC1": "GDP"}, inplace=True)
gdp.sort_values("Date", inplace=True)
unrate = pd.read_csv(r"C:\Users\Administrator\Desktop\UNRATE.csv", parse_dates=["observation_date"])
unrate.rename(columns={"observation_date": "Date"}, inplace=True)
unrate.sort_values("Date", inplace=True)
infl = pd.read_csv(r"C:\Users\Administrator\Desktop\FPCPITOTLZGUSA.csv", parse_dates=["observation_date"])
infl.rename(columns={"observation_date": "Date"}, inplace=True)
infl.sort_values("Date", inplace=True)
fedfunds = pd.read_csv(r"C:\Users\Administrator\Desktop\FEDFUNDS.csv", parse_dates=["observation_date"])
fedfunds.rename(columns={"observation_date": "Date"}, inplace=True)
fedfunds.sort_values("Date", inplace=True)
df_merged = pd.merge(gdp, unrate, on="Date", how="inner")
df_merged = pd.merge(df_merged, infl, on="Date", how="inner")
df_merged = pd.merge(df_merged, fedfunds, on="Date", how="inner")
df_merged.rename(columns={
    "UNRATE": "UnemploymentRate",
    "FPCPITOTLZGUSA": "Inflation",
    "FEDFUNDS": "FedFundsRate"
}, inplace=True)
df_merged.sort_values("Date", inplace=True)
df_merged.reset_index(drop=True, inplace=True)
print("Data after merging:")
Data after merging:
print(df_merged.head(10))
        Date       GDP  UnemploymentRate  Inflation  FedFundsRate
0 1960-01-01  3517.181               5.2   1.457976          3.99
1 1961-01-01  3493.703               6.6   1.070724          1.45
2 1962-01-01  3758.147               5.8   1.198773          2.15
3 1963-01-01  3893.482               5.7   1.239669          2.92
4 1964-01-01  4135.553               5.6   1.278912          3.48
5 1965-01-01  4362.111               4.9   1.585169          3.90
6 1966-01-01  4731.888               4.0   3.015075          4.42
7 1967-01-01  4870.299               3.9   2.772786          4.94
8 1968-01-01  5057.553               3.7   4.271796          4.61
9 1969-01-01  5283.597               3.4   5.462386          6.30
print("\nData shape:", df_merged.shape)

Data shape: (64, 5)
df_merged.dropna(inplace=True)
print("\nData shape after dropping NA:", df_merged.shape)

Data shape after dropping NA: (64, 5)
print("\nDate range:", df_merged["Date"].min(), "to", df_merged["Date"].max())

Date range: 1960-01-01 00:00:00 to 2023-01-01 00:00:00
X = df_merged[["UnemploymentRate", "Inflation", "FedFundsRate"]]
y = df_merged["GDP"]
print("Feature summary:")
Feature summary:
print(X.describe())
       UnemploymentRate  Inflation  FedFundsRate
count         64.000000  64.000000     64.000000
mean           5.881250   3.770332      4.712500
std            1.599988   2.762789      3.748391
min            3.400000  -0.355546      0.070000
25%            4.700000   1.876588      1.685000
50%            5.700000   3.021948      4.375000
75%            6.625000   4.399866      6.497500
max           10.400000  13.549202     19.080000
print("\nTarget summary (GDP):")

Target summary (GDP):
print("\nTarget summary (GDP):")

Target summary (GDP):
print(y.describe())
count       64.000000
mean     11319.421438
std       5624.681697
min       3493.703000
25%       6267.051250
50%      10141.910500
75%      16411.053750
max      22403.435000
Name: GDP, dtype: float64
>>> X_train, X_test, y_train, y_test = train_test_split(
...     x,y,
...     test_size=0.3
...     random_state=222
...     
SyntaxError: '(' was never closed
>>> X_train, X_test, y_train, y_test = train_test_split(
...     x,y,
...     test_size=0.3
...     random_state=222
...     
SyntaxError: '(' was never closed
>>> print("Training set size:", X_train.shape)
...     
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print("Training set size:", X_train.shape)
NameError: name 'X_train' is not defined
>>> from sklearn.model_selection import train_test_split
...     
>>> X_train, X_test, y_train, y_test = train_test_split(
...     X, y,
...     test_size=0.3,
...     random_state=222
... )
...     
>>> print("Training set size:", X_train.shape)
...     
Training set size: (44, 3)
>>> print("Test set size:", X_test.shape)
...     
Test set size: (20, 3)
