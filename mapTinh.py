# Choropleth mapping a numerical function by province in Vietnam
#
# (c) 2016 Minh Ha-Duong, CNRS, CC-ATTRIBUTION-SHAREALIKE
#
# Code lifted from stackoverflow question 15968762
# Doc is at:  https://pypi.python.org/pypi/pyshp
# On Ubuntu: "sudo apt install python3-pyshp"
#
# Usage:
#  fig = pyplot.figure(figsize=(3, 5), dpi=300)
#  ax = fig.add_subplot(111)
#  mapTinh(FUNCTIONTOPLOT, ax, 'Title')
#  fig.savefig('figure1.png')
#
# FUNCTIONTOPLOT takes one integer argument 'tinh'
#  returns one number between 0 and 1
#
# Notes:
# Borders between provinces drawn in 'cyan' because the islands have dense ink
# Density in level of 'Greys' because Internet says it's best
# Displaying the proportion misleads the eye for two reasons
#  - The quantity of ink is integrated on the surface, so a larger province
#      would be perceived as more problematic than a smaller province
#  - Provinces have different population density

from VHLSS_importer import DATADIR, provinceTinhByName

import shapefile

from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.cm import get_cmap
from matplotlib import pyplot, colorbar

DEBUG = False


sf = shapefile.Reader(DATADIR + "VNM_adm_shp/VNM_adm1")
recs = sf.records()
provinceNames = [row[11] for row in recs]
provinceNamesVN = [row[4] for row in recs]
provinceNum = [row[3] for row in recs]
# There are 65 shapes because two provinces get two shapes
# They are provinces 33 (Kien Giang at index 32, 33)
# and 42 (Ninh Binh indexes 42, 43)
# This is not a problem for coloring


def mapTinh(f, ax, title, colormap_name):
    colormap = get_cmap(colormap_name)

    for i, shape in enumerate(sf.shapes()):
        ptchs = []
        pts = list(shape.points)
        prt = shape.parts
        par = list(prt) + [len(pts)]
        tinh = provinceTinhByName[provinceNames[i]]
        stat = f(tinh)
        color = colormap(stat)
        ec = "black"
        if i in {7, 25, 29, 31, 33, 50}:
            ec = "lightgrey"  # Lower ink density for finely contoured islands provinces
        for pij in range(len(prt)):
            ptchs.append(Polygon(pts[par[pij] : par[pij + 1]]))
            ax.add_collection(
                PatchCollection(ptchs, facecolor=color, edgecolor=ec, linewidths=0.1)
            )
    ax.set_xlim(+102, +111)
    ax.set_ylim(+8, +23.3)
    ax.axis("off")
    ax.set_title(title)
    return 0


def plotChoropleths(f, label, filename, years):
    if not DEBUG:
        fig = pyplot.figure(figsize=(18, 10), dpi=150)
    else:
        fig = pyplot.figure(figsize=(9, 5), dpi=50)
    if DEBUG:
        years = [2008]
    colormap_name = "Greys"
    for yr in years:
        ax = fig.add_subplot(1, len(years), years.index(yr) + 1)
        mapTinh(lambda t: f(yr, t), ax, str(yr), colormap_name)
    cbaraxes = fig.add_axes([0.05, 0.15, 0.02, 0.7])
    cbar = colorbar.ColorbarBase(cbaraxes, cmap=get_cmap(colormap_name))
    cbar.set_ticks([0.0, 0.2, 0.4, 0.6, 0.8, 1])
    cbar.set_ticklabels(["0%", "20%", "40%", "60%", "80%", "100%"])
    cbar.set_label(label)
    if not DEBUG:
        fig.savefig(filename + ".png")
        fig.savefig(filename + "-300dpi.png", dpi=300)
