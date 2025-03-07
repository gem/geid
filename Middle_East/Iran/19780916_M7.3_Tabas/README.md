# 🌎 1978 M7.3 Tabas earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1978 M7.3 Tabas earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1978 Tabas earthquake` in Iran occurred on 16 September 1978 at approximately 19:05 local time. The epicenter was near the city of Tabas, in the South Khorasan Province, a region that endured extensive destruction. The earthquake had a moment magnitude of 7.4 and reached a maximum intensity of IX (MMI), signifying violent shaking and severe damage. It primarily devastated Tabas and the surrounding villages, with catastrophic destruction attributed to the traditional mud-brick construction. Tragically, an estimated 14800 to 25000 fatalities were reported, making it one of the deadliest earthquakes in Iran's history. Additionally, the disaster resulted in more than 6400 injuries. The earthquake caused economic losses estimated at over $11 million USD, although the true cost may have been higher due to the widespread devastation and the destruction of entire communities. Only one significant M5 aftershock occurred. The earthquake also triggered widespread landslides in the mountainous areas around the epicenter, further compounding the destruction. However, no liquefaction, tsunamis, or significant fires were reported. This disaster highlighted the extreme vulnerability of rural Iranian communities to seismic events.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1978 |
| Country | Iran |
| Region | Middle East |
| Event Name | Tabas |
| Local Date | 16/09/1978 |
| Local Time | 19:06:00 |
| Latitude (decimal degrees) | 33.37 |
| Longitude (decimal degrees) | 57.44 |
| Depth (km) | 33 |
| Mw | 7.3 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Thrust |
| Tectonic region type | Active Crustal |
| USGS event ID | usp0000wjx |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 14800-25000 |
| Injured | ~6400 |
| Displaced population | nan |
| Affected population | 40000-53994 |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | 15000 Buildings |
| Economic losses | 11-50 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |