# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#
import matplotlib.pyplot as plt
import numpy as np

from VHLSS_importer import survey

print(
    """Answers to VHLSS 2010/2012/2014 surveys
Multidimentional plot on what is energy poverty:
Electricity used last month
Electricity bill last month

Period               2010/04   2012/04    2014/04
First block tarif      600      993        993
Second block tariff   1004     1242       1418
"""
)


def subfig(yr, n):
    quantity = survey.loc[survey.year == yr, "kwh_last_month"]
    cost = survey.loc[survey.year == yr, "elec_last_month"]

    ax = fig.add_subplot(3, 1, n)
    plt.hexbin(quantity, cost, bins="log", cmap="Greys", gridsize=200)
    ax.set_title(str(yr), x=0.2, y=0.8)
    ax.set_ylabel("kVND last month")
    ax.set_xlim([0, 400])
    ax.set_ylim([0, 600])

    print("----------------------")
    print(yr)
    x = np.arange(50)
    slope, intercept = np.polyfit(quantity[quantity <= 50], cost[quantity <= 50], 1)
    ax.plot(x, intercept + slope * x, color="red")
    x = np.arange(50, 400)
    print("First block price estimate {:.0f} VND / kWh".format(slope * 1000))
    slope, intercept = np.polyfit(quantity[quantity > 50], cost[quantity > 50], 1)
    ax.plot(x, intercept + slope * x, color="blue")
    print("Beyond first block price estimate {:.0f} VND / kWh".format(slope * 1000))
    return ax


fig = plt.figure(figsize=(5.5, 11))
fig.suptitle(
    """Increasing block tariff of electricity for households in Vietnam
Red regression line, kWh <= 50 kWh
Blue regression line, 50 < kWh < 400""",
    fontsize=12,
)

subfig(2010, 1)
subfig(2012, 2)
subfig(2014, 3).set_xlabel("kWh last month")

plt.savefig("blockTariff.png")
plt.savefig("blockTariff-300dpi.png", dpi=300)
