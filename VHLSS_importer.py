# Reading the VHLSS 2010/2012/2014 survey data into a Python Pandas dataframe
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.style.use('ggplot')

datadir = '../data/'


#%% VHLSS surveys data

survey = pd.read_stata(datadir + 'Processed_data/VNHH_energy_2008-2014.dta')


def clip(s):
    return s.clip(0, s.quantile(0.9999))


survey.elec_last_month = clip(survey.elec_last_month)
survey.kwh_last_month = clip(survey.kwh_last_month)
survey.elec_year = clip(survey.elec_year)
survey.inc = clip(survey.inc)
survey.inc_ave = clip(survey.inc_ave)
survey['size'] = clip(survey['size'])
survey.sq_m = clip(survey.sq_m)
survey.assets = clip(survey.assets)

# Relabel in English
# tcvn3 encoding is not supported in python3 / Ubuntu 16.04
# http://sametmax.com/lencoding-en-python-une-bonne-fois-pour-toute/
survey.elec_poor.cat.categories = ["Lacking", "Enough", "Plenty", "Idk", "Missing"]
survey.main_light.cat.categories = ["Main_Grid", "Local_Elec", "Flame", "Other"]
survey.urb_rur.cat.categories = ["Urban", "Rural"]
survey.grid_presence.cat.categories = ['Present', 'Absent', 'Missing']
survey.elec_presence.cat.categories = ['Present', 'Absent']
survey.inc_pov.cat.categories = ['Yes', 'No']
survey.rent.cat.categories = ['Pay', 'DoNoPay']
survey.gender.cat.categories = ['Male', 'Female']


#%%% Color scheme from colorbrewer2.org

curve_style = {2014: {'color': '#b30000', 'linestyle': 'solid'},
               2012: {'color': '#e34a33', 'linestyle': 'dashed'},
               2010: {'color': '#fc8d59', 'linestyle': 'dashdot'},
               2008: {'color': '#fdcc8a', 'linestyle': 'solid'}
               }


#%% EVN tariff to households

electricity_tariffs = pd.read_csv(datadir + 'Processed_data/elec_price.csv',
                                  parse_dates=True,
                                  index_col=[0])

block_limits = [0, 30, 50, 100, 150, 200, 300, 400, 10000]

# The 2013 tariff didn't use the block at 30 kWh, have to add it
tariff_2013 = electricity_tariffs.ix['2013-08-01']
block_prices_2013 = np.insert(tariff_2013.values, 0, [0, tariff_2013[0]])

# Illustrative more progressive tariff, source: author
block_prices_alt = [0, 0, 1925, 1925, 1925, 2500, 2500, 3500, 3500]


#%% Inflation data

# https://www.gso.gov.vn/default_en.aspx?tabid=780
# Monthly consumer price index by Months and Year
# Year 2000 = 100
CPI = pd.DataFrame([104.30, 107.60,	115.90, 125.50, 134.90, 146.30, 179.64, 192.00, 209.64, 248.60, 271.49, 289.41, 301.26, 303.16],
                   index=pd.date_range('2002-01-01', periods=14, freq='A-JAN'),
                   columns=['Consumer_Price_Index']
                   )


#%%
# Gini code lifted from :
# https://planspacedotorg.wordpress.com/2013/06/21/how-to-calculate-gini-coefficient-from-raw-data-in-python/

def gini(list_of_values):
    sorted_list = sorted(list_of_values)
    height, area = 0, 0
    for value in sorted_list:
        height += value
        area += height - value / 2
    fair_area = height * len(list_of_values) / 2
    return (fair_area - area) / fair_area


# Not efficient alternative, usefull for double checking
# https://en.wikipedia.org/wiki/Gini_coefficient#Calculation
def relative_mean_absolute_difference(l):
    n = len(l)
    a = np.array(l)
    den = 2 * n * sum(l)
    num = 0
    for i in np.nditer(a):
        num += sum(abs(a - i))
    return num / den


#%%

provinces = pd.read_stata(datadir + 'VNM_adm_shp/ma_tinh_convert.dta')

provinceTinhByName = dict(zip(provinces.VARNAME_1, provinces.tinh))
provinceNameByTinh = dict(zip(provinces.tinh, provinces.VARNAME_1))

provinceNameByID1 = dict(zip(provinces.ID_1, provinces.VARNAME_1))
provinceID1ByName = dict(zip(provinces.VARNAME_1, provinces.ID_1))

provinceID1ByTinh = dict(zip(provinces.tinh, provinces.ID_1))
provinceTinhByID1 = dict(zip(provinces.ID_1, provinces.tinh))
