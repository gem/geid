# 🌎 2000 M5.87 Iceland earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2000 M5.87 Iceland earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2000 Iceland earthquakes`, a pair of magnitude 5.87 events, struck southern Iceland on June 17 and 21. The epicenters were located near the town of Selfoss. These powerful earthquakes caused significant damage to infrastructure, including roads, bridges, and buildings, particularly in the towns of Selfoss and Hveragerði. While there were no fatalities, numerous minor injuries were reported. Economic losses were substantial due to widespread property damage and disruptions to essential services. Although no tsunamis were generated, the earthquakes triggered numerous landslides and some localized liquefaction.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2000 |
| Country | Iceland |
| Region | Europe |
| Event Name | Iceland |
| Local Date | 17/06/2000 |
| Local Time | 15:40:41 |
| Latitude (decimal degrees) | 63.966 |
| Longitude (decimal degrees) | -20.487 |
| Depth (km) | 10 |
| Mw | 5.87 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Strike-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0009urh |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | nan |
| Injured | nan |
| Displaced population | ~36 |
| Affected population | ~108 |
| Affected units | nan |
| Damaged units | 11.0 Buildings |
| Collapsed units | 11.0 Buildings |
| Economic losses | 12-20 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |