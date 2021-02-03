# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:50:53 2016

@author: haduong
"""

# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
import matplotlib.pyplot as plt

from VHLSS_importer import survey, CPI, np, curve_style


def cdf(yr, ax, deflate):
    deflator = float(CPI.Consumer_Price_Index["2014"]) / float(
        CPI.Consumer_Price_Index[str(yr)]
    )
    if not deflate:
        deflator = 1
    d = (
        survey.loc[survey.year == yr, "elec_year"].dropna().sort_values()
        / 12
        * deflator
    )
    yvals = np.linspace(0, 1, len(d))
    ax.step(d, yvals, **curve_style[yr])


def subfig(i, deflate, xlabel):
    ax = fig.add_subplot(2, 1, i)

    cdf(2014, ax, deflate)
    cdf(2012, ax, deflate)
    cdf(2010, ax, deflate)
    cdf(2008, ax, deflate)

    ax.set_xlim([0, 500])
    ax.set_ylim([0, 1])
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel("% Households", fontsize=10)
    #    ax.set_title('Electricity expense by households in Vietnam')
    ax.grid(True)
    ax.legend(["2014", "2012", "2010", "2008"], loc=4, frameon=False)


fig = plt.figure(figsize=(5.5, 7.874))
subfig(1, False, "kVND / month - current nominal amount")
subfig(2, True, "kVND / month - adjusted to 2014 prices")
# fig.suptitle("""Electricity expenses by Vietnamese households
# almost doubled in real terms between 2008 and 2014""", fontsize=14)

plt.tight_layout()

fig.savefig("ECDspending.png")
fig.savefig("ECDspending-300dpi.png", dpi=300)
