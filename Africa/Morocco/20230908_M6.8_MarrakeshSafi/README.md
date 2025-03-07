# 🌎 2023 M6.8 Marrakesh–Safi earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2023 M6.8 Marrakesh–Safi earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The 2023 Marrakesh–Safi earthquake struck Morocco on September 8, 2023, at 11:11 PM local time. The earthquake had a moment magnitude of 6.8 and reached a maximum intensity of VIII on the Modified Mercalli Intensity scale. The epicenter was located near the town of Al Haouz, about 70 kilometers southwest of Marrakesh, in the High Atlas Mountains. The earthquake primarily affected the regions of Marrakesh, Al Haouz, and Taroudant, with significant damage in the city of Marrakesh. The event caused widespread devastation, resulting in approximately 2900 fatalities and over 5500 injuries. In addition to the primary shaking, there were reports of landslides in the mountainous areas, though no tsunamis or large-scale fires were observed. Liquefaction was not prominently reported, but the extensive destruction of buildings raised concerns over the resilience of the region’s infrastructure.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2023 |
| Country | Morocco |
| Region | Africa |
| Event Name | MarrakeshSafi 2023 |
| Local Date | 08/09/2023 |
| Local Time | 23:11:01 |
| Latitude (decimal degrees) | 31.0549 |
| Longitude (decimal degrees) | -8.3887 |
| Depth (km) | 19 |
| Mw | 6.8 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Oblique-Slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | us7000kufc |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="300">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_all.png" height="300">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~2946 |
| Injured | ~5674 |
| Displaced population | nan |
| Affected population | nan |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | nan |
| Economic losses | nan |
| Insured losses | nan |
| Earthquake-triggered effects | Slide |