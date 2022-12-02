# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
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
# <h3 align="center">PyData Global 2022</h3>
# <h3 align="center">December 2nd, 2022</h3>

# %% [markdown] slideshow={"slide_type": "slide"}
# # Geir Arne Hjelle
#
# - Lives in **Oslo, Norway**
# - Works at **Real Python** ([realpython.com](https://realpython.com/))
# - Experience with **Python** since 2012
# - Worked at the **Norwegian Mapping Authority**

# %% [markdown] slideshow={"slide_type": "slide"}
# # Folium
#
# **Folium** is a wrapper around the **LeafletJS** JavaScript library, and can be used for making interactive maps:

# %% slideshow={"slide_type": "-"}
import folium

map = folium.Map((0, 0), zoom_start=3)
map

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Folium
#
# We can add custom locations to use in the presentation:

# %% slideshow={"slide_type": "-"}
locations = {
    "Andenes": (69.32, 16.12),
    "Oslo": (59.92, 10.75),
    "Barcelona": (41.39, 2.16),
    "St. Louis": (38.63, -90.20),
}

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Folium
#
# You can connect to different Web Map Tile Services (WMTS), and display markers, polygons and other information on your map:

# %% slideshow={"slide_type": "-"}
map = folium.Map((25, 0), zoom_start=3, tiles="stamenwatercolor")
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
# - **Folium**: Add data to interactive maps

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Shapely
#
# **Shapely** deals with abstract **points**, **lines**, **polygons** and similar geometric objects

# %% slideshow={"slide_type": "-"}
from shapely import geometry

point = geometry.Point((2, 3))
line = geometry.LineString([(5, 0), (2, 6)])
square = geometry.Polygon([(1, 1), (1, 4), (4, 4), (4, 1), (1, 1)])

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Shapely
#
# You can inspect **Shapely** objects

# %% slideshow={"slide_type": "-"}
list(line.coords)

# %% slideshow={"slide_type": "-"}
line

# %% slideshow={"slide_type": "-"}
square

# %% [markdown] slideshow={"slide_type": "subslide"}
# # Shapely
#
# **Shapely** supports lots of calculations, transformations, predicates, and other operations

# %% slideshow={"slide_type": "-"}
point.union(line)

# %%
str(point.union(line))

# %% slideshow={"slide_type": "-"}
point.distance(line)

# %%
square.area

# %% slideshow={"slide_type": "-"}
square.contains(point)

# %% slideshow={"slide_type": "-"}
line.intersects(square)

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
# Geopandas lets you explore the data on an interactive map provided by **Folium**:

# %% slideshow={"slide_type": "-"}
data.explore(marker_kwds={"radius": 20}, tiles="stamenwatercolor")

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

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# Note that each geometry (each country polygon) has some attached information.

# %% slideshow={"slide_type": "-"}
countries.columns

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# Geopandas can also draw the data to **Matplotlib** plots:

# %% slideshow={"slide_type": "-"}
countries.plot(figsize=(15, 15));

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# Plots can also be combined with queries and other pandas functionality:

# %% slideshow={"slide_type": "-"}
countries.query("POP_EST >= 50_000_000").plot(figsize=(15, 15));

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# You can color the map based on one of the columns:

# %% slideshow={"slide_type": "-"}
import numpy as np

(
    countries.assign(log_pop=np.log10(countries.POP_EST))
    .plot(column="log_pop", figsize=(10, 10), cmap="winter")
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
    .plot(column="POP_EST", alpha=0.5, figsize=(8, 8))
)
ctx.add_basemap(ax, zoom=2)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Contextily
#
# Contextily also supports different WMTS providers:

# %% slideshow={"slide_type": "-"}
ax = (
    countries.query("CONTINENT == 'South America' and NAME_EN.str.startswith('B')")
    .to_crs("epsg:3857")
    .plot(column="POP_EST", alpha=0.3, figsize=(8, 8))
)
ctx.add_basemap(ax, source=ctx.providers.Esri )

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Contextily
#
# We can also work with **GEOJSON**

# %% slideshow={"slide_type": "-"}
holmenkollen = gpd.read_file("holmenkollen.json")
holmenkollen

# %% slideshow={"slide_type": "-"}
kv_norgeibilder = "http://opencache.statkart.no/gatekeeper/gk/gk.open_nib_web_mercator_wmts_v2?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=Nibcache_web_mercator_EUREF89_v2&STYLE=default&FORMAT=image/jpgpng&TILEMATRIXSET=default028mm&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}"

ax = holmenkollen.to_crs(epsg=3857).plot(alpha=0.3, figsize=(6, 6))
ctx.add_basemap(ax, source=kv_norgeibilder, zoom=16)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Contextily
#
# **Contextily** extends areas Web Map Tile Services can be used. It also supports transforming map tiles.
#
# The package is great for flexible, beautiful, static **visualizations**
#
# See [contextily.readthedocs.io](https://contextily.readthedocs.io/) for more information.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## RasterIO
#
# **RasterIO** handles raster data, typically geographical information stored in a grid

# %% slideshow={"slide_type": "-"}
import rasterio

surface_model = rasterio.open("DOM_32-1-514-135-40.tif")
surface_model.meta

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## RasterIO
#
# You can plot the grid or do some analysis on it

# %% slideshow={"slide_type": "-"}
import matplotlib.pyplot as plt
from rasterio import plot

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
plot.show(surface_model, ax=ax1, cmap="terrain")
plot.show(surface_model, ax=ax2, contour=True, levels=range(200, 400, 20), alpha=1)
plt.show()

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## RasterIO
#
# You can combine RasterIO with polygons and other geometric objects to mask your data

# %% slideshow={"slide_type": "-"}
import numpy as np
from rasterio import mask

arena, transform = mask.mask(surface_model, holmenkollen.to_crs("epsg:25832").geometry, crop=True)
arena[arena < 0] = np.nan
plt.imshow(arena[0], cmap="terrain", aspect="equal")
plt.show()

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## RasterIO
#
# **RasterIO** gives you effective and powerful access to raster data.
#
# The library supports many operations, including **transformations**, **combining data**, and **mask**.
#
# See [rasterio.readthedocs.io](https://rasterio.readthedocs.io/) for more information.
#

# %% [markdown] slideshow={"slide_type": "slide"}
# <h1 align="center">🎆 Thank you for your attention! 🎆</h1>
#
# <h2 align="center">@gahjelle</h2>
#
# <h3 align="center">github.com/gahjelle/talks</h3>
