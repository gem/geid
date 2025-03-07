# 🌎 1999 M7.4 Oaxaca earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1999 M7.4 Oaxaca earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1999 Oaxaca earthquake` struck on September 30, 1999, at approximately 11:31 local time, with a moment magnitude (Mw) of 7.4 and a maximum intensity of VIII on the Modified Mercalli Intensity (MMI) scale. The earthquake’s epicenter was located off the coast of southern Mexico near Puerto Ángel, in the state of Oaxaca. Among the most severely impacted areas were Oaxaca and neighboring regions in Chiapas and Guerrero, where significant damage to infrastructure and buildings was reported. The disaster resulted in economic losses exceeding $164 million USD, claimed the lives of over 30 individuals, and left more than 160 injured. The earthquake triggered instances of liquefaction and landslides, particularly in vulnerable zones, though no tsunamis or fires were observed. The event was followed by numerous aftershocks, some of which were strong enough to heighten concerns and cause additional minor damage. Notably, no foreshocks were recorded preceding the mainshock.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1999 |
| Country | Mexico |
| Region | North America |
| Event Name | Oaxaca 1999 |
| Local Date | 30/09/1999 |
| Local Time | 11:31:13 |
| Latitude (decimal degrees) | 16.056 |
| Longitude (decimal degrees) | -97.004 |
| Depth (km) | 39 |
| Mw | 7.4 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Normal |
| Tectonic region type | Subduction Intraslab |
| USGS event ID | usp0009f7v |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 31-50 |
| Injured | 160-215 |
| Displaced population | nan |
| Affected population | ~115000 |
| Affected units | ~86628  |
| Damaged units | 2000-45697  |
| Collapsed units | ~9538  |
| Economic losses | 164.8 M USD  |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides  |