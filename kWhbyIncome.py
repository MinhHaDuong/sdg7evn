# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#
import matplotlib.pyplot as plt
import numpy as np

from VHLSS_importer import survey
from scipy.stats import linregress

print("""Answers to VHLSS 2010/2012/2014 surveys
Electricity used last month vs. Income
""")


def subfig(yr, n):
    income = survey.loc[survey.year == yr, 'inc'] / 1000
    kWh = survey.loc[survey.year == yr, 'kwh_last_month']
    idx = np.isfinite(income) & np.isfinite(kWh) & (income < 200)

    ax = fig.add_subplot(3, 1, n)
    plt.hexbin(income, kWh,
               bins='log', cmap='Greys',
               gridsize=500
               )
    ax.set_title(str(yr), x=0.85, y=0.8)
    ax.set_ylabel('kWh / month')
    ax.set_ylim([0, 400])
    ax.set_xlim([0, 400])

    x = np.arange(200)
    slope, intercept, r_value, p_value, std_err = linregress(income[idx], kWh[idx])
    ax.plot(x, intercept + slope * x, color='k')

    regressionText = "kWh = {:.1f} + {:.2f} * income".format(intercept, slope)
    ax.text(205, intercept + slope * 200, regressionText, color='k', fontsize=8)
    return ax


fig = plt.figure(figsize=(4, 7.874))
#fig.suptitle("Monthly electricity use as a function of annual income\nfor households in Vietnam",
#             fontsize=14)

subfig(2010, 1)

subfig(2012, 2)

subfig(2014, 3).set_xlabel('Annual income, M VND')

plt.tight_layout()


plt.savefig('kWhbyIncome.png')
fig.savefig('kWhbyIncome-300dpi.png', dpi=300)
