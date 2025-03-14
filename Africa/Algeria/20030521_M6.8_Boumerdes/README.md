# 🌎 2003 M6.8 Boumerdes earthquake

[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2003 M6.8 Boumerdes earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance

The `2003 Boumerdes earthquake` struck northern Algeria on May 21, 2003, at approximately 19:44 local time, with an estimated magnitude of Mw6.8 and violent (IX) to extreme (X) shaking. The earthquake had its epicenter near the town of Zemmouri, approximately 50 km east of Algiers. The Boumerdès Province (Thénia, Zemmouri, Bourmerdès) experienced heavy damage. Many buildings built in the early twentieth century during the colonial rule suffered heavy damage in the Belcourt, Bab-El-Oued and El-Casbah areas in Algiers Province. The earthquake caused devastating economic losses, estimated at around $5000 million USD (at the time of the event), and led to the tragic loss of at least 2266 lives, with over 10000 injuries reported. The Boumerdes 2003 event at 19:44 local time is considered a main shock, which was followed by several aftershocks. Refer to Kherroubi et. al. 2017 for more information on aftershocks. Liquefaction was widely observed, particularly along the coastal areas, contributing to infrastructure damage, while landslides exacerbated the destruction in hilly regions. A minor tsunami was also triggered, reaching the shores of the western Mediterranean, and damaged some boats but no significant fires were reported in the aftermath. This event remains one of the most impactful earthquakes in the region's recent history.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2003 |
| Country | Algeria |
| Region | Africa |
| Event Name | Boumerdes 2003 |
| Local Date | 21/05/2003 |
| Local Time | 19:44:21 |
| Latitude (decimal degrees) | 36.91 |
| Longitude (decimal degrees) | 3.71 |
| Depth (km) | 12 |
| Mw | 6.8 |
| Max Intensity (MMI) | IX-X |
| Fault mechanism | Dip-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp000bxpg |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 0.58g, observed at 20km from the epicenter. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<p align="center">
  <img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
  <img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">
</p>

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 2266-2287 |
| Injured | 10261-11000 |
| Displaced population | ~200000 |
| Affected population | ~210261 |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | nan |
| Economic losses | 5000 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Tsunami |
