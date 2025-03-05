# 🌎 1999 M6 Athens earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1999 M6 Athens earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1999 Athens earthquake` struck on September 7, 1999, at 14:56 local time, registering a moment magnitude of 6.0 and reaching a maximum intensity of IX on the Modified Mercalli Intensity (MMI) scale. The epicenter was pinpointed near Mount Parnitha, about 17 kilometers northwest of central Athens. The quake caused widespread destruction, particularly in the northern and western suburbs of Athens, with areas such as Ano Liosia, Acharnes, Thrakomakedones, and Nea Philadelphia bearing the brunt of the damage. The disaster claimed the lives of approximately 143 people, left more than 750 injured, and rendered thousands homeless. Economic losses were estimated at a staggering $4500 million USD. Notable incidents of soil liquefaction occurred in coastal and reclaimed areas, though no tsunamis or major landslides were reported. As one of the most catastrophic natural disasters in Greece's modern history, the earthquake left an indelible mark on the nation's infrastructure and collective memory.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1999 |
| Country | Greece |
| Region | Europe |
| Event Name | Athens 1999 |
| Local Date | 07/09/1999 |
| Local Time | 14:56:49 |
| Latitude (decimal degrees) | 38.119 |
| Longitude (decimal degrees) | 23.605 |
| Depth (km) | 10 |
| Mw | 6 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Normal |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0009e46 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~143 |
| Injured | 750-2000 |
| Displaced population | ~108 |
| Affected population | ~113031 |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | 53000 Buildings |
| Economic losses | 4200 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |