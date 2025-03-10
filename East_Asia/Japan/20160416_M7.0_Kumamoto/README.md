# 🌎 2016 M7 Kumamoto earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2016 M7 Kumamoto earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2016 Kumamoto earthquake`, which struck on April 16, 2016, had a moment magnitude of 7. Occurring at 01:25 local time, its epicenter was located near the city of Kumamoto, situated on the island of Kyushu, Japan. The earthquake caused significant devastation across the Kumamoto Prefecture and extended to other regions of Kyushu, including Oita and Fukuoka. The event was classified with a maximum intensity (MMI) of IX in the hardest-hit areas, particularly in Kumamoto City. The economic toll of the disaster surpassed $20000 million USD, resulting in severe damage to critical infrastructure, residential buildings, and other properties. Tragically, the earthquake led to over 50 fatalities and left more than 1500 individuals injured. Alongside the destructive ground shaking, liquefaction and landslides were observed, and fires broke out in several locations. Fortunately, no tsunamis were triggered, as the earthquake's epicenter was inland.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2016 |
| Country | Japan |
| Region | East Asia |
| Event Name | Kumamoto 2016 |
| Local Date | 16/04/2016 |
| Local Time | 01:25:06 |
| Latitude (decimal degrees) | 32.7906 |
| Longitude (decimal degrees) | 130.7543 |
| Depth (km) | 10 |
| Mw | 7 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Strike slip |
| Tectonic region type | Active Shallow Crustal |
| USGS event ID | us20005iis |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 50-228 |
| Injured | 1500-2753 |
| Displaced population | 23985-196000 |
| Affected population | ~272763 |
| Affected units | ~198636  |
| Damaged units | ~189939  |
| Collapsed units | ~8697  |
| Economic losses | 20000-22580 M USD |
| Insured losses | 5000-5645 M USD |
| Earthquake-triggered effects | Landslides, Debris flows, Cliff failures |