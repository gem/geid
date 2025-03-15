# 🌎 2012 M6.4 Ahar-Varzaghan earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2012 M6.4 Ahar-Varzaghan earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2012 East Azerbaijan earthquakes` in Iran occurred on August 11, 2012, with a moment magnitude of 6.4 and a maximum MMI of VII. The epicenter was located near Ahar and Varzaghan, approximately 60 km from Tabriz. The main shock struck at 16:53 local time and was followed by a 6.2 magnitude aftershock. The most severely impacted areas included the cities of Ahar, Varzaghan, and nearby villages. The earthquakes led to over 250 fatalities, more than 1380 injuries, and widespread displacement. Economic losses exceeded 500 million USD, primarily due to structural damage. Landslides were observed, but there were no reports of liquefaction, tsunamis, or fires. Aftershocks continued to affect the region in the following days.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2012 |
| Country | Iran |
| Region | Middle East |
| Event Name | Ahar-Varzaghan |
| Local Date | 11/08/2012 |
| Local Time | 16:53:00 |
| Latitude (decimal degrees) | 38.52 |
| Longitude (decimal degrees) | 46.86 |
| Depth (km) | 11 |
| Mw | 6.4 |
| Max Intensity (MMI) | VII |
| Fault mechanism | Strike slip |
| Tectonic region type | Active Crustal |
| USGS event ID | usp000jq5p |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./20120811_M6.4_Ahar-Varzaghan/4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./20120811_M6.4_Ahar-Varzaghan/4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 253-330 |
| Injured | 1380-26000 |
| Displaced population | 30000-36000 |
| Affected population | 59540-250000 |
| Affected units | nan |
| Damaged units | 11908-72000 Buildings |
| Collapsed units | 5329-6000  |
| Economic losses | 500-599 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Rockfall, Landslides |