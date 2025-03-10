# 🌎 2017 M7.1 Puebla earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2017 M7.1 Puebla earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2017 Puebla earthquake` struck central Mexico on September 19, 2017, at 13:14 local time, registering a moment magnitude of 7.1. Its epicenter was near Axochiapan, in the state of Morelos, approximately 120 km southeast of Mexico City. The earthquake caused extensive damage across Mexico City and the states of Puebla, Morelos, and the State of Mexico, with a Modified Mercalli Intensity (MMI) of VIII in the worst-affected areas. Tragically, the disaster claimed the lives of more than 360 people, left over 6000 injured, and inflicted widespread devastation on buildings and infrastructure. Economic losses were estimated to range between $4000 million and $8000 million USD. While no tsunamis were reported, the quake triggered liquefaction and landslides, further compounding the destruction. Fortunately, no fires were directly attributed to the event. A series of aftershocks followed, though none caused comparable damage. Remarkably, the earthquake occurred on the anniversary of the catastrophic 1985 Mexico City earthquake, deepening the emotional and historical significance of the date in the region's collective memory.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2017 |
| Country | Mexico |
| Region | North America |
| Event Name | Puebla 2017 |
| Local Date | 19/09/2017 |
| Local Time | 13:14:39 |
| Latitude (decimal degrees) | 18.3297 |
| Longitude (decimal degrees) | -98.6712 |
| Depth (km) | 51.2 |
| Mw | 7.1 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Normal |
| Tectonic region type | Subduction Intraslab |
| USGS event ID | us2000ar20 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 362-471 |
| Injured | 6000-7289 |
| Displaced population | 5000-193546  |
| Affected population | 216672-250000 |
| Affected units | 150000-190000 Buildings |
| Damaged units | 54473 Buildings |
| Collapsed units | 19261 Buildings |
| Economic losses | 4000-8000 M USD |
| Insured losses | 725-2000 M USD |
| Earthquake-triggered effects | Landslides |