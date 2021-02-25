"""Compute the distributional consequences of applying a more progressive tariff.

On the electricity bills of households,
Based on the declared March bill in VHLSS 2014 <-- *** Warning ***

How many households would see their electricity bill decrease/increase, among the energy poors
for different definitions of energy poor

# Statistics on energy poverty in Vietnam
# based on VHLSS 2010/2012/2014 survey data
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
# Created on Thu Sep 22 13:50:53 2016
#

"""
import numpy as np

from VHLSS_importer import survey
from VHLSS_importer import block_limits, block_prices_2013, block_prices_alt

YEAR = 2014

block_sizes = np.diff(block_limits)

block_costs_2013 = block_sizes * block_prices_2013[1:] / 1000
total_bills_2013 = np.cumsum(np.insert(block_costs_2013, 0, 0))

block_costs_alt = block_sizes * block_prices_alt[1:] / 1000
total_bills_alt = np.cumsum(np.insert(block_costs_alt, 0, 0))


# %%

df = survey.loc[
    (survey.year == YEAR) & (survey.elec_poor.notnull()),
    [
        "inc",
        "kwh_last_month",
        "elec_last_month",
        "elec_poor",
        "inc_pov",
        "hhsize",
        "urb_rur",
    ],
]
df["bill_alt"] = np.interp(df.elec_last_month, total_bills_2013, total_bills_alt)
df["change"] = df.bill_alt - df.elec_last_month

df["high_cost"] = df.elec_last_month / (df.inc / 12) > 0.06
df["high_cost_expost"] = df.bill_alt / (df.inc / 12) > 0.06

df["income_percapita_permonth"] = df.inc / df.hhsize / 12

df["low_income"] = df.income_percapita_permonth < 400 + 100 * (df.urb_rur == "Urban")

# %%


def impact_categories(query_expr):
    winners = len(df.query(query_expr + " and change < 0"))
    loosers = len(df.query(query_expr + " and change > 0"))
    unaffected = len(df.query(query_expr + " and change == 0"))
    total = len(df.query(query_expr))
    n = df.count().inc
    return "{:5d} ({:.1f}%)\t{:5d} ({:.1f}%)\t{:5d} ({:.1f}%)\t{:5d} ({:.1f}%)".format(
        winners,
        100 * winners / n,
        unaffected,
        100 * unaffected / n,
        loosers,
        100 * loosers / n,
        total,
        100 * total / n,
    )


if __name__ == "__main__":
    print(
        "Define 'High costs' declaring an electricity bill last month > 6% annual income / 12"
    )
    print(
        """Define 'Low income' as household income per capita per month lower than 400 kVND
in rural area, 500 kVND in urban areas (official definition in 09-2011/QD-TTg)"""
    )

    print()
    print(
        "Household category         \tWinners     \tIndifferent   \tLoosers   \t# Households"
    )

    print(
        "Paid for <30kWh            \t", impact_categories("elec_last_month <= 29.79")
    )
    print("Using <30kWh               \t", impact_categories("kwh_last_month <= 30"))
    print("Lack electricity           \t", impact_categories('elec_poor == "Lacking"'))
    print("Officially poor            \t", impact_categories('inc_pov == "Yes"'))
    print("Low income                 \t", impact_categories("low_income"))
    print("High cost                  \t", impact_categories("high_cost"))
    print(
        "High cost & officialy poor \t",
        impact_categories('inc_pov == "Yes" and high_cost'),
    )
    print(
        "High cost & low income     \t", impact_categories("low_income and high_cost")
    )
    print("All households             \t", impact_categories("change < 1000000"))
