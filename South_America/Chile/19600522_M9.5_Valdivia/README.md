# 🌎 1960 M9.5 Valdivia earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1960 M9.5 Valdivia earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1960 Valdivia earthquake`, the most powerful earthquake ever recorded, struck southern Chile on May 22, 1960, at 15:11 local time, with an astounding moment magnitude of Mw 9.5. The epicenter was near Lumaco, approximately 570 kilometers south of Santiago. Valdivia and the surrounding regions, including the Arauco Peninsula, endured the highest Modified Mercalli Intensity (MMI) of IX. The megaquake was preceded by two significant foreshocks on May 21 in the Arauco Peninsula, measuring Mw 8.1 and 7.8. The earthquake unleashed devastating tsunamis that not only battered the Chilean coast with waves towering up to 25 meters but also reached far-flung shores in Hawaii, Japan, and beyond, leading to widespread fatalities and destruction. The seismic event triggered a cascade of secondary hazards, including landslides, liquefaction, a volcanic eruption at Cordón Caulle, and seiches on Panguipulli Lake and others as far as Argentina. Economic losses in Chile were estimated to exceed $400 million USD at the time, while fatalities ranged from 1000 to 6000, with over 2 million people displaced and more than 1740 injuries reported Aftershocks, including a major Mw 7.9 tremor in Aysén on June 6, highlighted the extensive tectonic realignments following the primary quake. 


| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1960 |
| Country | Chile |
| Region | South America |
| Event Name | Valdivia 1960 |
| Local Date | 22/05/1960 |
| Local Time | 15:11:14 |
| Latitude (decimal degrees) | -38.143 |
| Longitude (decimal degrees) | -73.407 |
| Depth (km) | 25 |
| Mw | 9.5 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Strike slip |
| Tectonic region type | Subduction |
| USGS event ID | official19600522191120_30 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 1000-6000 |
| Injured | 1743-3000 |
| Displaced population | ~2000000 |
| Affected population | 2000000-2500000  |
| Affected units | nan |
| Damaged units | 58622-450000  |
| Collapsed units | ~72  |
| Economic losses | 400-1000 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Tsunami, Volcano, Landslides, Flood |