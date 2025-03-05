# 🌎 2021 M7.1 Guerrero earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2021 M7.1 Guerrero earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The powerful `2021 Guerrero earthquake` struck near the city of Acapulco in Guerrero state, Mexico, on September 7th at 20:47 local time, with a moment magnitude of Mw7.1. This event exhibited a severe intensity of VIII on the Modified Mercalli Intensity (MMI) scale, with the epicenter located close to Acapulco, resulting in significant impacts on the city and its surrounding areas. The earthquake caused economic losses exceeding 0.2 million USD, with widespread damage to infrastructure, buildings, and businesses across the region. Tragically, the disaster claimed more than 3 lives, and over 23 individuals sustained injuries. Geophysical effects included landslides that obstructed roads in mountainous regions and liquefaction observed in some coastal areas. While there were no confirmed reports of tsunamis or fires, the earthquake was preceded by minor foreshocks and followed by a series of aftershocks, compounding the challenges faced by affected communities during their recovery efforts.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2021 |
| Country | Mexico |
| Region | North America |
| Event Name | Guerrero 2021 |
| Local Date | 07/09/2020 |
| Local Time | 20:47:00 |
| Latitude (decimal degrees) | 16.82 |
| Longitude (decimal degrees) | -99.78 |
| Depth (km) | 10 |
| Mw | 7.1 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Reverse |
| Tectonic region type | Subduction Interface |
| USGS event ID | us7000f93v |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 3-14 |
| Injured | 20-30 |
| Displaced population | ~15000 |
| Affected population | ~1600000 |
| Affected units | nan |
| Damaged units | 7317-12963 |
| Collapsed units | nan |
| Economic losses | 0.20-1.1 M USD |
| Insured losses | 0.20 M USD |
| Earthquake-triggered effects | Landslide |