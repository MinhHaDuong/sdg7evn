"""Tabulate Key Performance Indicators of the Vietnam electricity sector.

Statistics on electricity poverty in Vietnam
(c) 2016-2021 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
"""

import pandas as pd

from VHLSS_importer import survey, YEARS


def fmt(sample, selector):
    """Return the percentage of matches in the data, as a string."""
    data = sample.dropna()
    size = len(data)
    if size == 0:
        return "NA"
    matches = len(data[selector])
    return "{:4.1f}%".format(100 * matches / size)


def summary_stat(year):
    """Return key performance indicators for a given year."""
    sample = survey[survey.year == year]

    lrural = sample.main_light[sample.urb_rur == "Rural"]
    nogrid_rural = fmt(lrural, lrural != "Main_Grid")

    lurban = sample.main_light[sample.urb_rur == "Urban"]
    nogrid_urban = fmt(lurban, lurban != "Main_Grid")

    use = sample.kwh_last_month
    low_use = fmt(use, use < 30)

    effort = sample.effort
    pay_much = fmt(effort, effort > 0.06)

    satisfaction = sample.elec_poor
    needs_unmet = fmt(satisfaction, satisfaction == "Lacking")

    return nogrid_rural, nogrid_urban, low_use, pay_much, needs_unmet


labels = [
    "No grid, rural",
    "No grid, urban",
    "Use < 30kWh / month",
    "Bill > 6% income",
    "Needs not met"
]
contents = [summary_stat(year) for year in YEARS]
table = pd.DataFrame(contents, index=YEARS, columns=labels).transpose()

pd.set_option('display.max_columns', len(YEARS))
pd.set_option('display.width', 150)
print(table)
