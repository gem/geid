# 🌎 2007 M7.9 Pisco earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2007 M7.9 Pisco earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance

The `2007 Pisco earthquake` struck the central coast of Peru on August 15, 2007, at 6:40 p.m. local time. With a moment magnitude of 7.9, the epicenter was located approximately 50 kilometers west-northwest of Chincha Alta, off the coast of the Ica Region. The cities of Pisco, Ica, and Chincha Alta were the most severely affected, with Pisco experiencing widespread devastation. The earthquake caused more than 500 fatalities and injured over 1,300 people, leaving thousands homeless. Economic losses were estimated at more than $150 million USD (at the time of the event), accounting for extensive damage to homes, infrastructure, and cultural heritage sites. Secondary hazards included liquefaction in areas with soft soils, landslides in mountainous regions, and a small tsunami along the Peruvian coast.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2007 |
| Country | Peru |
| Region | South America |
| Event Name | Pisco 2007 |
| Local Date | 15/08/2007 |
| Local Time | 18:40:58 |
| Latitude (decimal degrees) | -13.67 |
| Longitude (decimal degrees) | -76.76 |
| Depth (km) | 40 |
| Mw | 7.9 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Reverse Fault |
| Tectonic region type | Subduction Interface |
| USGS event ID | usp000fjta |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 337-610  |
| Injured | 1042-2291 |
| Displaced population | ~100000 |
| Affected population | 32000-722643 |
| Affected units | 2574-13688  |
| Damaged units | 17000-230000  |
| Collapsed units | 33676-94000  |
| Economic losses | 139.1-600 M USD |
| Insured losses | 200 M USD  |
| Earthquake-triggered effects | Tsunami, Landslides, Liquefaction |