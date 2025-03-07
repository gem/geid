# 🌎 2008 M6.32 Iceland earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2008 M6.32 Iceland earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2008 Iceland earthquake`, a magnitude 6.32 event, struck southwestern Iceland on May 29, 2008, at 15:46 local time. The epicenter was located between the towns of Hveragerði and Selfoss. The earthquake was widely felt across Iceland, causing significant damage to infrastructure, including roads, bridges, and buildings, particularly in the affected areas. While there were no fatalities, numerous minor injuries were reported. Economic losses were substantial due to widespread property damage and disruptions to essential services. Although no tsunamis were generated, the earthquake triggered numerous landslides and some localized liquefaction.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2008 |
| Country | Iceland |
| Region | Europe |
| Event Name | Iceland 2008 |
| Local Date | 29/05/2008 |
| Local Time | 15:46:00 |
| Latitude (decimal degrees) | 64.005 |
| Longitude (decimal degrees) | -21.013 |
| Depth (km) | 9 |
| Mw | 6.32 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Strike-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp000g826 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 0.88g, observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | nan |
| Injured | 0-30 |
| Displaced population | nan |
| Affected population | nan |
| Affected units | nan |
| Damaged units | 30 Buildings |
| Collapsed units | nan |
| Economic losses | nan |
| Insured losses | nan |
| Earthquake-triggered effects | nan |