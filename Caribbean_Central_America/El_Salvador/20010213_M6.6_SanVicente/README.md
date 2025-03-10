# 🌎 2001 M6.6 San Vicente earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2001 M6.6 San Vicente earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance

The `February 2001 El Salvador earthquake` struck on February 13, 2001, with a moment magnitude of 6.6, occurring at 8:22 AM local time. The earthquake's epicenter was located 15 miles (30 km) east of San Salvador, El Salvador. This event took place nearly a month after the significant earthquake in January, which affected the same region, though it remains uncertain whether the two events are related. The earthquake impacted several areas, including Cojutepeque, San Martín, San Vicente, San Salvador, San Miguel, San Juan Tepezontes, Santa Cruz Analquito, and Candelaria in the Department of Cuscatlán, while it was also felt across the entire country and in neighboring Guatemala and Honduras. The maximum intensity reached MMI VIII, with widespread damage reported in the affected areas. The earthquake tragically resulted in over 280 fatalities and left more than 2600 injured. The economic impact was severe, with losses estimated at over $348 million USD. In addition to the structural damage, the earthquake triggered landslides, particularly in mountainous regions, and caused liquefaction in certain areas. Fortunately, no tsunamis or fires were observed. Numerous aftershocks followed the main event, exacerbating the destruction and complicating ongoing rescue efforts.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2001 |
| Country | El Salvador |
| Region | Caribbean Central America |
| Event Name | San Vicente 2001 |
| Local Date | 13/02/2001 |
| Local Time | 08:22:05 |
| Latitude (decimal degrees) | 13.64 |
| Longitude (decimal degrees) | -88.94 |
| Depth (km) | 13 |
| Mw | 6.6 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Strike Slip |
| Tectonic region type | Active Shallow Crustal |
| USGS event ID | usp000a9jv |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 286-315 |
| Injured | 2696-3399 |
| Displaced population | nan |
| Affected population | 250000-279753 |
| Affected units | ~57008  |
| Damaged units | 14339-17084  |
| Collapsed units | 35196-57242  |
| Economic losses | 348.5 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides |