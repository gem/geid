# 🌎 2016 M5.9 Bukoba earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2016 M5.9 Bukoba earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2016 Bukoba earthquake` in Tanzania occurred on September 10, 2016, at 15:27 local time, with a magnitude of 5.9 and very strong (VII) shaking along the border between Tanzania and Uganda. The earthquake's epicenter was located near Bukoba, in the Kagera Region of northwestern Tanzania, close to the borders with Uganda and Rwanda. The most affected regions included Bukoba Town, the Kagera Region, and surrounding areas, extending into parts of Uganda. The earthquake caused significant damage to infrastructure, homes, and businesses, resulting in economic losses estimated at approximately 458 million USD (at the time of the event). Tragically, the event led to at least 21 fatalities and around 440 injuries. In addition to the structural damage, there were reports of landslides in the affected areas, although no liquefaction, tsunamis, or fires were observed as a result of the earthquake.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2016 |
| Country | Tanzania |
| Region | Africa |
| Event Name | Bukoba 2016 |
| Local Date | 10/09/2016 |
| Local Time | 15:27:33 |
| Latitude (decimal degrees) | -1.0355 |
| Longitude (decimal degrees) | 31.6181 |
| Depth (km) | 40 |
| Mw | 5.9 |
| Max Intensity (MMI) | VII |
| Fault mechanism | Strike-slip |
| Tectonic region type | Cratonic |
| USGS event ID | us10006nkx |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 21-23 |
| Injured | ~440 |
| Displaced population | 590-10000 |
| Affected population | ~139161 |
| Affected units | nan |
| Damaged units | 1125-6281  |
| Collapsed units | 118-7500  |
| Economic losses | 458 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |