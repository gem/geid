# 🌎 2010 M7 Haiti earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2010 M7 Haiti earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2010 Haiti earthquake` struck on January 12, 2010, with a magnitude of 7.0 Mw at 16:53 local time. The epicenter was located near Léogâne, approximately 25 kilometers west of the capital city, Port-au-Prince. The earthquake caused widespread and severe destruction, particularly affecting the capital and its surrounding areas, including Carrefour and Jacmel. The maximum reported intensity of the earthquake was IX on the Modified Mercalli Intensity (MMI) scale, reflecting the intense shaking experienced across the region. The event resulted in a catastrophic loss of life, with fatalities estimated between 158679 and 316000, and over 300000 individuals injured. Economic losses were substantial, with an estimated range of 7000 to 8000 million USD. The earthquake also triggered significant secondary hazards, including liquefaction and landslides. While no tsunamis were reported, fires broke out in several locations due to infrastructure damage. Numerous aftershocks, including a notable magnitude 6.1 Mw tremor, followed the main event, further compounding the devastation.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2010 |
| Country | Haiti |
| Region | Caribbean Central America |
| Event Name | Haiti |
| Local Date | 01/12/2010 |
| Local Time | 16:53:10 |
| Latitude (decimal degrees) | 18.443 |
| Longitude (decimal degrees) | -72.571 |
| Depth (km) | 13 |
| Mw | 7 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Strike slip |
| Tectonic region type | Active Shallow Crustal |
| USGS event ID | usp000h60h |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 158679-316000 |
| Injured | ~300000 |
| Displaced population | 1269110-1800000 |
| Affected population | 3000000-3700000 |
| Affected units | nan |
| Damaged units | 285677-317289 |
| Collapsed units | 105000-188383 |
| Economic losses | 7000-8000 M USD |
| Insured losses | 200 M USD |
| Earthquake-triggered effects | Liquefaction |