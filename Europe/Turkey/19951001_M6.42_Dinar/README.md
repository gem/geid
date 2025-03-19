# 🌎 1995 M6.42 Dinar earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1995 M6.42 Dinar earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1995 Dinar earthquake` struck on October 1, 1995, at 15:57 local time, near the town of Dinar, Turkey. This magnitude 6.42 event, centered on the Dinar-Çivril fault, caused significant damage to the region. The event caused significant damage to the region, with approximately 90 fatalities and over 200 injuries reported. Its intensity reached a maximum of VIII on the Mercalli scale, and economic losses were about 205.8 million USD. While no tsunamis occurred, the earthquake triggered numerous landslides and some localized liquefaction.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1995 |
| Country | Turkey |
| Region | Europe |
| Event Name | Dinar |
| Local Date | 01/10/1995 |
| Local Time | 15:57:16 |
| Latitude (decimal degrees) | 38.063 |
| Longitude (decimal degrees) | 30.134 |
| Depth (km) | 33 |
| Mw | 6.42 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Normal |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp000749b |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 90-95 |
| Injured | 200-348 |
| Displaced population | ~40000 |
| Affected population | ~120000 |
| Affected units | nan |
| Damaged units | 2473-5100 Buildings |
| Collapsed units | nan |
| Economic losses | 205.8 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |