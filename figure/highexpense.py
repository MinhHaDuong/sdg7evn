"""VHLSS 2008-2018 analysis - Plot housholds with high electricity expense.

Define "High Expense" as "Electricity bill > 6% income"

The surveys asked about the annual electricity expense, and about the electricity bill last month
The surveys asked about annual income estimate.

We display Electricity bill vs. Income for Vietnam households
with red line defining the 'bill == 6% of income' frontier.
Households above the line are in High electricity expense conodition

Statistics on energy poverty in Vietnam
(c) 2016-2021 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
"""

import matplotlib.pyplot as plt
import numpy as np

from VHLSS_importer import survey, YEARS

fig = plt.figure(figsize=(12, 20))


def subfig(yr, row):
    num_rows = len(YEARS)
    ax = fig.add_subplot(num_rows, 2, 2 * row + 1)
    plt.hexbin(
        survey.inc[survey.year == yr] / 1000,
        survey.elec_year[survey.year == yr] / 1000,
        bins="log",
        cmap="Greys",
        gridsize=500,
    )
    ax.set_title(str(yr), y=0.8, x=0.85)
    ax.set_ylabel("Annual expense, M VND")
    ax.set_ylim([0, 5])
    ax.set_xlim([0, 400])
    x = np.arange(200)
    if row == num_rows - 1:
        ax.set_xlabel("Annual income, M VND")
    ax.plot(x, x * 0.06, color="red")
    return ax


for y, year in enumerate(YEARS):
    subfig(year, y)


def subfig2(yr, row):
    num_rows = len(YEARS)
    ax = fig.add_subplot(len(YEARS), 2, 2 * row + 2)
    plt.hexbin(
        survey.inc[survey.year == yr] / 12,
        survey.elec_last_month[survey.year == yr],
        bins="log",
        cmap="Greys",
        gridsize=500,
    )
    ax.set_title(str(yr), y=0.8, x=0.85)
    ax.set_ylabel("Bill last month, k VND")
    ax.set_ylim([0, 410])
    ax.set_xlim([0, 33000])
    x = np.arange(7000)
    ax.plot(x, x * 0.06, color="red")
    if row == num_rows - 1:
        ax.set_xlabel("Monthly income, k VND")
    return ax


for y, year in enumerate(YEARS[1:]):
    subfig2(year, y + 1)

plt.savefig("highexpense.png")
plt.savefig("highexpense-300dpi.png", dpi=300)
