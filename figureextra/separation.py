# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#

"""Exploring VHLSS 2010/2012/2014 survey results, about on energy poverty

Multidimentional plot on what is energy poverty:
Annual electricity expenses / annual income
Household size

Red: electricity needs not met
Blue: all others
"""
import matplotlib.pyplot as plt

from VHLSS_importer import survey


def subfig(yr):
    x = survey.loc[survey.year == yr, "effort"]
    y = survey.loc[survey.year == yr, "size"]
    plt.scatter(x[~survey.lacking], y[~survey.lacking], color="blue")
    plt.scatter(x[survey.lacking], y[survey.lacking], color="red", alpha=0.3)


fig = plt.figure(figsize=(5.5, 11))

ax = fig.add_subplot(311)
subfig(2010)
ax.set_title("2010")
ax.set_xlim([0, 0.10])
ax.set_ylim([1, 16])

ax = fig.add_subplot(312)
subfig(2012)
ax.set_title("2012")
ax.set_xlim([0, 0.10])
ax.set_ylim([1, 16])

ax = fig.add_subplot(313)
subfig(2014)
ax.set_title("2014")
ax.set_ylabel("Household size")
ax.set_xlabel("Electricity expense / income ratio")
ax.set_xlim([0, 0.10])
ax.set_ylim([1, 16])

plt.savefig("separation.png")
plt.close(fig)

#%%
from pandas.plotting import radviz

plt.figure(figsize=(10, 10))
radviz(
    survey.loc[
        survey.year == 2014, ["elec_last_month", "inc", "size", "Q12", "sq_m"]
    ].dropna(),
    "Q12",
)
