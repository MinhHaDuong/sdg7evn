# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:50:53 2016

@author: haduong
"""

# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#

from VHLSS_importer import survey, CPI, plt, np, curve_style


def cdf(yr, ax, deflate):
    deflator = float(CPI.Consumer_Price_Index["2014"]) / float(CPI.Consumer_Price_Index[str(yr)])
    if not deflate:
        deflator = 1
    d = survey[survey.year == yr].elec_year.dropna() / 12 * deflator
    sorted = d.sort_values()
    yvals = np.arange(1, len(sorted) + 1) / float(len(sorted))
    ax.step(sorted, yvals, color=curve_style[yr][0], linestyle=curve_style[yr][1])
    print('\nIn year', yr, 'the fraction of households who declared')
    print('having spend less than 100 kVND on electricity on average month was ', end='')
    print(round(100 * (len(d[d <= 100]) + len(d[d < 100])) / 2 / len(d), 1), '%\n')
    print(d.describe())


def subfig(i, deflate, xlabel):
    ax = fig.add_subplot(2, 1, i)

    cdf(2014, ax, deflate)
    cdf(2012, ax, deflate)
    cdf(2010, ax, deflate)
    cdf(2008, ax, deflate)

    ax.set_xlim([0, 500])
    ax.set_ylim([0, 1])
    ax.set_xlabel(xlabel)
    ax.set_ylabel('CDF: % respondents who spend less than X kVND')
#    ax.set_title('Electricity expense by households in Vietnam')
    ax.grid(True)
    ax.legend(['2014', '2012', '2010', '2008'], loc=4)


fig = plt.figure(figsize=(6, 12))
subfig(1, False, 'kVND per month - current nominal amount')
subfig(2, True, 'kVND per month - adjusted to 2014 prices')
fig.suptitle("""Electricity expenses by Vietnamese households
almost doubled in real terms between 2008 and 2014""", fontsize=14)

fig.savefig('ECDspending.png')
fig.savefig('ECDspending-300dpi.png', dpi=300)
fig.savefig('ECDspending.pdf')
