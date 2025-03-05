# 🌎 2023-08-17 M6.1 El Calvario earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2023-08-17 M6.1 El Calvario earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2023 El Calvario earthquake` struck near El Calvario, Meta, on August 17, 2023, at 12:04 local time, with a magnitude 6.1 earthquake and a superficial depth of less than 30 kilometers. The earthquake was strongly felt in nearby regions, significantly impacting El Calvario and its surrounding areas. The Modified Mercalli Intensity (MMI) in the epicentral zone reached VII, reflecting very strong shaking. Notably, no instances of liquefaction, landslides, tsunamis, or fires were observed during this event. The earthquake was preceded by minor foreshocks and followed by multiple aftershocks, with the strongest measuring 4.7 in magnitude, intensifying concerns among the affected communities.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2023 |
| Country | Colombia |
| Region | South America |
| Event Name | El Calvario |
| Local Date | 17/08/2023 |
| Local Time | 12:04:57 |
| Latitude (decimal degrees) | 4.4177 |
| Longitude (decimal degrees) | -73.5111 |
| Depth (km) | 10 |
| Mw | 6.1 |
| Max Intensity (MMI) | VII |
| Fault mechanism | Strike-slip |
| Tectonic region type | Active shallow |
| USGS event ID | us7000kp2i |

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
| Injured | ~0 |
| Displaced population | nan |
| Affected population | ~0 |
| Affected units | nan |
| Damaged units | ~82 |
| Collapsed units | N/A |
| Economic losses | nan |
| Insured losses | nan |
| Earthquake-triggered effects | nan |