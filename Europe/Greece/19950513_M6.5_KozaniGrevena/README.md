# 🌎 1995 M6.5 KozaniGrevena earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1995 M6.5 KozaniGrevena earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1995 Kozani-Grevena earthquake` struck on May 13, 1995, at 11:47 local time, with a magnitude of 6.5 (Mw) and a maximum Mercalli Intensity (MMI) of VIII. Its epicenter was located near Kozani in northern Greece. The earthquake primarily impacted the areas of Kozani and Grevena, causing extensive damage in nearby villages. Economic losses were significant, estimated at approximately $450 million USD, due to widespread destruction of buildings and infrastructure. Despite the earthquake's strength, the human toll was remarkably low, with only 26 fatalities and around 25 reported injuries. Notably, there were no instances of liquefaction, tsunamis, or major landslides, underscoring the event's relatively limited secondary impacts. This earthquake remains a significant example of a high-magnitude event with minimal loss of life.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1995 |
| Country | Greece |
| Region | Europe |
| Event Name | KozaniGrevena 1995 |
| Local Date | 13/05/1995 |
| Local Time | 11:47:12 |
| Latitude (decimal degrees) | 40.149 |
| Longitude (decimal degrees) | 21.695 |
| Depth (km) | 14 |
| Mw | 6.5 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Normal |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0006x90 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 0-26 |
| Injured | 25-60 |
| Displaced population | nan |
| Affected population | ~15000 |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | 12000 Buildings |
| Economic losses | 450 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |