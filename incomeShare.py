# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#
# The data distribution is shown on "elec_yearbyIncome.py"

from VHLSS_importer import survey, np, plt, pd, curve_style


def cdf(yr):
#    print('\n------------------------------', yr, '------------------------')
    df = survey[['year', 'elec_year', 'inc', 'elec_poor']]
    df = df[(df.year == yr) & (df.inc != 0)]
    x = (df.elec_year / df.inc).dropna()
#    print('Quantiles of the electricity bill/income distribution')
#    print(x.quantile([0.5, 0.95, 0.99]))

    sorted = x.sort_values()
    N = len(sorted)
#    print('Proportion of zero bills')
#    print(round(len(x[x == 0]) / N * 100, 1))
#    print('Proportion of >10% bills')
#    print(round(len(x[x >= 0.1]) / N * 100, 1))

    yvals = np.arange(1, N + 1) / N
    plt.step(sorted, yvals, color=curve_style[yr][0], linestyle=curve_style[yr][1])

plt.axis([0, 0.1, 0, 1])

cdf(2014)
cdf(2012)
cdf(2010)
cdf(2008)

plt.xlabel('Fraction of income spend on electricity')
plt.ylabel('% Households')
plt.legend(['2014', '2012', '2010', '2008'], loc='lower right')

plt.savefig('incomeShare.png')



#print("Electricity bill as a fraction of income. Source VHLSS.")
print("Survey year                          \t2008\t2010\t2012\t2014")

def column(yr):
    df = survey[['year', 'elec_year', 'inc', 'elec_poor']]
    df = df[(df.year == yr) & (df.inc != 0)]
    x = (df.elec_year / df.inc).dropna()
    sorted = x.sort_values()
    N = len(sorted)
    r1 = len(x[x == 0]) / N * 100
    r2 = len(x[x >= 0.1]) / N * 100
    r3 = x.quantile(0.5) * 100
    r4 = x.quantile(0.95) * 100
    return r1, r2, r3, r4

print("Households not paying anything  "
      +"\t{:,.3f}%\t{:,.1f}%\t{:,.1f}%\t{:,.1f}%\tof households".format(column(2008)[0],
                                                         column(2010)[0],
                                                         column(2012)[0],
                                                         column(2014)[0])
      )
print("Hh paying >10% of income on electricity"
      +"\t{:,.1f}%\t{:,.1f}%\t{:,.1f}%\t{:,.1f}%\tof households".format(column(2008)[1],
                                                         column(2010)[1],
                                                         column(2012)[1],
                                                         column(2014)[1])
      )
print("Half of households pay less than"
      +"\t{:,.1f}%\t{:,.1f}%\t{:,.1f}%\t{:,.1f}%\tof income on electricity".format(column(2008)[2],
                                                         column(2010)[2],
                                                         column(2012)[2],
                                                         column(2014)[2])
      )
print("95% of households pay less than "
      +"\t{:,.1f}%\t{:,.1f}%\t{:,.1f}%\t{:,.1f}%\tof income on electricity".format(column(2008)[3],
                                                         column(2010)[3],
                                                         column(2012)[3],
                                                         column(2014)[3])
      )
