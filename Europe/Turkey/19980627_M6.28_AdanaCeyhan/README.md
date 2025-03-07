# 🌎 1998 M6.28 AdanaCeyhan earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1998 M6.28 AdanaCeyhan earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1998 Adana–Ceyhan earthquake` struck at 16:55 local time on June 27, 1998. This magnitude 6.28 event, centered near the cities of Adana and Ceyhan, caused widespread damage in southern Turkey. The earthquake resulted in significant casualties, with around 145 fatalities and over 1500 injuries reported. Substantial economic losses, estimated at over 550 million USD, were incurred. The ground shaking was intense, reaching a maximum intensity of VIII on the Modified Mercalli Intensity scale. While no tsunamis were generated, the earthquake triggered numerous landslides and some localized liquefaction.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1998 |
| Country | Turkey |
| Region | Europe |
| Event Name | AdanaCeyhan 1998 |
| Local Date | 27/06/1998 |
| Local Time | 16:55:52 |
| Latitude (decimal degrees) | 36.878 |
| Longitude (decimal degrees) | 35.307 |
| Depth (km) | 33 |
| Mw | 6.28 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Strike-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0008qkc |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.
<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~145 |
| Injured | 1500-1600 |
| Displaced population | ~88000 |
| Affected population | ~1500000 |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | 1700 Buildings |
| Economic losses | 550-1300 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |