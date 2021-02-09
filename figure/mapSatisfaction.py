"""Map percentage of households lacking electricity.

VHLSS 2010, 2012 and 2014 asked respondents if they lacked electricity.
(c) 2016-2021 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
"""

import numpy as np

from VHLSS_importer import survey
from mapTinh import plotChoropleths

DEBUG = False


def satisfaction(yr, provinceTinh):
    responses = survey.elec_poor[
        (survey.year == yr) & (survey.tinh == provinceTinh)
    ]
    unsatisfied = responses[survey.lacking].count()
    Nresponses = responses.count()
    if DEBUG:
        print(provinceTinh, "\t", unsatisfied, "/", Nresponses)
    if Nresponses:
        return 1 - unsatisfied / Nresponses
    else:
        return np.nan


# Test
assert satisfaction(2008, 0) is np.nan
assert satisfaction(2010, 15) == 1 - 54 / 114
assert satisfaction(2012, 25) == 1 - 17 / 156
assert satisfaction(2014, 12) == 1 - 20 / 102

# %%

plotChoropleths(
    satisfaction,
    "%Responses 'Power needs met last month'",
    "mapSatisfaction",
    [2010, 2012, 2014]
)
