# Plot the electricity tariff in Vietnam.

"""
Plot the electricity tariff in Vietnam.

(c) 2016-2021 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from VHLSS_importer import electricity_tariffs, CPI

# %%

for date in electricity_tariffs.index:
    CPI.loc[date] = np.nan

CPI.interpolate(method='time', inplace=True)

deflated_tariff = pd.DataFrame()

for date in electricity_tariffs.index:
    for block in electricity_tariffs.columns:
        t = float(electricity_tariffs.loc[date, block])
        d = float(CPI.loc[date]) / 100
        deflated_tariff.loc[date, block] = t/d


# %%

fig = plt.figure(figsize=(11, 5.5))

ax = fig.add_subplot(121)

electricity_tariffs.plot(ax=ax, legend=False)

ax.set_xlabel("")
ax.set_ylabel("VND / kWh")
ax.set_ylim([0, 3000])
ax.set_title("""VN households electricity tariff, nominal""")

(5 * CPI).plot(ax=ax, linewidth=3.0, linestyle='dashed')

# Source: https://www.vietcombank.com.vn/exchangerates/   Accessed 2016-09-28
VNDperUSD = 22265

# %%

ax2 = fig.add_subplot(122)

deflated_tariff.plot(ax=ax2)

ax2.set_xlabel("")
ax2.set_ylabel("VND / kWh")
ax2.set_ylim([0, 3000])
ax2.set_title("""VN households electricity tariff, deflated""")

# Source: https://www.vietcombank.com.vn/exchangerates/   Accessed 2016-09-28
# VNDperUSD = 22265
#
# ax3 = ax.twinx()
# ax3.set_ylim([0, 1500 / VNDperUSD])
# ax3.set_ylabel("US cents / kWh")

plt.tight_layout()

# %%plt.tight_layout()

fig.savefig("prices.png")
fig.savefig("prices-300dpi.png", dpi=300)
