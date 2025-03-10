# 🌎 2020 M7 AegeanSea earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2020 M7 AegeanSea earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2020 Aegean Sea earthquake`, a magnitude 7.0 event, struck the eastern Aegean Sea on October 30, 2020, at 14:51 local time. The maximum Mercalli intensity reached VIII. The epicenter was located in the Aegean Sea, between the Greek islands of Samos and Ikaria. This powerful earthquake caused significant damage in both Greece and Turkey. The most affected cities included İzmir in Turkey and Samos Town in Greece. The death toll exceeded 117, with over 1000 injuries reported. Economic losses were around 400 million USD, and the earthquake triggered numerous landslides and some localized liquefaction. A small tsunami, with waves up to 1.5 meters, was observed in some coastal areas.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2020 |
| Country | Turkey |
| Region | Europe |
| Event Name | AegeanSea 2020 |
| Local Date | 30/10/2020 |
| Local Time | 14:51:27 |
| Latitude (decimal degrees) | 37.8973 |
| Longitude (decimal degrees) | 26.7838 |
| Depth (km) | 21 |
| Mw | 7 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Normal |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | us7000c7y0 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 117-119 |
| Injured | 1034-1632 |
| Displaced population | 5000-15000 |
| Affected population | ~6034 |
| Affected units | 8703 Buildings |
| Damaged units | 700 Buildings |
| Collapsed units | 103 Buildings |
| Economic losses | 400-450 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |