# 🌎 2015 M6.5 Lefkada earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2015 M6.5 Lefkada earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2015 Lefkada earthquake` struck on November 17, 2015, at 10:40 local time, registering a moment magnitude (Mw) of 6.5 and reaching a maximum Mercalli Intensity (MMI) of VIII. The epicenter was located off the western coast of Lefkada Island in the Ionian Sea, Greece, a region known for its seismic activity. The earthquake severely impacted Lefkada Town, Athani, and nearby western coastal areas, causing extensive damage to buildings and infrastructure. Economic losses were estimated at $20 million USD, with 2 fatalities and 4 injuries reported. The event triggered landslides, particularly along Lefkada’s steep western cliffs, leading to road blockages and compounding the damage. This disaster underscored the seismic vulnerability of the region, situated along the tectonically active Hellenic Arc, and highlighted the need for improved preparedness and resilience in earthquake-prone areas.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2015 |
| Country | Greece |
| Region | Europe |
| Event Name | Lefkada 2015 |
| Local Date | 17/11/2015 |
| Local Time | 10:40:07 |
| Latitude (decimal degrees) | 38.67 |
| Longitude (decimal degrees) | 20.6 |
| Depth (km) | 11 |
| Mw | 6.5 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Strike-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | us10003ywp |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 0-2 |
| Injured | 4-10 |
| Displaced population | nan |
| Affected population | nan |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | 1 Buildings |
| Economic losses | 20 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides, rock falls, road cracks, ground subsidence, liquefaction |