# 🌎 1992 M5.3 Roermond earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1992 M5.3 Roermond earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1992 Roermond earthquake` occurred on April 13, 1992, at 3:20 local time, with a moment magnitude (Mw) of 5.3 and a maximum intensity of VIII on the Modified Mercalli Intensity (MMI) scale. The earthquake's epicenter was located near Roermond in the southeastern Netherlands. Roermond and nearby areas in the Dutch Limburg province, along with parts of neighboring Germany, were the most affected regions. Economic losses exceeded 50 million USD, mainly due to extensive damage to buildings and infrastructure. Fortunately, no fatalities were reported, though around 20 people sustained injuries. Liquefaction was observed in some areas close to the epicenter; however, there were no reports of landslides, tsunamis, or fires. The earthquake was preceded by a series of minor foreshocks and followed by aftershocks, the largest of which had a magnitude of 3.9. This event remains one of the most significant seismic occurrences in the Netherlands' history.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1992 |
| Country | Netherlands |
| Region | Europe |
| Event Name | Roermond 1992 |
| Local Date | 13/04/1992 |
| Local Time | 03:20:00 |
| Latitude (decimal degrees) | 51.153 |
| Longitude (decimal degrees) | 5.798 |
| Depth (km) | 21.2 |
| Mw | 5.3 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Normal |
| Tectonic region type | Stable Continental |
| USGS event ID | usp00055q3 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | nan |
| Injured | 20-45 |
| Displaced population | nan |
| Affected population | ~1500 |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | nan |
| Economic losses | 50-100 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |