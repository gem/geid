# 🌎 1994 M6.8 Cacua earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1994 M6.8 Cacua earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1994 Páez River earthquake`, also referred to as the Páez River disaster, struck southwestern Colombia on June 6, 1994, at 03:47 local time. With a moment magnitude (Mw) of 6.8 and a depth of 12 km, the earthquake’s epicenter was located near the town of Páez, in the department of Cauca. The Modified Mercalli Intensity (MMI) reached a peak of IX in the affected areas. The earthquake’s impact was most strongly felt in the municipalities of Páez, Toribío, Inzá, Jambaló, and Totoró, where extensive structural damage occurred, including the collapse and severe damage of numerous buildings. The earthquake’s violent shaking also triggered widespread landslides and avalanches, resulting in over 128 fatalities, with the town of Páez alone accounting for about 50% of the casualties. Additionally, more than 158 people were injured. The economic toll was significant, with estimated losses totaling approximately 2.4 million USD. The destruction affected homes, crops, and critical infrastructure, while the obstruction of rivers due to landslides led to further avalanches that devastated entire communities. The challenges of distinguishing between the direct effects of the earthquake and the damage caused by the landslides and avalanches complicated assessments of the total impact. Notably, there were no reports of liquefaction, tsunamis, or fires. The severity of the event was heightened by the region’s deforestation, topography, and the ongoing winter season. The 1994 Páez River earthquake remains one of the most destructive seismic events in the history of the region.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1994 |
| Country | Colombia |
| Region | South America |
| Event Name | Cacua 1994 |
| Local Date | 06/06/1994 |
| Local Time | 03:47:00 |
| Latitude (decimal degrees) | 2.89 |
| Longitude (decimal degrees) | -75.95 |
| Depth (km) | 10 |
| Mw | 6.8 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Strike-Slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0006dv8 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 128-1100 |
| Injured | 158-207 |
| Displaced population | 13000-24797 |
| Affected population | 12461-28569 |
| Affected units | ~1664  |
| Damaged units | ~3160  |
| Collapsed units | ~200  |
| Economic losses | 2.4 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides, Flood, Avalanches |