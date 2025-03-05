# 🌎 2017 M6.46 Moijabana earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2017 M6.46 Moijabana earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2017 Moijabana earthquake` struck Botswana on April 3, 2017, at 19:40 local time. It registered an estimated magnitude of Mw 6.5 and caused severe (VIII) shaking in a rural area near the village of Moijabana, approximately 238 kilometers north of Gaborone, the nation's capital. The earthquake's effects were felt across much of Botswana and neighboring countries, including South Africa and Zimbabwe. The most affected areas were villages near the epicenter, where structural damage to buildings was reported. Fortunately, despite its significant magnitude, the earthquake did not result in any fatalities or major economic losses. However, 36 injuries were reported, primarily caused by a stampede triggered by the tremor. No secondary hazards such as liquefaction, landslides, tsunamis, or fires were observed. The event underscored the region's susceptibility to moderate seismic activity, despite being located in an intraplate tectonic setting. Following the mainshock, at least 30 aftershocks with magnitudes greater than 3.0 were recorded (ISC).

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2017 |
| Country | Botswana |
| Region | Africa |
| Event Name | Moijabana 2017 |
| Local Date | 03/04/2017 |
| Local Time | 19:40:18 |
| Latitude (decimal degrees) | -22.6784 |
| Longitude (decimal degrees) | 25.1558 |
| Depth (km) | 23.5 |
| Mw | 6.46 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Normal |
| Tectonic region type | Unknown (occurred in an area with no know previous seismicity) |
| USGS event ID | us10008e3k |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~0 |
| Injured | ~0 |
| Displaced population | ~271 |
| Affected population | ~271 |
| Affected units | nan |
| Damaged units | ~13  |
| Collapsed units | nan |
| Economic losses | nan |
| Insured losses | nan |
| Earthquake-triggered effects | Stampede |