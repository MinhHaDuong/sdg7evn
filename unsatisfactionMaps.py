# Mapping energy poverty in Vietnam, by province
#
# Map of percentage of energy poors by province for each date
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE


from VHLSS_importer import survey, np
from mapTinh import plotChoropleths

DEBUG = False


def unsatisfaction(yr, provinceTinh):
    responses = survey[(survey.year == yr) & (survey.tinh == provinceTinh)].elec_poor.dropna()
    unsatisfied = len(responses[responses == 'Lacking'])
    Nresponses = len(responses)
    if DEBUG:
        print(provinceTinh, '\t', unsatisfied, '/', Nresponses)
    if (Nresponses != 0):
        return unsatisfied / Nresponses
    else:
        return np.nan

plotChoropleths(unsatisfaction,
                "%Responses 'Power needs were not met last month'",
                'unsatisfactionMaps.png',
                [2010, 2012, 2014])
