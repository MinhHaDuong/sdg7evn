"""Plot regression line of Electricity used last month on Income.

Data: Answers to VHLSS 2010-2018 surveys.
See Hoai Son's PhD for discussion.
Warning: In ordinary regression, the constant is there to ensure
that the mean of the residuals is zero. Attributing a meaning to it is fishy.
(c) 2016-2021 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
"""

import matplotlib.pyplot as plt
import numpy as np

from VHLSS_importer import survey, YEARS
from scipy.stats import linregress


def subfig(year, row):
    income = survey.inc[survey.year == year] / 1000
    kWh = survey.kwh_last_month[survey.year == year]
    idx = np.isfinite(income) & np.isfinite(kWh) & (income < 200)

    ax = fig.add_subplot(len(YEARS[1:]), 1, row)
    plt.hexbin(income, kWh, bins="log", cmap="Greys", gridsize=500)
    ax.set_title(str(year), x=0.85, y=0.8)
    ax.set_ylabel("kWh / month")
    ax.set_ylim([0, 400])
    ax.set_xlim([0, 400])

    x = np.arange(200)
    slope, intercept, r_value, p_value, std_err = linregress(income[idx], kWh[idx])
    ax.plot(x, intercept + slope * x, color="k")

    regressionText = "kWh = {:.1f} + {:.2f} * income".format(intercept, slope)
    ax.text(205, intercept + slope * 200, regressionText, color="k", fontsize=8)
    if row == len(YEARS[1:]):
        ax.set_xlabel("Annual income, M VND")
    return ax


fig = plt.figure(figsize=(4, 7.874))
# fig.suptitle("Monthly electricity use as a function of annual income\nfor households in Vietnam",
#             fontsize=14)

for y, year in enumerate(YEARS[1:]):
    subfig(year, y + 1)

plt.tight_layout()


plt.savefig("kWhbyIncome.png")
fig.savefig("kWhbyIncome-300dpi.png", dpi=300)
