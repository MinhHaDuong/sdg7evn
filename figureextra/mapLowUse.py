# Mapping energy poverty in Vietnam, by province
#
# Map of percentage of energy poors by province for each date
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE

import numpy as np

from VHLSS_importer import survey
from mapTinh import plotChoropleths

DEBUG = False


# %%

def lowUseRate(yr, provinceTinh):
    usage = survey.loc[(survey.year == yr) & (survey.tinh == provinceTinh),
                       "kwh_last_month"
                       ].dropna()
    NlowUsers = (usage <= lowkWhperMonth).sum()
    Nresponses = len(usage)
    if DEBUG:
        print(provinceTinh, '\t', NlowUsers, '/', Nresponses)
    try:
        ratio = NlowUsers / Nresponses
    except ZeroDivisionError:
        ratio = np.nan
    return ratio


# %%

lowkWhperMonth = 30
legend = f'Households using less than {lowkWhperMonth} kWh in previous month'
plotChoropleths(lowUseRate, legend, 'mapLowUse', [2010, 2012, 2014])
