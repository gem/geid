# 🌎 1990 M7.4 Manjil-Rudbar earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1990 M7.4 Manjil-Rudbar earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1990 Manjil–Rudbar earthquake` struck northern Iran on June 20, 1990, at 12:30 a.m. local time, with a moment magnitude (Mw) of 7.4 and a maximum intensity of IX on the Modified Mercalli Intensity scale. The earthquake's epicenter was near the town of Manjil, located in Gilan Province. This devastating event severely impacted the provinces of Gilan and Zanjan, with cities such as Rudbar, Manjil, and Lushan experiencing extensive destruction. The earthquake caused economic losses exceeding $7000 million USD and led to a tragic death toll of 13000–50000, with over 50000 injured. The disaster also triggered widespread landslides, worsening the devastation in the mountainous areas. However, no instances of liquefaction, tsunamis, or fires were reported. This earthquake remains one of the deadliest in Iran's history, underscoring the region's vulnerability to seismic risks.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1990 |
| Country | Iran |
| Region | Middle East |
| Event Name | Manjil-Rudbar |
| Local Date | 20/06/1990 |
| Local Time | 00:30:00 |
| Latitude (decimal degrees) | 36.96 |
| Longitude (decimal degrees) | 49.41 |
| Depth (km) | 18.5 |
| Mw | 7.4 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Strike slip |
| Tectonic region type | Active Crustal |
| USGS event ID | usp0004arq |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 0.65g, observed at location (36.92°N, 48.95°E), corresponding to Ab-Bar. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 13000-50000 |
| Injured | 50000-105000 |
| Displaced population | 105000-400000 |
| Affected population | 70000-500000 |
| Affected units | ~0  |
| Damaged units | 100000-196774 Buildings |
| Collapsed units | 100000-321486 Buildings |
| Economic losses | 7000-8000 M USD |
| Insured losses | 100-115 M USD |
| Earthquake-triggered effects | Landslides, Rockfall, Tsunami |