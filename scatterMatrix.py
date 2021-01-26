# Reading the VHLSS 2010/2012/2014 survey data into a Python Pandas dataframe
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

import matplotlib.pyplot as plt
import pandas as pd

from VHLSS_importer import survey

plt.figure(figsize=(20, 20))

pd.scatter_matrix(survey.loc[survey.year == 2014,
                             ['elec_last_month',
                              'kwh_last_month',
                              'elec_year',
                              'inc',
                              'inc_ave',
                              'size',
                              'edu_max',
                              'sq_m',
                              'assets']],
                  figsize=(10, 10),
                  diagonal='kde')

plt.savefig('scatterMatrix.png')
