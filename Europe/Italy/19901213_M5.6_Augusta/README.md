# 🌎 1990 M5.6 Augusta earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1990 M5.6 Augusta earthquake in southern Italy.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1990 Carlentini earthquake` struck on December 13, 1990, at 01:24 local time, shaking southeastern Sicily with a magnitude of 5.6. The event reached a maximum intensity of VIII on the Modified Mercalli Intensity (MMI) scale, causing widespread destruction. The epicenter was located approximately 20 kilometers east-northeast of Augusta, near the town of Carlentini, which, along with Augusta, bore the brunt of the disaster. The earthquake claimed the lives of approximately 18 people, left over 200 injured. The economic losses exceeded $500 million USD, highlighting the scale of the destruction. There were cases of landslides and liquefaction, but no reports of tsunamis or fires.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1990 |
| Country | Italy |
| Region | Europe |
| Event Name | Augusta 1990 |
| Local Date | 13/12/1990 |
| Local Time | 01:24:25 |
| Latitude (decimal degrees) | 37.3 |
| Longitude (decimal degrees) | 15.438 |
| Depth (km) | 11.1 |
| Mw | 5.6 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Strike-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0004j1w |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 0.25 g, observed at Catania. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 17-19 |
| Injured | 200-300 |
| Displaced population | 13200-15000 |
| Affected population | nan |
| Affected units | nan |
| Damaged units | 6103-7104 Buildings |
| Collapsed units | nan |
| Economic losses | 500 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides, liquefaction |