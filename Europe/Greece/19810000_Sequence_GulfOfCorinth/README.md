# 🌎 1981 M6.7 GulfofCorinth earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1981 M6.7 GulfofCorinth earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

In early 1981, the eastern Gulf of Corinth in Greece was impacted by a series of three significant earthquakes, each with magnitudes exceeding 6.0 Ms, occurring within an 11-day period from January 24 to February 3. These seismic events, with epicenters located in proximity to the coastal regions of the Gulf, resulted in extensive damage across the Corinth-Athens corridor, with the most severely affected areas experiencing a Mercalli Intensity (MMI) of IX. Cities such as Corinth, Loutraki, and parts of Athens bore the brunt of the destruction. The magnitudes of the individual earthquakes ranged from 6.4 to 6.7, contributing to the collapse of approximately 8000 buildings. The earthquake sequence claimed around 22 lives, 400 injuries and inflicted substantial economic losses, estimated to exceed 812 million USD. Observations of liquefaction, landslides, and surface rupture were documented in several areas, although no tsunamis were reported in association with the events.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1981 |
| Country | Greece |
| Region | Europe |
| Event Name | GulfofCorinth 1981 |
| Local Date | 24/02/1981 |
| Local Time | 20:53:38 |
| Latitude (decimal degrees) | 38.222 |
| Longitude (decimal degrees) | 22.934 |
| Depth (km) | 33 |
| Mw | 6.7 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Normal |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0001ccb |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./19810224_M6.7_GulfofCorinth/4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./19810224_M6.7_GulfofCorinth/4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~22 |
| Injured | ~400 |
| Displaced population | nan |
| Affected population | ~80400 |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | 8000 Buildings |
| Economic losses | 812-900 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |