# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#

"""VHLSS 2008/2010/2012/2014 Vietnam Households surveys analysis - Satisfaction of needs

Red: Vietnam households declaring their electricity needs were not met (Q12)
Blue: The complementary population
Axis: electricity consumption, electricity bill
"""
import matplotlib.pyplot as plt

from VHLSS_importer import survey


def subfig(yr, n):
    ax = fig.add_subplot(3, 1, n)
    plt.hexbin(
        survey.loc[(survey.year == yr) & ~survey.lacking, "kwh_last_month"],
        survey.loc[(survey.year == yr) & ~survey.lacking, "elec_last_month"],
        bins="log",
        cmap="Blues",
        gridsize=200,
    )
    plt.hexbin(
        survey.loc[(survey.year == yr) & survey.lacking, "kwh_last_month"],
        survey.loc[(survey.year == yr) & survey.lacking, "elec_last_month"],
        bins="log",
        cmap="Reds",
        alpha=0.5,
        gridsize=200,
    )
    ax.set_title(str(yr), x=0.85, y=0.8)
    ax.set_ylabel("Bill last month (kVND)")
    ax.set_xlim([0, 400])
    ax.set_ylim([0, 600])
    return ax


fig = plt.figure(figsize=(5.5, 11))

subfig(2010, 1)
subfig(2012, 2)
subfig(2014, 3).set_xlabel("Electricity usage last month (kWh)")

plt.savefig("electricityBills.png")
