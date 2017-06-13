# Statistics on energy poverty in Vietnam
# based on VHLSS 2010/2012/2014 survey data
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#Created on Thu Sep 22 13:50:53 2016
#

"""Computes the distributional consequences of applying a more progressive tariff
on the electricity bills of households, based on the declared March bill in VHLSS 2014

How many people get in to / out of the High Cost of electricity (bill > 6% income) condition
with a more progressive tariff.
Among the general population, and among the officially income poor
"""

from VHLSS_importer import np, survey

from table_TariffWinners import df


def lihc_count(df, ante, post):
    return len(df.loc[(df.high_cost == ante) & (df.high_cost_expost == post)])


def lihc_array(d):
    return np.array([[lihc_count(d, False, False), lihc_count(d, False, True)],
                     [lihc_count(d, True,  False), lihc_count(d, True,  True)]])


def lihc_table(df):
    d = df[np.isfinite(df.inc)]
    t = lihc_array(d)
    d2 = df.loc[df.inc_pov == 'Yes']
    t2 = lihc_array(d2)
    d3 = df.loc[df.low_income]
    t3 = lihc_array(d3)
    n = survey[survey.year == 2014].count().inc
    fmt = "\t{:5d} ({:.1f}%)\t{:5d} ({:.1f}%)\t{:5d} ({:.1f}%)\n"
    s = "Households with high costs under the EVN 2013 (ex ante)"
    s += " and the more progressive tariff (ex post)\n"
    s += "                              \tAll respondents\tOfficially poor\tLow income\n"
    s += "Never high cost               " + fmt.format(
            t[0, 0], 100 * t[0, 0] / n, t2[0, 0], 100 * t2[0, 0] / n, t3[0, 0], 100 * t3[0, 0] / n)
    s += "High cost with both tariffs   " + fmt.format(
            t[1, 1], 100 * t[1, 1] / n, t2[1, 1], 100 * t2[1, 1] / n, t3[1, 1], 100 * t3[1, 1] / n)
    s += "High cost only ex ante        " + fmt.format(
            t[1, 0], 100 * t[1, 0] / n, t2[1, 0], 100 * t2[1, 0] / n, t3[1, 0], 100 * t3[1, 0] / n)
    s += "High cost only ex post        " + fmt.format(
            t[0, 1], 100 * t[0, 1] / n, t2[0, 1], 100 * t2[0, 1] / n, t3[0, 1], 100 * t3[0, 1] / n)
    s += "Total                         " + fmt.format(
            len(d), 100 * len(d) / n, len(d2), 100 * len(d2) / n, len(d3), 100 * len(d3) / n)
    return s

if __name__ == '__main__':
    print(lihc_table(df))
