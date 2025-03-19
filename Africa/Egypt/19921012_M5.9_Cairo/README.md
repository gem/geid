# 🌎 1992 M5.9 Cairo earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1992 M5.9 Cairo earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance

The `1992 Cairo earthquake` struck Egypt on October 12, 1992, at at 13:08 local time, with an estimated magnitude of Mw 5.9 and severe shaking measured at intensity VIII. The earthquake's epicenter was located near Dahshur, approximately 35 kilometers south of Cairo. The quake caused significant damage in Cairo and the surrounding areas, particularly in neighborhoods such as Helwan and rural villages near the epicenter. It resulted in at least 545 fatalities, injured over 6500 people, and left many homeless. Economic losses were estimated at more than $1200 million USD (at the time of the event). The earthquake was followed by several aftershocks, as summarized in studies by Badawy and Mónus (1995). The event caused widespread building collapses and structural damage. Liquefaction was reported in areas near the epicenter. However, there were no reports of landslides, tsunamis, or fires associated with the earthquake.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1992 |
| Country | Egypt |
| Region | Africa |
| Event Name | Cairo 1992 |
| Local Date | 12/10/1992 |
| Local Time | 13:09:55 |
| Latitude (decimal degrees) | 29.778 |
| Longitude (decimal degrees) | 31.144 |
| Depth (km) | 21.5 |
| Mw | 5.9 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Dip-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0005f89 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 0.232g, observed near Cairo. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 545-561 |
| Injured | 6512-12199 |
| Displaced population | 25020-50000 |
| Affected population | 57700-92649 |
| Affected units | nan |
| Damaged units | 8300-9350  |
| Collapsed units | nan |
| Economic losses | 1200-4000 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Liquefaction |
