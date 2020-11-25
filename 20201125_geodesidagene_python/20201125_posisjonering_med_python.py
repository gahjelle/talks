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
# # %load_ext nb_black

import warnings

warnings.filterwarnings("ignore")

# %% [markdown] slideshow={"slide_type": "slide"}
# <h1 align="center">Posisjonering med Python</h1>
#
# <h2 align="center">Geir Arne Hjelle</h2>
#
# <h3 align="center">Geodesi- og Hydrografidagene</h3>
# <h3 align="center">25. november, 2020</h3>

# %% [markdown] slideshow={"slide_type": "slide"}
# **Python** er et populært programmeringsspråk, særlig innen **dataanalyse**

# %% [markdown] slideshow={"slide_type": "fragment"}
# - basert på **pakker**, ofte utviklet av frivillige
# - pakkene er tilgjengelige på [pypi.org](https://pypi.org/)
# - mange pakker for **GIS og kartanvendelser**
# - bygd på toppen av biblioteker som **GDAL**, **PROJ**, osv

# %% [markdown] slideshow={"slide_type": "fragment"}
# Denne presentasjonen vil vise frem en del av mulighetene

# %% [markdown] slideshow={"slide_type": "slide"}
# # Folium
#
# **Folium** er et overbygg over **LeafletJS** og gir tilgang til interaktive kart:

# %% slideshow={"slide_type": "fragment"}
import folium

kart = folium.Map((60, 10), zoom_start=10)
kart

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Folium
#
# La oss definere noen punkter vi kan bruke i demonstrasjonen:

# %% slideshow={"slide_type": "-"}
punkter = {
    "Andenes": (69.32, 16.12),
    "Hvervenmoen": (60.14, 10.25),
    "Oslo": (59.92, 10.75),
    "Stavanger": (58.97, 5.74),
}

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Folium
#
# Du kan koble deg på forskjellige **WMTS-tjenester** - inkludert Kartverkets tjenester. Du kan også legge til **markører**, **polygoner** og annen informasjon:

# %% slideshow={"slide_type": "-"}
kv_topo4 = "https://opencache.statkart.no/gatekeeper/gk/gk.open_gmaps?layers=topo4&zoom={z}&x={x}&y={y}"

kart = folium.Map((60, 10), zoom_start=6, tiles=kv_topo4, attr="Kartverket")
for navn, posisjon in punkter.items():
    folium.Marker(posisjon, popup=navn).add_to(kart)

kart

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Folium
#
# **Folium** er spesielt nyttig for å **utforske** og **få oversikt** over dataene dine.
#
# Pakken kan også fungere som en platform for å **visualisere** data for sluttbrukere.
#
# Se [python-visualization.github.io/folium/](https://python-visualization.github.io/folium/) for mer informasjon.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Geopandas
#
# **Geopandas** er bygd på toppen av, og sammenstiller funksjonaliteten fra, mange forskjellige Pythonpakker:

# %% [markdown] slideshow={"slide_type": "fragment"}
# - **pandas**: Dataanalyse
# - **Shapely**: Beskrivelse av punkter, polygoner, osv
# - **Fiona**: Lesing og skriving av geofilformater som Shape, GeoJSON, osv
# - **PyProj**: Konvertering og transformasjon av koordinater, basert på **Proj**
# - **Descartes**: Tegn punkter, polygoner osv i **Matplotlib**-figurer

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas

# %% slideshow={"slide_type": "-"}
import geopandas as gpd
from shapely import geometry


data = gpd.GeoDataFrame(
    {
        "navn": [navn for navn in punkter.keys()],
        "lengde": [len(navn) for navn in punkter.keys()],
    },
    geometry=[geometry.Point(posisjon[::-1]) for posisjon in punkter.values()],
    crs="epsg:4326",
)
data

# %% slideshow={"slide_type": "fragment"}
data.query("lengde <= 8")

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# Geopandas (egentlig **Fiona**) støtter ikke SOSI-filer, men programmet [Sosicon](https://sosicon.espenandersen.no/) kan brukes for å konvertere SOSI til Shape eller andre støttede formater.
#
# Her er et eksempel hvor vi bruker fylkespolygoner lastet ned fra [GeoNorge](https://www.geonorge.no/).

# %% slideshow={"slide_type": "fragment"}
fylker = gpd.read_file("Basisdata_0000_Norge_25833_Fylker_SOSI_Fylke_FLATE.shp")
fylker

# %% [markdown] slideshow={"slide_type": "fragment"}
# Legg merke til at hver geometri (hvert fylkespolygon) har en del tilhørende informasjon.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# Geopandas støtter enkel opptegning av de geografiske dataene.

# %% slideshow={"slide_type": "-"}
fylker.plot(figsize=(6, 6))

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# Dette kan kombineres med spørringer og annen pandas-funksjonalitet.

# %% slideshow={"slide_type": "-"}
fylker.astype({"FYLKESNUMM": int}).query("FYLKESNUMM <= 20").plot(figsize=(6, 6))

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# Du kan også fargelegge kartet basert på tilhørende data.

# %% slideshow={"slide_type": "-"}
fylker.assign(areal=lambda df: df.area / 1_000_000).plot(column="areal", figsize=(6, 6))

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# Gjennom **PyProj** støtter Geopandas koordinattransformasjoner.
#
# Referansesystemet for fylkesdatasettet er UTM33:

# %% slideshow={"slide_type": "-"}
fylker.crs

# %% [markdown]
# Vi kan transformere til lengde-bredde:

# %% slideshow={"slide_type": "fragment"}
fylker.to_crs(epsg=4326).plot(figsize=(6, 6))

# %% [markdown] slideshow={"slide_type": "fragment"}
# Etterhvert som Kartverkets transformasjoner blir tilgjengelige gjennom **Proj** vil de også bli tilgjengelige i **Geopandas**.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Geopandas
#
# **Geopandas** er en **arbeidshest** for all analyse av geografiske data.
#
# Pakken gir tilgang til mye nyttig funksjonalitet i en pakke, og kan brukes til **dataanalyse**, **konvertering** mellom filformater, **transformasjoner** av koordinater, og statiske **visualiseringer**.
#
# Se [geopandas.org](https://geopandas.org/) for mer informasjon.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Contextily
#
# **Contextily** kan brukes for lage statiske visualiseringer basert på WMTS-tjenester.

# %% slideshow={"slide_type": "fragment"}
import contextily as ctx

ax = (
    fylker.query("FYLKESNUMM > '20'")
    .to_crs(epsg=3857)
    .plot(column="FYLKESNUMM", alpha=0.6, figsize=(6, 6))
)
ctx.add_basemap(ax)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Contextily
#
# På samme måte som for **Folium** støtter Contextily forskjellige WMTS-tjenester, inkludert Kartverkets:

# %% slideshow={"slide_type": "-"}
holmenkollen = gpd.read_file("holmenkollen.json")
holmenkollen

# %% slideshow={"slide_type": "fragment"}
kv_norgeibilder = "http://opencache.statkart.no/gatekeeper/gk/gk.open_nib_web_mercator_wmts_v2?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=Nibcache_web_mercator_EUREF89_v2&STYLE=default&FORMAT=image/jpgpng&TILEMATRIXSET=default028mm&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}"

ax = holmenkollen.to_crs(epsg=3857).plot(alpha=0.3, figsize=(6, 6))
ctx.add_basemap(ax, source=kv_norgeibilder, zoom=16)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Contextily
#
# **Contextily** utvider bruksområdene til WMTS-tjenester, og støtter også transformering av kartfliser.
#
# Pakken er spesielt nyttig for fleksible, statiske **visualiseringer**.
#
# Se [contextily.readthedocs.io](https://contextily.readthedocs.io/) for mer info.

# %% [markdown] slideshow={"slide_type": "slide"}
# # RasterIO
#
# **RasterIO** er en pakke for å lese og jobbe med raster-data, slik som for eksempel **høydemodeller**. Her bruker vi en Digital OverflateModell fra [hoydedata.no](https://hoydedata.no/):

# %% slideshow={"slide_type": "fragment"}
import rasterio
from rasterio import plot

dom = rasterio.open("DOM_32-1-514-135-40.tif")
dom.meta

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## RasterIO
#
# RasterIO jobber sammen med **Matplotlib** for enkle visualiseringer av rasterdataene:

# %% slideshow={"slide_type": "-"}
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1, figsize=(6,6))
plot.show(dom, ax=ax, cmap="terrain", aspect="equal")
plot.show(dom, ax=ax, contour=True, levels=range(200, 400, 20), alpha=0.3)
plt.show()


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## RasterIO
#
# RasterIO kan kombineres med polygoner og andre geometrier for å **maskere** dataene.

# %% slideshow={"slide_type": "-"}
import numpy as np
from rasterio import mask

stadion, transform = mask.mask(dom, holmenkollen.to_crs("epsg:25832").geometry, crop=True)
stadion[stadion < 0] = np.nan
plt.imshow(stadion[0], cmap="terrain", aspect="equal")

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## RasterIO
#
# **RasterIO** gir effektiv tilgang til raster-data.
#
# Pakken støtter mange operasjoner inkludert **transformasjoner**, **kombinasjon** av data, **maskeringer** osv.
#
# Se [rasterio.readthedocs.io](https://rasterio.readthedocs.io/) for mer informasjon.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Midgard
#
# **Midgard** er en pakke utviklet av **Kartverket**. Midgard startet som et støttebibliotek til **Where**, Kartverkets programvare for å beregne referanserammer basert på VLBI, SLR, og GNSS.

# %% [markdown] slideshow={"slide_type": "fragment"}
# Midgard gir tilgang til en datastruktur for sammenstilling av **posisjon**, **hastighet** og **tid** med geodetisk nøyaktighet.

# %% slideshow={"slide_type": "-"}
from midgard.data import dataset

dset = dataset.Dataset(num_obs=4)
dset.add_text("navn", val=list(punkter.keys()))
dset.add_time("tidspunkt", val=["2020-11-25T11:30:00"] * 4, scale="utc", fmt="isot")
dset.add_position("posisjon", val=np.array([[pkt[0] for pkt in punkter.values()], [pkt[1] for pkt in punkter.values()], [10, 20, 40, 25]]).T, system="llh", time="tidspunkt")
print(dset)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Midgard
#
# Posisjoner og hastigheter støtter forskjellige koordinatsystemer:
#
# - **llh**: Breddegrad, Lengdegrad, Høyde
# - **trs**: XYZ
# - **enu**: Lokalt Øst, Nord, Opp

# %% slideshow={"slide_type": "-"}
dset.posisjon.to_system("trs")

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Midgard
#
# Tid kan konverteres mellom forskjellige **tidsskalaer** (UTC, TAI, GPS, osv) og **tidsformater** (tekst, Julian Day, Python `datetime`, osv)

# %% slideshow={"slide_type": "-"}
print(dset.tidspunkt.tai)
print(dset.tidspunkt.gps.jd)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Midgard
#
# **Midgard** kan brukes til å gjøre effektive beregninger på geodetiske punkter.
#
# Pakken er nyttig for å behandle tidsserier med høyest mulig nøyaktighet.
#
# Se [kartverket.github.io/midgard](https://kartverket.github.io/midgard/) for mer informasjon.
#
# **Where** ([kartverket.github.io/where](https://kartverket.github.io/where/)) er programvare som bruker Midgard til databehandlingen.

# %% [markdown] slideshow={"slide_type": "slide"}
# <h1 align="center">Takk for meg!</h1>
#
# <h2 align="center">geirarne@gmail.com</h2>
