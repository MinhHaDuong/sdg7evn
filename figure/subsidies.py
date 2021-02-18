# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#
# sudo pip3 install matplotlib-venn
import matplotlib.pyplot as plt

from matplotlib_venn import venn2
from matplotlib import gridspec

from VHLSS_importer import survey

# %%

# Subsampling to Q12 respondents does not change much the
# percentages for off_grid, low_use, high_cost

data = survey[(survey.year == 2014) & survey.elec_poor.notnull()]


english = {
    "low_use": "Used <30kWh",
    "lacking": "Needs not met",
    "high_cost": "Bill > 6% income",
    "poor": "Low income",
    "LIVLU": "Low income & use < 30kWh",
    "LILU": "Low income & use < 50 kWh",
    "subsidized": "Subsidized",
}


def cover_two(col1, col2, axe):
    gb = data.groupby([col1, col2]).size()
    venn2(
        subsets=(gb[1, 0], gb[0, 1], gb[1, 1]),
        set_labels=([english[col1], english[col2]]),
        ax=axe,
    )


fig = plt.figure(figsize=(10, 3))
gs = gridspec.GridSpec(2, 3)

cover_two("subsidized", "low_use", fig.add_subplot(gs[0, 1]))
cover_two("subsidized", "lacking", fig.add_subplot(gs[0, 0]))
cover_two("subsidized", "high_cost", fig.add_subplot(gs[1, 0]))
cover_two("subsidized", "poor", fig.add_subplot(gs[1, 1]))
cover_two("subsidized", "LILU", fig.add_subplot(gs[1, 2]))
cover_two("subsidized", "LIVLU", fig.add_subplot(gs[0, 2]))

plt.tight_layout()

fig.savefig("subsidies.png")
fig.savefig("subsidies-300dpi.png", dpi=300)
