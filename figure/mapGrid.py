# Mapping energy poverty in Vietnam, by province
#
# Map of percentage of energy poors by province for each date
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE

import numpy as np

from VHLSS_importer import survey, YEARS
from mapTinh import plotChoropleths

DEBUG = False


def grid_lighting(yr, provinceTinh):
    responses = survey.main_light[
        (survey.year == yr) & (survey.tinh == provinceTinh)
    ]
    fromGrid = responses[responses == "Main_Grid"].count()
    Nresponses = responses.count()
    if DEBUG:
        print(provinceTinh, "\t", fromGrid, "/", Nresponses)
    if Nresponses:
        return fromGrid / Nresponses
    else:
        return np.nan


# %%

plotChoropleths(
    grid_lighting,
    "%Households electrified",
    "mapGrid",
    YEARS,
    "magma"
)
