# 🌎 1989 M5.4 Newcastle earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1989 M5.4 Newcastle earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1989 Newcastle earthquake` in Australia occurred on December 28, 1989, at 10:27 AM local time. With a moment magnitude of 5.4 and a maximum MMI intensity of VIII, the epicenter was situated near the city of Newcastle, in New South Wales. The earthquake primarily affected Newcastle and its surrounding regions, including Wollongong and Sydney. The event resulted in at least 9 fatalities and over 100 injuries, alongside significant economic losses, estimated at over $900 million USD in damages. While the earthquake did not trigger tsunamis, it was accompanied by liquefaction, landslides, and fires, particularly in the Newcastle area. Following the main shock, aftershocks were reported, though no major foreshocks were recorded. This event remains one of Australia's most destructive earthquakes, both in terms of its economic impact and the extensive damage to infrastructure.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1989 |
| Country | Australia |
| Region | Oceania |
| Event Name | Newcastle |
| Local Date | 28/12/1989 |
| Local Time | 10:27:00 |
| Latitude (decimal degrees) | -32.967 |
| Longitude (decimal degrees) | 151.619 |
| Depth (km) | 10 |
| Mw | 5.4 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Thrust/reverse  |
| Tectonic region type | Stable Continental Regions (SCRs)  |
| USGS event ID | usp00043na |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 9-12 |
| Injured | 100-160 |
| Displaced population | nan |
| Affected population | 2000-300000 |
| Affected units | nan |
| Damaged units | 1000-50000 |
| Collapsed units | ~300 |
| Economic losses | 900-1100 M USD |
| Insured losses | 396-500 M USD |
| Earthquake-triggered effects | nan |