# Posisjonering Med Python

Presentasjon gitt på onlinekonferansen [Geodesi- og Hydrografidagene 2020](https://geoforum.no/geodesi-og-hydrografidagene-2020/) den 25. november 2020.


## Presentasjon

- [ [Presentasjon] ](posisjonering_med_python.ipynb)
- [ [Kode] ](posisjonering_med_python.py)

Presentasjonen ble gjort i en [Jupyter Notebook](https://jupyter.org/) med utvidelsen [RISE](https://rise.readthedocs.io/) som gir muligheten for å gjøre presentasjoner med kjørende kode.

Du kan se eksemplene fra presentasjonen ved å åpne [Notebook-filen](posisjonering_med_python.ipynb). Noen av eksemplene baserer seg på datafiler som også ligger i denne katalogen.

Presentasjonen er også direkte [konvertert](https://jupytext.readthedocs.io/) til en [Pythonfil](posisjonering_med_python.py) som også inneholder informasjon fra presentasjonen som kommentarer.

## Biblioteker

For å kjøre koden selv må du installere de relevante Pythonpakkene. Disse er listet opp i filen [`requirements.in`](requirements.in). Du kan installere alle bibliotekene ved å kjøre:

```
$ python -m pip install -r requirements.in
```

Filen [`requirements.txt`](requirements.txt) viser hvilke versjoner av de forskjellige bibliotekene som ble brukt i presentasjonen. Alle bibliotekene er i kontinuerlig utvikling. Det er som regel best å bruke seneste versjon av disse.

## Datafiler

- **Fylkespolygoner**: Lastet ned fra [GeoNorge](https://kartkatalog.geonorge.no/metadata/6093c8a8-fa80-11e6-bc64-92361f002671). Konvertert fra SOSI til Shape med [SosiCon](https://sosicon.espenandersen.no/).
- **Digital OverflateModell**: Lastet ned fra [Høydedata](https://hoydedata.no/)
- **Holmenkollen stadion, polygon**: Manuelt tegnet på [geojson.io](https://geojson.io/#map=16/59.9637/10.6728)
