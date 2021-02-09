"""
Plot cumulative distribution function of electricity expense.

Created on Thu Sep 22 13:50:53 2016
@author: haduong
"""

# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
import matplotlib.pyplot as plt

from VHLSS_importer import survey, YEARS, CPI, np, curve_style


def cdf(yr, ax, deflate):
    if not deflate:
        deflator = 1
    else:
        deflator = CPI["2018"][0] / CPI[str(yr)][0]
    d = (
        survey.elec_year[survey.year == yr].dropna().sort_values()
        / 12
        * deflator
    )
    yvals = np.linspace(0, 1, len(d))
    ax.step(d, yvals, **curve_style[yr])


def subfig(i, deflate, xlabel):
    ax = fig.add_subplot(2, 1, i)

    for year in YEARS:
        cdf(year, ax, deflate)

    ax.set_xlim([0, 500])
    ax.set_ylim([0, 1])
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel("% Households", fontsize=10)
    #    ax.set_title('Electricity expense by households in Vietnam')
    ax.grid(True)
    ax.legend(YEARS, loc="lower right", frameon=False)


fig = plt.figure(figsize=(5.5, 7.874))
subfig(1, False, "kVND / month - current nominal amount")
subfig(2, True, "kVND / month - adjusted to 2018 prices")
# fig.suptitle("""Electricity expenses by Vietnamese households
# almost doubled in real terms between 2008 and 2014""", fontsize=14)

plt.tight_layout()

fig.savefig("ECDspending.png")
fig.savefig("ECDspending-300dpi.png", dpi=300)
