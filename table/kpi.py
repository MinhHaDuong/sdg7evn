"""Tabulate Key Performance Indicators of the Vietnam electricity sector.

Statistics on electricity poverty in Vietnam
(c) 2016-2021 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
"""

import pandas as pd

from VHLSS_importer import survey, YEARS

survey["elec_use"] = pd.cut(survey.kwh_last_month, [-100, 30, 3000])
# Why not use survey.effort ?
survey["income_share"] = pd.cut(survey.elec_year / survey.inc, [0, 0.06, 1])


def cell(kpi, year):
    """Return the KPI as a formatted string."""
    if year in kpi.index:
        fmt_string = "\t {:4.1f}%"
        return fmt_string.format(kpi[year])
    return "\t   NA"


def row(column, complement=False, df=survey):
    """Return the row as a string."""
    xtable = pd.crosstab(df[column], df.year, normalize="columns")
    kpi = 100 * xtable.iloc[0]
    if complement:
        kpi = 100 - kpi
    items = [cell(kpi, year) for year in YEARS]
    return ''.join(items)


print("""
            Year         \t 2008 \t 2010 \t 2012 \t 2014 \t 2016 \t 2018
Share of households""")
print(
    "No grid lighting, Rural",
    row("main_light", True, survey[survey.urb_rur == "Rural"]),
)
print(
    "No grid lighting, Urban",
    row("main_light", True, survey[survey.urb_rur == "Urban"]),
)
print("Use < 30 kWh / month   ", row("elec_use"))
print("Bill > 6% income       ", row("income_share", True))
print("Use does not meet needs", row("elec_poor"))
