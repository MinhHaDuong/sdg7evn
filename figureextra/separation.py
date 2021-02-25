"""Exploring VHLSS 2010/2012/2014 survey results, about on energy poverty

Multidimentional plot on what is energy poverty:
Annual electricity expenses / annual income
Household size

Red: electricity needs not met
Blue: all others
"""
import matplotlib.pyplot as plt
from pandas.plotting import radviz

from VHLSS_importer import survey


# %%
# Effort is not well correlated with insufficient electricity

def subfig(yr):
    x = survey.effort[survey.year == yr]
    y = survey.hhsize[survey.year == yr]
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

# %%
# RadViz allow to project a N-dimensional data set into a 2D space
# where the influence of each dimension can be interpreted as
# a balance between the influence of all dimensions.
# https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.135.889
#

plt.figure(figsize=(10, 10))
radviz(
    survey.loc[
        survey.year == 2014, ["elec_last_month", "inc", "hhsize", "Q12", "sq_m"]
    ].dropna(),
    "Q12",
)
