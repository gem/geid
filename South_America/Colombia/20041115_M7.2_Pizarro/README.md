# 🌎 2004 M7.2 Pizarro earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2004 M7.2 Pizarro earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance

The `2004 Bajo Baudo Earthquake`, also referred to as the Pizarro Earthquake, struck the Colombian Pacific coast on November 15, 2004, at 04:06 local time. This significant seismic event had a moment magnitude (Mw) of 7.2, with its epicenter located in the Pacific Ocean, approximately 50 km southwest of the municipality of Bajo Baudo. The earthquake reached a maximum observed intensity of MMI VIII, reflecting severe shaking in the hardest-hit areas. The quake caused widespread devastation in Bajo Baudo and its surroundings, with regions such as Cali, Buenaventura, and various municipalities in Chocó, Valle del Cauca, and Cauca experiencing considerable damage to infrastructure and structural failures. Liquefaction, soil cracking, and temporary flooding were reported in the epicentral zone, amplifying the destruction. In Buenaventura, changes in sea levels disrupted low-lying neighborhoods like Pampalinda. The earthquake resulted in over 6 injuries, further highlighting its impact. Following the mainshock, an intense aftershock sequence unfolded, with over 1000 aftershocks recorded within the first two weeks. Among these were five aftershocks with magnitudes between 4.0 and 4.4 and more than fifteen ranging between 3.5 and 4.0. The majority of aftershocks were between 1.0 and 3.5, causing ongoing tremors and heightened anxiety across the affected communities.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2004 |
| Country | Colombia |
| Region | South America |
| Event Name | Pizarro 2004 |
| Local Date | 15/11/2004 |
| Local Time | 04:06:00 |
| Latitude (decimal degrees) | 4.69 |
| Longitude (decimal degrees) | -77.47 |
| Depth (km) | 15 |
| Mw | 7.2 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Reverse |
| Tectonic region type | Subduction Interface |
| USGS event ID | usp000d8gx |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | nan |
| Injured | 6-20 |
| Displaced population | nan |
| Affected population | ~8016 |
| Affected units | ~1000  |
| Damaged units | 611-1978  |
| Collapsed units | 154-296  |
| Economic losses | nan |
| Insured losses | nan |
| Earthquake-triggered effects | Liquefaction |