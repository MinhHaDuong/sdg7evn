"""Verify the effectiveness of increasing block tariff.

Do households using less than 50 kWh / month pay electricity lower?
Yes if the slope of red segment is lower than the blue.
Statistics on electricity poverty in Vietnam
(c) 2016-2021 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
"""

import matplotlib.pyplot as plt
import numpy as np

from VHLSS_importer import survey, YEARS


def subfig(yr, n):
    quantity = survey.loc[survey.year == yr, "kwh_last_month"]
    cost = survey.loc[survey.year == yr, "elec_last_month"]

    n_plots = len(YEARS) - 1
    ax = fig.add_subplot(n_plots, 1, n)
    plt.hexbin(quantity, cost, bins="log", cmap="Greys", gridsize=200)
    ax.set_title(str(yr), x=0.1, y=0.4)
    ax.set_ylabel("kVND last month")
    ax.set_xlim([0, 400])
    ax.set_ylim([0, 600])
    if n == n_plots:
        ax.set_xlabel("kWh/month")

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

for y, year in enumerate(YEARS[1:]):
    subfig(year, y+1)

plt.savefig("blockTariff.png")
plt.savefig("blockTariff-300dpi.png", dpi=300)
