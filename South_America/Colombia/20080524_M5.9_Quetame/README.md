# 🌎 2008 M5.9 Quetame earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2008 M5.9 Quetame earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2008 El Calvario earthquake` struck central Colombia on May 24, 2008, at 14:20 local time, with a moment magnitude (Mw) of 5.9. Its epicenter was located near El Calvario, Meta, at a depth of 35 km, classifying it as a shallow earthquake. The tremor was strongly felt across a wide area, including Bogotá, Villavicencio, and as far as Medellín and Bucaramanga. However, the towns of Quetame, Puente Quetame, Fosca, Fomeque, and Guayabetal endured the most significant impacts. The earthquake resulted in 5 to 33 fatalities and 32 to 4181 injuries, inflicting severe damage on residential, commercial, and public infrastructure. The town of Quetame, home to approximately 6,500 residents, suffered the most extensive destruction, with numerous houses collapsing. The widespread damage was exacerbated by poor construction practices, such as the use of adobe structures with inadequate structural support. Economic losses from the disaster were estimated at 10 million USD (based on an exchange rate of COP 2000). Landslides emerged as a prominent consequence of the earthquake and hindering rescue operations. Additionally, mass movements, including flows, slippage, and rockfalls, were reported in heavily affected areas like Quetame, El Calvario, and Fómeque. Notably, there were no reports of liquefaction, tsunamis, or fires. A significant aftershock sequence followed the main event, with 597 aftershocks recorded, the largest of which—a Mw 4.5 tremor—occurred just three minutes after the initial quake. The disaster caused widespread panic, overwhelming telecommunications networks and prompting heightened emergency alerts in Bogotá. This tragic event underscored the vulnerability of local infrastructure and emphasized the critical need for improved construction standards to mitigate the risks of future seismic activity.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2008 |
| Country | Colombia |
| Region | South America |
| Event Name | Quetame 2008 |
| Local Date | 24/05/2008 |
| Local Time | 14:20:00 |
| Latitude (decimal degrees) | 4.44 |
| Longitude (decimal degrees) | -73.81 |
| Depth (km) | 10 |
| Mw | 5.9 |
| Max Intensity (MMI) | VII |
| Fault mechanism | Strike-Slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp000g7p6 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 5-33 |
| Injured | 32-4181 |
| Displaced population | 1700-9000 |
| Affected population | 1754-10000 |
| Affected units | nan |
| Damaged units | 160-2316  |
| Collapsed units | 47-1234  |
| Economic losses | 10 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides |