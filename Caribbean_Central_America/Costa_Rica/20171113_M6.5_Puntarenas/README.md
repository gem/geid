# 🌎 2017 M6.5 Puntarenas earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2017 M6.5 Puntarenas earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance

The `2017 Puntarenas earthquake`, also referred to as the Jacó earthquake, struck on November 12, 2017, at 20:28 local time in Costa Rica. With a moment magnitude of 6.5, the earthquake's epicenter was located approximately 16 kilometers southeast of Jacó, a coastal town in the Puntarenas province. The earthquake's maximum observed intensity reached VIII on the Modified Mercalli Intensity (MMI) scale, denoting severe shaking. The most affected areas included Jacó, Puntarenas, and surrounding coastal regions. The earthquake caused significant damage to buildings and infrastructure, particularly in the impacted areas. Reported fatalities ranged from 2 to 3 individuals, while no substantial occurrences of liquefaction, landslides, tsunamis, or fires were observed. Following the main event, a series of aftershocks occurred, with the largest ones taking place in the days that followed. Notably, there were no major foreshocks recorded before the earthquake.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2017 |
| Country | Costa Rica |
| Region | Caribbean Central America |
| Event Name | Puntarenas 2017 |
| Local Date | 12/11/2017 |
| Local Time | 20:28:23 |
| Latitude (decimal degrees) | 9.448 |
| Longitude (decimal degrees) | -84.544 |
| Depth (km) | 22 |
| Mw | 6.5 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Reverse Fault |
| Tectonic region type | Subduction Interface |
| USGS event ID | us2000bmhe |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 2-3 |
| Injured | nan |
| Displaced population | nan |
| Affected population | nan |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | nan |
| Economic losses | nan |
| Insured losses | nan |
| Earthquake-triggered effects | nan |