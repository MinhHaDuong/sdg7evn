# Statistics on energy poverty in Vietnam
# based on VHLSS 2010/2012/2014 survey data
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
# Created on Thu Sep 22 13:50:53 2016
#
import matplotlib.pyplot as plt
from scipy.stats import percentileofscore

from VHLSS_importer import survey, YEARS, cdf_plot

fig = plt.figure(figsize=(5.5, 4.125))

plt.axis([0, 350, 0, 100])
plt.xlabel("kWh / month")
plt.ylabel("% Households")

for year in YEARS[1:]:
    cdf_plot(year, "kwh_last_month")

plt.grid(True)
plt.legend(YEARS[1:], loc="lower right", frameon=False)

kWh = 150
array = survey.kwh_last_month[survey.year == 2018].dropna()
percentile = percentileofscore(array, kWh)
plt.plot([0, kWh, kWh], [percentile, percentile, 0], "grey", linestyle="--", alpha=0.5)
plt.text(0, percentile, "{:.1f}".format(percentile), alpha=0.5)

note = """In 2018, {:1.1f}% of households
used less than {:3d} kWh / month"""
note_text = note.format(percentile, kWh)

plt.annotate(
    note_text,
    xy=(kWh, percentile),
    xytext=(kWh + 15, percentile - 15),
    alpha=0.5,
    arrowprops=dict(facecolor="grey", shrink=0.0, width=2),
)

fig.savefig("ECDuse.png")
fig.savefig("ECDuse-300dpi.png", dpi=300)
