# 🌎 2005 M7.6 Kashmir earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2005 M7.2 Kashmir earthquake in Pakistan.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2005 Pakistan earthquake` occurred on 8 October at 08:50 local time, registering a moment magnitude of 7.6 in the region of Azad Jammu and Kashmir. The epicenter, located near Muzaffarabad in northern Pakistan, experienced a maximum intensity of IX on the Modified Mercalli Intensity (MMI) scale. The most heavily impacted regions included Azad Jammu and Kashmir and parts of northern Pakistan, with cities such as Muzaffarabad, Rawalakot, and Bagh suffering significant devastation. The earthquake resulted in over 74000 fatalities and left more than 75000 individuals injured. The economic impact was substantial, with losses exceeding $5000 million USD. The region also faced severe landslides that blocked key roads, hindering rescue efforts, although no tsunamis or fires were reported. Liquefaction was observed in several areas, compounding the damage. Aftershocks followed the main event, exacerbating the strain on already fragile infrastructure.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2005 |
| Country | Pakistan |
| Region | South Asia |
| Event Name | Kashmir |
| Local Date | 08/10/2005 |
| Local Time | 08:50:39 |
| Latitude (decimal degrees) | 34.539 |
| Longitude (decimal degrees) | 73.588 |
| Depth (km) | 26 |
| Mw | 7.6 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Reverse |
| Tectonic region type | Active shallow crustal |
| USGS event ID | usp000e12e |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 74689-88705 |
| Injured | 75277-206277 |
| Displaced population | ~2800000 |
| Affected population | >5000000 |
| Affected units | nan |
| Damaged units | 780000 Buildings |
| Collapsed units | 32335 Buildings |
| Economic losses | 5000-6680 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides, rockfall, seiche |