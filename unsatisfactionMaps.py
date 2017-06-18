# Mapping energy poverty in Vietnam, by province
#
# Map of percentage of energy poors by province for each date
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE


from VHLSS_importer import survey, np
from mapTinh import plotChoropleths

DEBUG = False


def unsatisfaction(yr, provinceTinh):
    responses = survey.loc[(survey.year == yr) & (survey.tinh == provinceTinh), 'elec_poor']
    unsatisfied = responses[survey.lacking].count()
    Nresponses = responses.count()
    if DEBUG:
        print(provinceTinh, '\t', unsatisfied, '/', Nresponses)
    if Nresponses:
        return unsatisfied / Nresponses
    else:
        return np.nan


# Test
assert unsatisfaction(2008, 0) is np.nan
assert unsatisfaction(2010, 15) == 54 / 114
assert unsatisfaction(2012, 25) == 17 / 156
assert unsatisfaction(2014, 12) == 45 / 240

#%%

plotChoropleths(unsatisfaction,
                "%Responses 'Power needs were not met last month'",
                'unsatisfactionMaps.png',
                [2010, 2012, 2014])
