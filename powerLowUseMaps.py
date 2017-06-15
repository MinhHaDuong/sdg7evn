# Mapping energy poverty in Vietnam, by province
#
# Map of percentage of energy poors by province for each date
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE


from VHLSS_importer import survey, np
from mapTinh import plotChoropleths

DEBUG = False


def lowUseRate(yr, provinceTinh):
    usage = survey.loc[(survey.year == yr) & (survey.tinh == provinceTinh),
                       "kwh_last_month"
                       ].dropna()
    NlowUsers = len(usage[usage <= lowkWhperMonth])
    Nresponses = len(usage)
    if DEBUG:
        print(provinceTinh, '\t', NlowUsers, '/', Nresponses)
    if (Nresponses != 0):
        return NlowUsers / Nresponses
    else:
        return np.nan


lowkWhperMonth = 30

plotChoropleths(lowUseRate,
                'Households using less than " + str(lowkWhperMonth) + " kWh in previous month',
                'powerLowUseMaps.png',
                [2010, 2012, 2014])
