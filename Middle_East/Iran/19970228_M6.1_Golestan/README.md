# 🌎 1997 M6.1 Golestan earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1997 M6.1 Golestan earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1997 Ardabil earthquake` struck Iran on February 28 at 12:57 local time, with its epicenter located near the town of Ardabil in the Ardabil Province. The earthquake, with a magnitude of 6.1, and a maximum Modified Mercalli Intensity (MMI) of VIII, caused significant damage to the region, particularly affecting rural areas and villages surrounding the city of Ardabil. Over 950 fatalities were reported, along with approximately 2000 injuries. The earthquake caused widespread destruction to infrastructure and homes, resulting in estimated economic losses of about $76 million USD. Roughly 350 aftershocks followed the main Ardabil earthquake. The largest one had a magnitude of 5.2 on the Richter scale. While liquefaction and landslides were observed in the affected areas, there were no reports of tsunamis or fires associated with this earthquake. The disaster highlighted the vulnerability of rural communities to seismic events in the region.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1997 |
| Country | Iran |
| Region | Middle East |
| Event Name | Golestan |
| Local Date | 28/02/1997 |
| Local Time | 12:57:28 |
| Latitude (decimal degrees) | 38.075 |
| Longitude (decimal degrees) | 48.06 |
| Depth (km) | 10 |
| Mw | 6.1 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Strike Slip |
| Tectonic region type | Active Crustal |
| USGS event ID | usp0007y0b |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 0.62g, observed at location (37.92°N, 48.062°E), corresponding to Kariq. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 954-1100 |
| Injured | 2000-2600 |
| Displaced population | ~0 |
| Affected population | 38600-453756 |
| Affected units | ~0  |
| Damaged units | 12000 Buildings |
| Collapsed units | 12000-13500 Buildings |
| Economic losses | 76 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |