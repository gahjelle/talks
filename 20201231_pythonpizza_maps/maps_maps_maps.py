# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.5.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% slideshow={"slide_type": "skip"}
# %matplotlib inline

# %% [markdown] slideshow={"slide_type": "slide"}
# <h1 align="center">Maps, Maps, Maps!!</h1>
#
# <h2 align="center">Geir Arne Hjelle</h2>
#
# <h3 align="center">Python Pizza 🍕 New Year's Countdown</h3>
# <h3 align="center">December 31st, 2020</h3>

# %% [markdown] slideshow={"slide_type": "slide"}
# # Folium
#
# **Folium** is a wrapper around the **LeafletJS** JavaScript library, and can be used for making interactive maps:

# %% slideshow={"slide_type": "-"}
import folium

map = folium.Map((53.5, 10), zoom_start=5)
map

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Folium
#
# We can add custom locations to use in the presentation:

# %% slideshow={"slide_type": "-"}
locations = {
    "Andenes": (69.32, 16.12),
    "Hamburg": (53.55, 9.99),
    "Barcelona": (41.39, 2.16),
    "St. Louis": (38.63, -90.20),
}

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Folium
#
# You can connect to different Web Map Tile Services (WMTS), and display markers, polygons and other information on your map:

# %% slideshow={"slide_type": "-"}
map = folium.Map((40, 0), zoom_start=2, tiles="stamenwatercolor")
for name, latlon in locations.items():
    folium.Marker(latlon, popup=name).add_to(map)
map

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Folium
#
# **Folium** is great for **exploring** and getting an **overview** of your data.
#
# The package can also be used to **visualize** data for your end-users.
#
# See [python-visualization.github.io/folium/](https://python-visualization.github.io/folium/) for more information.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Geopandas
#
# **Geopandas** is built on top of, and brings together the functionality of many different geospatial Python packages:

# %% [markdown] slideshow={"slide_type": "fragment"}
# - **pandas**: Data analysis
# - **Shapely**: Describing points, polygons, etc
# - **Fiona**: Read and write geo-file formats like Shape, GeoJSON, etc
# - **PyProj**: Convert and transform coordinates. Based on **Proj**
# - **Descartes**: Draw points, polygons, etc in **Matplotlib** figures

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# Geopandas organizes data in **GeoDataFrames**:

# %% slideshow={"slide_type": "-"}
import geopandas as gpd
from shapely import geometry


data = gpd.GeoDataFrame(
    {
        "name": [name for name in locations.keys()],
        "size": [len(name) for name in locations.keys()],
    },
    geometry=[geometry.Point(latlon[::-1]) for latlon in locations.values()],
    crs="epsg:4326",
)
data

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# **GeoDataFrames** are also pandas **DataFrames** so all the pandas functionality is available:

# %% slideshow={"slide_type": "-"}
data.query("size <= 8")

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# The following example read data from a Shapefile, one of several common file formats for geodata:

# %% slideshow={"slide_type": "-"}
countries = gpd.read_file("ne_110m_admin_0_countries.shp")
countries.head()

# %% [markdown] slideshow={"slide_type": "fragment"}
# Note that each geometry (each country polygon) has some attached information.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# Geopandas can do simple drawing of the data:

# %% slideshow={"slide_type": "-"}
countries.plot(figsize=(10, 10));

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# Plots can also be combined with queries and other pandas functionality:

# %% slideshow={"slide_type": "-"}
countries.query("POP_EST >= 50_000_000").plot(figsize=(10, 10));

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# You can color the map based on one of the columns:

# %% slideshow={"slide_type": "-"}
import numpy as np

(
    countries.assign(log_pop=np.log10(countries.POP_EST))
    .plot(column="log_pop", figsize=(10, 10))
);

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# **Geopandas** is a **work horse** for all kinds of analysis of geodata.
#
# The package gives access to lots of functionality, and can do **data analysis**, **conversion** between file formats, **transformation** of coordinates, and static **visualizations**.
#
# See [geopandas.org](https://geopandas.org/) for more information.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Contextily
#
# **Contextily** kan be used to combine Web Map Tile Services with static visualizations:

# %% slideshow={"slide_type": "-"}
import contextily as ctx

ax = (
    countries.query("CONTINENT == 'North America'")
    .to_crs("epsg:3857")
    .plot(column="POP_EST", alpha=0.5, figsize=(10, 10))
)
ctx.add_basemap(ax)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Contextily
#
# Contextily also supports different WMTS providers:

# %% slideshow={"slide_type": "-"}
ax = (
    countries.query("CONTINENT == 'South America' and NAME_EN.str.startswith('B')")
    .to_crs("epsg:3857")
    .plot(column="POP_EST", alpha=0.3, figsize=(10, 10))
)
ctx.add_basemap(ax, source=ctx.providers.Esri.WorldImagery)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Contextily
#
# **Contextily** extends areas Web Map Tile Services can be used. It also supports transforming map tiles.
#
# The package is great for flexible, beautiful, static **visualizations**
#
# See [contextily.readthedocs.io](https://contextily.readthedocs.io/) for more information.

# %% [markdown] slideshow={"slide_type": "slide"}
# <h1 align="center">🎆 All the best for 2021! 🎆</h1>
#
# <h2 align="center">geirarne@gmail.com</h2>
