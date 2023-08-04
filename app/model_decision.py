# -*- coding: utf-8 -*-
# @Time    : 2023/4/14 1:39 PM
# @Author  : jiangmin5
# @Email   : jiangmin5@longfor.com
# @File    : model_decision.py
# @Software: PyCharm

#
from datetime import datetime
from pandas import Series
from sklearn.metrics import mean_squared_error
from math import sqrt
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA

import pandas as pd
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', 1000)
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateLocator, DateFormatter
import numpy as np
import pandas_profiling as pp
import seaborn as sns
import matplotlib.dates as mdates
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler,MinMaxScaler
import math
from sklearn.neighbors import LocalOutlierFactor


def dataset_etl():
    df1w = pd.read_csv("/Users/jiangmin5/Downloads/month2.csv")
    pass


def model1_rel():
    pass


def decision1_rel(is_remove_maxmin_n, line_type1, line_type2):
    """
    param
    is_remove_maxmin_n: 0
    line_type: mean
    """
    pass
    return {"No. of bad projects": 7,
            "No. of good projects": 6,
            "bad projects": [],
            "good projects": [],
            "recommendation reasons": "超过费效{}线以上; 同时超过签约占比{}线".format(line_type1, line_type2)
            }


def decision2_rel():
    pass
    return {"bad projects":[],
            "medium projects": [],
            "good projects": [],
    }


import plotly.graph_objs as go
import numpy as np

# Generate some random data
x1 = step1_anomoly_ana["基础渠道签约占比"]
y1 = step1_anomoly_ana["基础渠道费效"]

# Calculate the quartile values for the x and y axes
x1_q3 = np.quantile(x1, 0.75)
y1_q3 = np.quantile(y1, 0.75)

# Create the scatter trace
trace = go.Scatter(x=x1, y=y1, mode='markers')

# Create the x quartile line
x_q3_line = go.Scatter(x=[x1_q3, x1_q3], y=[np.min(y1), np.max(y1)],
                       mode='lines', line=dict(color='green'))

# Create the y quartile line
y_q3_line = go.Scatter(x=[np.min(x1), np.max(x1)], y=[y1_q3, y1_q3],
                       mode='lines', line=dict(color='green'), )







