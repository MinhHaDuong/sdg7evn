# Statistics on energy poverty in Vietnam
# based on VHLSS 2010/2012/2014 survey data
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
# Created on Thu Sep 22 13:50:53 2016
#
import numpy as np
import pandas
import matplotlib.pyplot as plt

from VHLSS_importer import survey, YEARS

# %%


def lorenz_curve_points(data):
    """Return the Lorentz curve points of a pandas series or numpy array.

    Lifted from:  https://zhiyzuo.github.io/Plot-Lorenz/
    There is an IneqPy package, but creating a dependancy is overkill.
    Another source could have been
    https://gist.github.com/CMCDragonkai/c79b9a0883e31b327c88bfadb8b06fc4

    Argument can be a pandas Series or a numpy array.
    """
    if isinstance(data, pandas.core.series.Series):
        data = np.array(data.dropna())
    if data.size == 0:
        print("Error: calling with empty data")
        return
    data.sort()
    y = data.cumsum() / data.sum()
    y = np.insert(y, 0, 0)
    x = np.arange(y.size) / (y.size - 1)
    return x, y


def lorenz_curve(ax, data, label):
    x, y = lorenz_curve_points(data)
    ax.scatter(x, y,  label=label)


def subfig(fig, y, k):
    ax = fig.add_subplot(len(YEARS), 2, 2 * k + 1)
    ax.plot([0, 1], [0, 1], color='k')
    lorenz_curve(ax, survey[survey.year == y].inc, "Income")
    lorenz_curve(ax, survey[survey.year == y].elec_year, "Elec year")
    ax.set_title(y)
    ax.legend()


def subfig2(fig, y, k):
    ax = fig.add_subplot(len(YEARS), 2, 2 * k + 4)
    ax.plot([0, 1], [0, 1], color='k')
    lorenz_curve(ax, survey[survey.year == y].inc, "Income")
    lorenz_curve(ax, survey[survey.year == y].kwh_last_month, "kWh")
    ax.set_title(y)
    ax.legend()


fig = plt.figure(figsize=(12, 20))

for y, year in enumerate(YEARS):
    subfig(fig, year, y)

for y, year in enumerate(YEARS[1:]):
    subfig2(fig, year, y)

fig.savefig("inequalities.png")
fig.savefig("inequalities-300dpi.png", dpi=300)
