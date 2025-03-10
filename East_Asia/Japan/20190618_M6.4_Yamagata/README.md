# 🌎 2019 M6.4 Yamagata earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2019 M6.4 Yamagata earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2019 Yamagata earthquake` occurred on 18 June 2019 at 22:22 local time, with a moment magnitude of Mw 6.4. The earthquake's epicenter was located near Yamagata Prefecture, Japan. The seismic event resulted in widespread shaking, with the maximum intensity reaching MMI VII in several regions, particularly affecting Yamagata City and surrounding areas. The earthquake led to significant damage, including over 28 injuries. While liquefaction, landslides, and fires were not observed, the event did produce a small tsunami, with recorded waves of up to 10 cm. The economic impact was substantial, though specific loss figures remain unavailable. Notably, there were no damaging aftershocks, and no significant foreshocks were reported prior to the earthquake.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2019 |
| Country | Japan |
| Region | East Asia |
| Event Name | Yamagata 2019 |
| Local Date | 18/06/2019 |
| Local Time | 22:22:20 |
| Latitude (decimal degrees) | 38.639 |
| Longitude (decimal degrees) | 139.477 |
| Depth (km) | 12 |
| Mw | 6.4 |
| Max Intensity (MMI) | VII |
| Fault mechanism | Reverse |
| Tectonic region type | Active Shallow Crustal |
| USGS event ID | us600042fx |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~0 |
| Injured | 28-43 |
| Displaced population | 45-840 |
| Affected population | ~432 |
| Affected units | nan |
| Damaged units | 144-1608 Buildings |
| Collapsed units | nan |
| Economic losses | nan |
| Insured losses | nan |
| Earthquake-triggered effects | Tsunami |