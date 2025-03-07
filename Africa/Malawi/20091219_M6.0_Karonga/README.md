# 🌎 2009 M6.0 Karonga earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2009 M6.0 Karonga earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2009 Karonga earthquakes` in Malawi struck on December 19, 2009, at 15:02 local time. The epicenter was located near the town of Karonga, in the northern part of the country, close to the border with Tanzania. The earthquake, which had a magnitude of 6.0, was most strongly felt in the northern regions of Malawi, particularly in the cities of Karonga, Mzuzu, and surrounding areas. The quake caused significant damage to buildings and infrastructure, resulting in the tragic loss of at least 3 lives and more than 250 injuries. While no tsunamis or major fires were reported, the earthquake triggered landslides in the affected regions. Liquefaction was also observed in some areas, which contributed to further damage.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2009 |
| Country | Malawi |
| Region | Africa |
| Event Name | Karonga |
| Local Date | 19/12/2009 |
| Local Time | 15:02:00 |
| Latitude (decimal degrees) | -10.108 |
| Longitude (decimal degrees) | 33.818 |
| Depth (km) | 6 |
| Mw | 6 |
| Max Intensity (MMI) | VII |
| Fault mechanism | Dip Slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp000h56x |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~3 |
| Injured | ~250 |
| Displaced population | nan |
| Affected population | nan |
| Affected units | nan |
| Damaged units | ~3565 |
| Collapsed units | ~1111 |
| Economic losses | nan |
| Insured losses | nan |
| Earthquake-triggered effects | nan |