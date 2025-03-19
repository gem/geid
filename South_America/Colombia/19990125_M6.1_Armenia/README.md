# 🌎 1999 M6.1 Armenia earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1999 M6.1 Armenia earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1999 Armenia, Colombia earthquake` occurred on January 25, 1999, at 13:19 local time with a moment magnitude of 6.1 Mw. The Modified Mercalli Intensity (MMI) reached IX in the most affected areas, indicating widespread structural damage. The epicenter was located approximately 40 kilometers south-west of Ibagué, in the Coffee-Growers Axis region, affecting Armenia, the capital of Quindío department, as well as surrounding municipalities including Córdoba, Pijao, Calarcá, and La Tebaida in Quindío, along with regions in Risaralda and Valle del Cauca. The earthquake caused significant destruction, particularly in Armenia, where many buildings, including multi-story apartment blocks and government offices, collapsed, resulting in severe economic losses. The coffee industry, a vital economic activity in the region, was heavily impacted, with approximately 8000 coffee farms destroyed. More than 1000 fatalities were reported, along with over 4000 injuries. Among the victims were firefighters and police officers, many of whom were killed when their facilities collapsed. The earthquake triggered landslides that blocked roads and isolated several towns, further complicating rescue efforts. Liquefaction and tsunamis were not observed, but widespread landslides and fires caused additional damage. The total economic losses were estimated at more than 1500 million USD, significantly affecting the local economy. The region experienced aftershocks, with the most significant occurring hours after the main earthquake, and additional aftershocks continued for several months, including notable ones on January 25 (M5.5), January 29 (M4.2), and January 31 (M3.5). These aftershocks caused continued panic among residents and disrupted recovery efforts.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1999 |
| Country | Colombia |
| Region | South America |
| Event Name | Armenia 1999 |
| Local Date | 25/01/1999 |
| Local Time | 13:19:00 |
| Latitude (decimal degrees) | 4.432 |
| Longitude (decimal degrees) | -75.703 |
| Depth (km) | 15 |
| Mw | 6.1 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Strike-Slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp00091q3 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 1000-2000 |
| Injured | 4000-10000 |
| Displaced population | 67539-250000 |
| Affected population | 200000-1534500 |
| Affected units | 45019-90474  |
| Damaged units | 20000-61859  |
| Collapsed units | 15000-35972  |
| Economic losses | 1500-2630 M USD |
| Insured losses | 100-150 M USD |
| Earthquake-triggered effects | Landslides |