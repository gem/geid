# 🌎 1995 M6.5 Aigio earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1995 M6.5 Aigio earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1995 Aigio earthquake`, a devastating seismic event, struck on June 15, 1995, at 03:15 local time, with a magnitude of 6.5 and a peak intensity of VIII on the Modified Mercalli Intensity (MMI) scale. Its epicenter was pinpointed in the Gulf of Corinth, near the town of Aigio, Greece. The quake inflicted severe damage on the cities of Aigio, Patras, and nearby regions, causing widespread structural devastation. Economic losses were immense, estimated at $660 million USD, and the disaster claimed 26 lives, leaving over 60 injured. The earthquake triggered liquefaction and landslides, further compounding the destruction. Additionally, a minor tsunami, with a recorded height of approximately 30 cm, was observed along the coast, adding to the calamity’s impact.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1995 |
| Country | Greece |
| Region | Europe |
| Event Name | Aigio 1995 |
| Local Date | 15/06/1995 |
| Local Time | 03:15:48 |
| Latitude (decimal degrees) | 38.401 |
| Longitude (decimal degrees) | 22.283 |
| Depth (km) | 14.2 |
| Mw | 6.5 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Normal |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0006z34 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~26 |
| Injured | 60-200 |
| Displaced population | 2100-6300 |
| Affected population | ~13900 |
| Affected units | 3400 Buildings |
| Damaged units | 2300 Buildings |
| Collapsed units | 2000 Buildings |
| Economic losses | 422.7-660 M USD |
| Insured losses | 0.2 M USD |
| Earthquake-triggered effects | nan |