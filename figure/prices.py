"""
Plot the households electricity tariff in Vietnam over time.

(c) 2016-2021 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from VHLSS_importer import electricity_tariffs, CPI

# %%

for date in electricity_tariffs.index:
    if date not in CPI.index:
        CPI.loc[date] = np.nan

CPI.interpolate(method='time', inplace=True)

deflated_tariff = pd.DataFrame()
base = CPI["2002-01-31"][0]

for date in electricity_tariffs.index:
    for block in electricity_tariffs.columns:
        t = electricity_tariffs.at[date, block]
        d = CPI[date]
        deflated_tariff.loc[date, block] = t / d * base


# %%

fig = plt.figure(figsize=(11, 5.5))

ax = fig.add_subplot(121)

electricity_tariffs.plot(ax=ax, legend=False, drawstyle="steps-post")

ax.set_xlabel("")
ax.set_ylabel("VND / kWh")
ax.set_ylim([0, 3000])
ax.set_title("""Nominal households electricity tariff""")

# (5 * CPI).plot(ax=ax, linewidth=3.0, linestyle='dashed')

# %%

ax2 = fig.add_subplot(122)

deflated_tariff.plot(ax=ax2, drawstyle="steps-post")

ax2.set_xlabel("")
ax2.set_ylabel("VND / kWh")
ax2.set_ylim([0, 3000])
ax2.set_title("""Deflated households electricity tariff""")

plt.tight_layout()

# %%

fig.savefig("prices.png")
fig.savefig("prices-300dpi.png", dpi=300)
