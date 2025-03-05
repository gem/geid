# 🌎 1989-03-10 M6.2 Salima earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1989-03-10 M6.2 Salima earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1989 Salima earthquake` struck Malawi at 23:49 local time on March 10, 1989, with its epicenter located near the town of Salima, situated on the shores of Lake Malawi. The earthquake primarily affected the central and northern regions of the country, including areas such as Salima, Kasungu, and Lilongwe, leading to significant damage to infrastructure and homes. The reported fatalities were around 9, with approximately 100 people injured and thousands displaced. Economic losses from the event were estimated at around $28 million USD (at the time of the event), primarily due to damage to buildings, roads, and public infrastructure. Although the earthquake caused widespread destruction, there were no reports of tsunamis, fires, or significant liquefaction. However, landslides were observed in some areas, especially in regions with hilly terrain, contributing to the overall destruction caused by the quake.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1989 |
| Country | Malawi |
| Region | Africa |
| Event Name | Salima |
| Local Date | 03/10/1989 |
| Local Time | 23:49:47 |
| Latitude (decimal degrees) | -13.66 |
| Longitude (decimal degrees) | 34.496 |
| Depth (km) | 28.2 |
| Mw | 6.27 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Dip-slip |
| Tectonic region type | Active Shallow Crust / Stable Continental Crust |
| USGS event ID | N/A |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~9 |
| Injured | ~100 |
| Displaced population | ~50000 |
| Affected population | ~50100 |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | nan |
| Economic losses | 28 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |