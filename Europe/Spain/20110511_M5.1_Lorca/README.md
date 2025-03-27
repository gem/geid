# 🌎 2011 M5.1 Lorca earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2011 M5.1 Lorca earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2011 Lorca earthquake`, a magnitude 5.1 event, struck southeastern Spain on May 11, 2011, at 18:47 local time. Its epicenter was located near the town of Lorca. The earthquake caused significant damage, particularly to older structures, resulting in around 9 fatalities and over 320 injuries. Economic losses were substantial, exceeding 700 million EUR. The earthquake's intensity reached a maximum of VI on the Modified Mercalli Intensity scale.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2011 |
| Country | Spain |
| Region | Europe |
| Event Name | Lorca 2011 |
| Local Date | 11/05/2011 |
| Local Time | 18:47:25 |
| Latitude (decimal degrees) | 37.699 |
| Longitude (decimal degrees) | -1.672 |
| Depth (km) | 1 |
| Mw | 5.1 |
| Max Intensity (MMI) | VI |
| Fault mechanism | Strike-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp000j1en |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 0.376g, observed close to Lorca. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~9 |
| Injured | ~300 |
| Displaced population | nan |
| Affected population | nan |
| Affected units | nan |
| Damaged units | ~889 |
| Collapsed units | ~1 |
| Economic losses | 700 M EUR |
| Insured losses | 484.7 M EUR |
| Earthquake-triggered effects | nan |