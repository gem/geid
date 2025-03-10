# 🌎 2018 M5.5 Osaka earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2018 M5.5 Osaka earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2018 Osaka earthquake` occurred at 07:58 local time on June 18, 2018, with a moment magnitude of Mw 5.5. The epicenter was located near Amagasaki, Osaka Prefecture, and the earthquake had a profound impact on the surrounding regions, including Osaka, Kyoto, and Kobe. The Modified Mercalli Intensity (MMI) in some areas reached VIII, resulting in significant damage to infrastructure and buildings. The event led to approximately 5 fatalities and more than 400 injuries. Economic losses were considerable, with estimates ranging from 3250 to 7000 million USD, primarily due to damage to buildings, roads, and utilities. While no tsunamis were generated, the earthquake triggered 1 landslide and caused 8 fire incidents. Following the mainshock, a series of aftershocks were recorded. The earthquake also activated Japan's national earthquake warning system, providing a brief 3.2-second warning to cities such as Kyoto and Osaka.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2018 |
| Country | Japan |
| Region | East Asia |
| Event Name | Osaka 2018 |
| Local Date | 18/06/2018 |
| Local Time | 07:58:35 |
| Latitude (decimal degrees) | 34.825 |
| Longitude (decimal degrees) | 135.639 |
| Depth (km) | 10.3 |
| Mw | 5.5 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Complex (strike-slip, reverse) |
| Tectonic region type | Active Shallow Crustal |
| USGS event ID | us1000eu1c |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~5 |
| Injured | 417-421 |
| Displaced population | 267-2700 |
| Affected population | nan |
| Affected units | nan |
| Damaged units | 6766-8086  |
| Collapsed units | ~3  |
| Economic losses | 3250-7000 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslide, Fire |