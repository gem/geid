# 🌎 2004 M6.3 AlHoceima earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2004 M6.3 AlHoceima earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance

The `2004 Al Hoceima earthquake`in Morocco occurred on May 24, 2004, at 2:27 AM local time. With a magnitude of 6.3 and violent (IX) shaking, the earthquake's epicenter was located near the town of Al Hoceima in the Rif Mountains, in the northern part of the country. The most affected regions included Al Hoceima and the surrounding cities of Imzouren and Boudnib, which experienced significant damage. The earthquake caused severe destruction, resulting in over 628 fatalities and injuring more than 900 people. The economic losses were estimated at over 300 million USD (at the time of the event). The earthquake also triggered various secondary hazards, particularly landslides and rockfalls, which exacerbated the destruction. These events were reported between Ajdir and Beni Abdallah. Although the earthquake caused widespread damage, no tsunamis, fires, or liquefaction events were observed. The 2:27 AM local time event is considered the main shock of the sequence, followed by hundreds of aftershocks. Three notable aftershocks occurred on February 26, March 2, and March 7, with magnitudes of 5.0. These aftershocks caused additional collapses of already damaged houses, resulting in at least three more deaths (Cherkaoui, 2005).

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2004 |
| Country | Morocco |
| Region | Africa |
| Event Name | AlHoceima 2004 |
| Local Date | 24/02/2004 |
| Local Time | 02:27:47 |
| Latitude (decimal degrees) | 35.235 |
| Longitude (decimal degrees) | 3.963 |
| Depth (km) | 12.2 |
| Mw | 6.4 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Strike-slip; left-lateral |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp000cmxe |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 0.51g, observed near Imzourene. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.
<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 628-631 |
| Injured | ~926 |
| Displaced population | 12539-15230 |
| Affected population | nan |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | ~2539  |
| Economic losses | 300-400 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides |
