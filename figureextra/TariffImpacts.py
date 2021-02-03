# Statistics on energy poverty in Vietnam
# based on VHLSS 2010/2012/2014 survey data
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
# Created on Thu Sep 22 13:50:53 2016
#

"""Computes the distributional consequences of applying a more progressive tariff
on the electricity bills of households, based on the declared March bill in VHLSS 2014

As a proxy to the total EVN revenue, we look at variations of the mean bill
"""
import matplotlib.pyplot as plt
import numpy as np

from VHLSS_importer import survey
from VHLSS_importer import block_limits, block_prices_2013, block_prices_alt
from scipy.optimize import fsolve

block_sizes = np.diff(block_limits)

block_costs_2013 = block_sizes * block_prices_2013[1:] / 1000
total_bills_2013 = np.cumsum(np.insert(block_costs_2013, 0, 0))

block_costs_alt = block_sizes * block_prices_alt[1:] / 1000
total_bills_alt = np.cumsum(np.insert(block_costs_alt, 0, 0))

#%%


def change(bill):
    return np.interp(bill, total_bills_2013, total_bills_alt) - bill


untouched_bill = fsolve(change, 70)[0]

#%%

bill_ref = survey.loc[survey.year == 2014, "elec_last_month"].dropna()
bill_alt = np.interp(bill_ref, total_bills_2013, total_bills_alt)
bill_change = bill_alt - bill_ref

avg_paid_ref = bill_ref.mean()
avg_paid_alt = bill_alt.mean()
relative_increase = (avg_paid_alt - avg_paid_ref) / avg_paid_ref


def percent_zero(series):
    return 100 * (series == 0).sum() / len(series)


print(
    "Electricity bills up to {:.1f} k VND per month are reduced.".format(untouched_bill)
)

print("The share of households with a zero electricity bill ", end="")
print(
    "increases from {:.1f}% to {:.1f}%.".format(
        percent_zero(bill_ref), percent_zero(bill_alt)
    )
)

print(
    "The bill decreases for {:.1f}% of households, ".format(
        100 * len(bill_change[bill_change <= 0]) / len(bill_change)
    ),
    end="",
)
print("at most by {:.1f} kVND.".format(bill_change.min()))

print()

print(
    "The average bill increases {:.0f}% from {:.1f} kVND to {:.1f} kVND, ".format(
        relative_increase * 100, avg_paid_ref, avg_paid_alt
    ),
    end="",
)

print("that is {:.1f} kVND.".format(bill_change.mean()))

print(
    "For 50% of households, the bill increases over {:.1f} kVND".format(
        bill_change.quantile(0.50)
    )
)
print(
    "For  5% of households, the bill increases over {:.1f} kVND".format(
        bill_change.quantile(0.95)
    )
)
print(
    "For  1% of households, the bill increases over {:.1f} kVND, ".format(
        bill_change.quantile(0.99)
    ),
    end="",
)
print("with a maximum increase of {:.1f} kVND.".format(bill_change.max()))

#%%

plt.figure()
bill_change.hist(bins=[-30, 0, 30, 60, 90, 120, 150, 180, 360, 2000], density=True)
plt.axis([0, 305, -0.001, 0.015])
plt.xticks([-30, 0, 30, 60, 90, 120, 150, 180, 360])
plt.xlabel("kVND")
plt.yticks([])
plt.title("Distribution of monthly bill change (area = 1)")

#%% The  change  function

plt.figure()
plt.plot(bill_ref, bill_alt, ".", color="blue", alpha=0.01)
plt.plot(total_bills_2013[:-1], total_bills_alt[:-1])
plt.plot(total_bills_alt[:-1], total_bills_alt[:-1], color="grey")
plt.axis([0, 300, 0, 300])
plt.xlabel("EVN 2013 tariff, kVND")
plt.ylabel("More progressive tariff, kVND")
plt.title("Change in monthly electricity bill")
plt.xticks(block_limits[:-1])
plt.yticks(block_limits[:-1])


#%%


def plot_poverty_criteria(bills):
    plt.figure()
    plt.hexbin(df.inc / 12, bills, bins="log", cmap="Greys", gridsize=1000)
    plt.xlabel("Monthly income / 12, kVND")
    plt.ylabel("Monthly bill, kVND")
    plt.axis([-100, 6000, -10, 250])

    x = np.arange(20000)

    # Bill > 6% income
    plt.plot(x, x * 0.06, color="k", linestyle=":")
    plt.text(
        2800,
        250,
        "Electricity bill = 6% income",
        color="k",
        bbox=dict(facecolor="white", alpha=0.5),
        rotation=45,
    )

    # Pays less than for 30kWh
    energy_poverty_line = total_bills_2013[1]
    plt.plot(
        [0, 6000],
        [energy_poverty_line, energy_poverty_line],
        color="blue",
        linestyle="--",
    )
    plt.text(
        4000,
        energy_poverty_line + 3,
        "Energy poverty line",
        color="blue",
        bbox=dict(facecolor="white", alpha=0.5),
    )

    # Winners of the reform
    plt.plot([0, 6000], [untouched_bill, untouched_bill], color="red", linestyle="-")
    plt.text(
        4000,
        untouched_bill + 3,
        "Redistribution line",
        color="red",
        bbox=dict(facecolor="white", alpha=0.5),
    )

    # Average household size 3.9 people in Vietnam in 2014
    # Source: http://www.arcgis.com/home/item.html?id=80ffd900e5284873995b4e4ffb0e1d62
    # Poverty line 400 kVND/month/person country, 500 kVND/month/person city
    # Source: Quyet-dinh-09-2011-QD-TTg-chuan-ho-ngheo-can-ngheo
    # Urbanization 33.1% in 2016
    income_poverty_line = 3.9 * (0.331 * 500 + (1 - 0.331) * 400)
    plt.plot(
        [income_poverty_line, income_poverty_line],
        [0, 250],
        color="green",
        linestyle="-.",
    )
    plt.text(
        income_poverty_line + 10,
        230,
        "Income\npoverty line",
        color="green",
        bbox=dict(facecolor="white", alpha=0.5),
    )


df = survey.loc[survey.year == 2014, ["elec_last_month", "inc"]].dropna()
plot_poverty_criteria(df.elec_last_month)
plot_poverty_criteria(np.interp(df.elec_last_month, total_bills_2013, total_bills_alt))
