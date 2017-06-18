# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#
# The data distribution is shown on "elec_yearbyIncome.py"
"""Electricity bill as a fraction of income in the VHLSS.
"""

from VHLSS_importer import survey, np, plt, curve_style

#%%


def cdf(yr):
    x_sorted = survey.loc[survey.year == yr, 'effort'].dropna().sort_values()
    N = len(x_sorted)
    y = np.arange(1, N + 1) / N
    plt.step(x_sorted, y, **curve_style[yr])


plt.axis([0, 0.1, 0, 1])

cdf(2014)
cdf(2012)
cdf(2010)
cdf(2008)

plt.xlabel('Fraction of income spend on electricity')
plt.ylabel('% Households')
plt.legend(['2014', '2012', '2010', '2008'], loc='lower right')

plt.savefig('incomeShare.png')


#%%

print("Survey year                          \t2008\t2010\t2012\t2014")


def column(yr):
    x = survey.loc[survey.year == yr, 'effort'].dropna()

    sorted = x.sort_values()
    N = len(sorted)
    r1 = len(x[x == 0]) / N * 100
    r2 = len(x[x >= 0.06]) / N * 100
    r3 = x.quantile(0.5) * 100
    r4 = x.quantile(0.95) * 100
    return r1, r2, r3, r4


row_fmt = "\t{:,.2f}%\t{:,.1f}%\t{:,.1f}%\t{:,.1f}%\t"

print("Households not paying anything  " + (row_fmt + "of households").format(
      column(2008)[0], column(2010)[0], column(2012)[0], column(2014)[0])
      )
print("Hh paying >6% of income on electricity" + (row_fmt + "of households").format(
      column(2008)[1], column(2010)[1], column(2012)[1], column(2014)[1])
      )
print("Half of households pay less than" + (row_fmt + "of income on electricity").format(
      column(2008)[2], column(2010)[2], column(2012)[2], column(2014)[2])
      )
print("95% of households pay less than " + (row_fmt + "of income on electricity").format(
      column(2008)[3], column(2010)[3], column(2012)[3], column(2014)[3])
      )
