# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
# The data summary is shown in "incomeShare.py"
#


"""VHLSS 2008/2010/2012/2014 Vietnam Households surveys analysis - High electricity expense

Define "High Expense" as "Electricity bill > 6% income"

The surveys asked about the annual electricity expense, and about the electricity bill last month
The surveys asked about annual income estimate.

We display Electricity bill vs. Income for Vietnam households
with red line defining the 'bill == 6% of income' frontier.
Households above the line are in High electcitiy expense conodition
"""
import matplotlib.pyplot as plt
import numpy as np

from VHLSS_importer import survey

fig = plt.figure(figsize=(12, 12))


def subfig(yr, n):
    ax = fig.add_subplot(4, 2, n)
    plt.hexbin(survey.loc[survey.year == yr, 'inc'] / 1000,
               survey.loc[survey.year == yr, 'elec_year'] / 1000,
               bins='log', cmap='Greys',
               gridsize=500
               )
    ax.set_title(str(yr), y=0.8, x=0.85)
    ax.set_ylabel('Annual expense, M VND')
    ax.set_ylim([0, 5])
    ax.set_xlim([0, 400])
    x = np.arange(200)
    ax.plot(x, x * 0.06, color='red')
    return ax


subfig(2008, 1)
subfig(2010, 3)
subfig(2012, 5)
subfig(2014, 7).set_xlabel('Annual income, M VND')


def subfig2(yr, n):
    ax = fig.add_subplot(4, 2, n)
    plt.hexbin(survey.loc[survey.year == yr, 'inc'] / 12,
               survey.loc[survey.year == yr, 'elec_last_month'],
               bins='log', cmap='Greys',
               gridsize=500
               )
    ax.set_title(str(yr), y=0.8, x=0.85)
    ax.set_ylabel('Bill last month, k VND')
    ax.set_ylim([0, 410])
    ax.set_xlim([0, 33000])
    x = np.arange(7000)
    ax.plot(x, x * 0.06, color='red')
    return ax


subfig2(2010, 4)
subfig2(2012, 6)
subfig2(2014, 8).set_xlabel('Monthly income, k VND')

plt.savefig("figure_highexpense.png")
plt.savefig("figure_highexpense-300dpi.png", dpi=300)
