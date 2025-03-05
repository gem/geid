# 🌎 1999 M7.6 Izmit earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1999 M7.6 Izmit earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The devastating `1999 İzmit earthquake`, a magnitude 7.6 event, struck northwestern Turkey on August 17, 1999, at 3:01 local time. The epicenter was located near the city of İzmit, along the North Anatolian Fault. The maximum Mercalli intensity was X.This powerful earthquake caused widespread destruction in the region, affecting major cities like İzmit, Gölcük, and Yalova. The death toll was tragically high, with estimates ranging from 17127 to 18373 fatalities. It resulted in over 43900 injuries. Economic losses were substantial, exceeding 20000 million USD. The earthquake triggered numerous landslides, and liquefaction was observed in several areas.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1999 |
| Country | Turkey |
| Region | Europe |
| Event Name | Izmit |
| Local Date | 17/08/1999 |
| Local Time | 03:01:39 |
| Latitude (decimal degrees) | 40.748 |
| Longitude (decimal degrees) | 29.864 |
| Depth (km) | 17 |
| Mw | 7.6 |
| Max Intensity (MMI) | X |
| Fault mechanism | Strike-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0009d4z |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 17118-18373 |
| Injured | 43953-50000 |
| Displaced population | ~600000 |
| Affected population | ~1358953 |
| Affected units | 241000 Buildings |
| Damaged units | 73342-108000 Buildings |
| Collapsed units | 16400 Buildings |
| Economic losses | 20000-30000 M USD |
| Insured losses | 2000 M USD |
| Earthquake-triggered effects | nan |