# 🌎 2017 M6.3 AegeanSea earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2017 M6.3 AegeanSea earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2017 Aegean Sea earthquake`, registering a magnitude of 6.3 and an MMI of VII, struck on June 12, 2017, at 15:28 local time. The epicenter was located in the Aegean Sea, approximately 5 kilometers south of Plomari on the island of Lesbos, Greece. The earthquake caused significant devastation, with the most affected areas being southern Lesbos, particularly the village of Vrisa, which suffered extensive structural damage, and parts of western Turkey, including Izmir. The disaster resulted in 1 fatality and 15 injuries, primarily concentrated on Lesbos. While liquefaction was not widely reported, the earthquake triggered landslides in some hilly regions and a minor tsunami that caused localized impacts along the coastlines.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2017 |
| Country | Greece |
| Region | Europe |
| Event Name | AegeanSea 2017 |
| Local Date | 12/06/2017 |
| Local Time | 12:28:39 |
| Latitude (decimal degrees) | 38.9296 |
| Longitude (decimal degrees) | 26.365 |
| Depth (km) | 12 |
| Mw | 6.3 |
| Max Intensity (MMI) | VII |
| Fault mechanism | Normal |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | us20009ly0 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~1 |
| Injured | 11-15 |
| Displaced population | nan |
| Affected population | ~731 |
| Affected units | nan |
| Damaged units | 250 Buildings |
| Collapsed units | 10 Buildings |
| Economic losses | nan |
| Insured losses | nan |
| Earthquake-triggered effects | nan |