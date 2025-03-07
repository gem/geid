# 🌎 2012 M7.6 Nicoya earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2012 M7.6 Nicoya earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance

 The `2012 Costa Rica earthquake`, also known as the Nicoya earthquake, struck on September 5, 2012, at 8:42 AM local time. It had a moment magnitude of 7.6 and reached an intensity of VII on the Modified Mercalli Intensity (MMI) scale. The epicenter was located near the Nicoya Peninsula, approximately 10 kilometers offshore, at a depth of 40 kilometers. The earthquake primarily impacted the Nicoya Peninsula, the province of Guanacaste, and parts of the Central Valley, including the cities of Liberia, Santa Cruz, and the capital, San José. Economic losses from the event were estimated at $45 million USD, with at least 1 fatality reported and 20 injuries. Liquefaction and landslides were observed in some areas, but no significant tsunamis or fires occurred. The earthquake was preceded by smaller foreshocks and followed by several aftershocks, some of which were strongly felt in the affected regions.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2012 |
| Country | Costa Rica |
| Region | Caribbean Central America |
| Event Name | Nicoya |
| Local Date | 05/09/2012 |
| Local Time | 08:42:00 |
| Latitude (decimal degrees) | 9.828 |
| Longitude (decimal degrees) | -85.545 |
| Depth (km) | 15.4 |
| Mw | 7.6 |
| Max Intensity (MMI) | VII |
| Fault mechanism | Purely inverse |
| Tectonic region type | Subduction interface |
| USGS event ID | usp000jrsw |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 1-2 |
| Injured | 20-225 |
| Displaced population | ~1474 |
| Affected population | ~537 |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | nan |
| Economic losses | 45 M USD |
| Insured losses | 32 M USD |
| Earthquake-triggered effects | Tsunami, landslides  |