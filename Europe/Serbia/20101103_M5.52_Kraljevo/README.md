# 🌎 2010 M5.52 Kraljevo earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2010 M5.52 Kraljevo earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2010 Serbia earthquake` struck on November 3, 2010, at 01:56 local time, just several kilometers from Kraljevo, Serbia. The earthquake had a magnitude of 5.52 and a maximum Mercalli intensity of VI. Its epicenter was located near the village of Vitanovac. The earthquake was felt across Serbia, including the capital Belgrade, and in neighboring countries. Two people were killed and over 100 suffered injuries. Economic losses were estimated at around 138 million USD. There were more than 350 aftershocks, including a magnitude 4.3 earthquake the following day. No reports of liquefaction, tsunamis, or landslides were observed.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2010 |
| Country | Serbia |
| Region | Europe |
| Event Name | Kraljevo |
| Local Date | 03/11/2010 |
| Local Time | 01:56:55 |
| Latitude (decimal degrees) | 43.76 |
| Longitude (decimal degrees) | 20.73 |
| Depth (km) | 0.9 |
| Mw | 5.52 |
| Max Intensity (MMI) | VI |
| Fault mechanism | Reverse |
| Tectonic region type | Subduction Intraslab |
| USGS event ID | usp000hny4 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~2 |
| Injured | 100-120 |
| Displaced population | ~1470 |
| Affected population | ~25440 |
| Affected units | nan |
| Damaged units | 5000-5967 Buildings |
| Collapsed units | 1000-1550 Buildings |
| Economic losses | 0-138 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |