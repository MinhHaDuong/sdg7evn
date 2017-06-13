# Mapping energy poverty in Vietnam, by province
#
# Map of percentage of energy poors by province for each date
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE


from VHLSS_importer import survey, np
from mapTinh import plotChoropleths

DEBUG = False


def notGridLighting(yr, provinceTinh):
    lightPowerSource = survey[(survey.year == yr) & (survey.tinh == provinceTinh)].main_light.dropna()
    fromGrid = len(lightPowerSource[lightPowerSource == 'Main_Grid'])
    Nresponses = len(lightPowerSource)
    if DEBUG:
        print(provinceTinh, '\t', fromGrid, '/', Nresponses)
    if (Nresponses != 0):
        return 1 - fromGrid / Nresponses
    else:
        return np.nan

plotChoropleths(notGridLighting,
                '%Households not lighting from grid',
                'powerGridMaps.png',
                [2008, 2010, 2012, 2014])
