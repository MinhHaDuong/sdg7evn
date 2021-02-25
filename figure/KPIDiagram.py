# Statistics on energy poverty in Vietnam
##
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
#
# sudo pip3 install matplotlib-venn
import matplotlib.pyplot as plt

from matplotlib_venn import venn3
from matplotlib import gridspec

from VHLSS_importer import survey

# %%

# Subsampling to Q12 respondents does not change much the
# percentages for off_grid, low_use, high_cost

data = survey[(survey.year == 2014) & survey.elec_poor.notnull()]

label = {
    "low_use": "Used <30kWh",
    "lacking": "Needs not met",
    "high_cost": "Bill > 6% income",
    "LIHC": "Low income high cost",
    "subsidized": "Subsidized",
}


def cover3(col1, col2, col3, axe):
    gb = data.groupby([col1, col2, col3]).size()
    # Handle exception when the 3-way intersection is empty
    try:
        gb[1, 1, 1]
    except KeyError:
        gb.loc[1, 1, 1] = 0
    venn3(
        subsets=(
            gb[1, 0, 0],
            gb[0, 1, 0],
            gb[1, 1, 0],
            gb[0, 0, 1],
            gb[1, 0, 1],
            gb[0, 1, 1],
            gb[1, 1, 1],
        ),
        set_labels=([label[col1], label[col2], label[col3]]),
        ax=axe,
    )
    axe.text(-0.6, -0.5, "All other: " + str(gb[0, 0, 0]) + " replies")
    return sum(gb)


fig = plt.figure(figsize=(10, 10))
gs = gridspec.GridSpec(6, 2)

n = cover3("low_use", "lacking", "high_cost", fig.add_subplot(1, 1, 1))

fig.suptitle(
    "Energy poverty in Vietnam Households 2014 survey\n(n=" + str(n) + ")", fontsize=18
)

plt.tight_layout()

fig.savefig("KPIDiagram.png")
fig.savefig("KPIDiagram-300dpi.png", dpi=300)
