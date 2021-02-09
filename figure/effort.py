"""Plot the cumulative distribution of budgetary effort for electricity.

Statistics on energy poverty in Vietnam
(c) 2016-2021 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
"""

import matplotlib.pyplot as plt

from VHLSS_importer import survey, YEARS, cdf_plot

fig = plt.figure(figsize=(5.5, 4.125))

plt.axis([0, 0.1, 0, 100])

for year in YEARS:
    cdf_plot(year, "effort")

example_percentile = 80
example_fraction = survey.loc[survey.year == 2018, "effort"].quantile(
    example_percentile / 100
)
plt.plot(
    [0, example_fraction, example_fraction],
    [example_percentile, example_percentile, 0],
    "grey",
    linestyle="--",
    alpha=0.5,
)
plt.text(example_fraction, 0, "{:.3f}".format(example_fraction), alpha=0.5)

note = "In 2018, 80% of households\nspend less than {:1.1f}% of income\non electricity"
note_text = note.format(example_fraction * 100)

plt.annotate(
    note_text,
    xy=(example_fraction, example_percentile),
    xytext=(example_fraction + 0.005, example_percentile - 20),
    alpha=0.5,
    arrowprops=dict(facecolor="grey", shrink=0.0, width=2),
)

plt.xlabel("Fraction of income spend on electricity")
plt.ylabel("% Households")
plt.legend(YEARS, loc="lower right", frameon=False)

fig.savefig("effort.png")
fig.savefig("effort-300dpi.png", dpi=300)
