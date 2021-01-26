# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#
# The data distribution is shown on "elec_yearbyIncome.py"

from VHLSS_importer import survey, np, plt
import pandas as pd


def cdf(yr, col):
    print('\n------------------------------', yr, '------------------------')
    df = survey[['year', 'elec_year', 'inc', 'elec_poor']]
    df = df[(df.year == yr) & (df.inc != 0)]
    x = (df.elec_year / df.inc).dropna()
    print('Quantiles of the electricity bill/income distribution')
    print(x.quantile([0.5, 0.95, 0.99]))

    sorted = x.sort_values()
    N = len(sorted)
    print('Proportion of zero bills')
    print(round(len(x[x == 0]) / N * 100, 1))
    print('Proportion of >10% bills')
    print(round(len(x[x >= 0.1]) / N * 100, 1))

    yvals = np.arange(1, N + 1) / N
    plt.step(sorted, yvals, color=col)

plt.axis([0, 0.1, 0, 1])

cdf(2008, "yellow")
cdf(2010, "red")
cdf(2012, "green")
cdf(2014, "blue")

plt.xlabel('Fraction of income spend on electricity')
plt.ylabel('% Households')
plt.legend(['2008', '2010', '2012', '2014'])

plt.savefig('incomeShare.png')


def rows(yr):
    df = survey[['year', 'elec_year', 'inc', 'elec_poor']]
    df = df[(df.year == yr) & (df.inc != 0)]
    x = (df.elec_year / df.inc).dropna()
    sorted = x.sort_values()
    N = len(sorted)
    r1 = len(x[x == 0]) / N
    r2 = len(x[x >= 0.1]) / N
    r3 = x.quantile(0.5)
    r4 = x.quantile(0.95)
    return [r1, r2, r3, r4]

df = pd.DataFrame([rows(yr) for yr in (2008, 2010, 2012, 2014)],
                  index=[2008, 2010, 2012, 2014],
                  columns=["Paid nothing", "Paid > 10% income", "Median effort", "Top 5%"])

pd.set_option('precision', 3)

print("Distribution of the effort: annual electricity bill / annual income")
print(df.transpose() * 100)