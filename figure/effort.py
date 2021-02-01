# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#
# The data distribution is shown on "elec_yearbyIncome.py"
"""Electricity bill as a fraction of income in the VHLSS.
"""
import matplotlib.pyplot as plt

from VHLSS_importer import survey, cdf_plot

fig = plt.figure(figsize=(5.5, 4.125))

plt.axis([0, 0.1, 0, 100])

cdf_plot(2014, 'effort')
cdf_plot(2012, 'effort')
cdf_plot(2010, 'effort')
cdf_plot(2008, 'effort')

example_percentile = 80
example_fraction = survey.loc[survey.year == 2014, 'effort'].quantile(example_percentile / 100)
plt.plot([0, example_fraction, example_fraction],
         [example_percentile, example_percentile, 0],
         'grey', linestyle='--', alpha=0.5)
plt.text(example_fraction, 0, "{:.3f}".format(example_fraction), alpha=0.5)

note = 'In 2014, 80% of households\nspend less than {:1.1f}% of income\non electricity'
note_text = note.format(example_fraction * 100)

plt.annotate(note_text,
             xy=(example_fraction, example_percentile),
             xytext=(example_fraction + 0.005, example_percentile - 20),
             alpha=0.5,
             arrowprops=dict(facecolor='grey', shrink=0.0, width=2))

plt.xlabel('Fraction of income spend on electricity')
plt.ylabel('% Households')
plt.legend(['2014', '2012', '2010', '2008'], loc='lower right', frameon=False)

fig.savefig('effort.png')
fig.savefig('effort-300dpi.png', dpi=300)
