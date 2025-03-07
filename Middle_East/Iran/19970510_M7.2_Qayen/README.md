# 🌎 1997 M7.2 Qayen earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1997 M7.2 Qayen earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1997 Qayen earthquake`, also known as the Ardakul earthquake, struck northeastern Iran on May 10, 1997, at 12:27 PM local time. It had a moment magnitude of 7.2 and a maximum Modified Mercalli Intensity (MMI) of IX. The epicenter was located near the city of Qayen in the South Khorasan province. The earthquake primarily affected rural areas, including the cities of Qayen and Birjand, causing widespread destruction. It resulted in over 1500 fatalities, more than 2300 injuries, and left tens of thousands homeless. Economic losses were estimated at over $100 million USD. 155 aftershocks occurred and caused further destruction. Liquefaction and landslides were observed in the affected areas, further exacerbating the damage, while no tsunamis or fires were reported. The earthquake highlighted the region's vulnerability to seismic hazards and the need for improved building resilience.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1997 |
| Country | Iran |
| Region | Middle East |
| Event Name | Qayen |
| Local Date | 10/05/1997 |
| Local Time | 12:27:00 |
| Latitude (decimal degrees) | 33.82 |
| Longitude (decimal degrees) | 59.8 |
| Depth (km) | 10 |
| Mw | 7.2 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Strike Slip |
| Tectonic region type | Active Crustal |
| USGS event ID | usp000820p |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 1500-1728 |
| Injured | 2300-2600 |
| Displaced population | nan |
| Affected population | 72000-200166 |
| Affected units | nan |
| Damaged units | 5474-7000 Buildings |
| Collapsed units | 10533-15000 Buildings |
| Economic losses | 100-500 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides |