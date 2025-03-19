# 🌎 2005 M6.5 Zarand earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2005 M6.5 Zarand earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2005 Zarand earthquake` in Iran occurred on February 22, 2005, at 5:55 AM local time, with a moment magnitude of 6.5. Its epicenter was located near Zarand in Kerman Province, in southeastern Iran. The earthquake caused widespread damage across several regions, with Zarand being the most severely affected city. The Maximum Modified Mercalli Intensity (MMI) reached VIII, indicating intense shaking. The earthquake resulted in significant economic losses, estimated at over $79 million USD, primarily due to building damage and infrastructure destruction. Tragically, it led to at least 400 fatalities and over 1000 injuries. Reports indicate that landslides were triggered by the shaking, although no tsunamis or fires were observed. While there were no major foreshocks, the region experienced several aftershocks, some of which caused additional damage and panic among the affected population.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2005 |
| Country | Iran |
| Region | Middle East |
| Event Name | Zarand |
| Local Date | 22/02/2005 |
| Local Time | 05:55:21 |
| Latitude (decimal degrees) | 30.804 |
| Longitude (decimal degrees) | 56.746 |
| Depth (km) | 14 |
| Mw | 6.5 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Thrust |
| Tectonic region type | Active Crustal |
| USGS event ID | usp000dgpx |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 400-912 |
| Injured | 1000-2000 |
| Displaced population | nan |
| Affected population | 32000-93355 |
| Affected units | nan |
| Damaged units | 7000-15087 Buildings |
| Collapsed units | 8000-12449 Buildings |
| Economic losses | 79-80 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |