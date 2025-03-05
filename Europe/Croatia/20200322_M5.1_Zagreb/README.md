# 🌎 2020 M5.3 Zagreb earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2020 M5.3 Zagreb earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2020 Zagreb earthquake`, with a magnitude of M5.3, struck on March 22, 2020, at 6:24 AM local time. Its epicenter was located approximately 7 kilometers north of Zagreb, Croatia. The earthquake, which reached a maximum Modified Mercalli Intensity (MMI) of VIII, caused extensive damage, particularly in Zagreb and its surrounding areas. The capital city was among the hardest hit, with significant damage to older buildings and historic structures. The disaster resulted in 1 reported fatality and approximately 27 injuries, alongside economic losses exceeding 1800 million USD, ranking it as one of the most costly earthquakes in Croatia's modern history. Although no tsunamis, landslides, or fires were recorded, minor liquefaction occurred in certain localized areas. The earthquake was preceded by multiple foreshocks and followed by numerous aftershocks, the strongest reaching a magnitude of 5.0, compounding structural damage and heightening public concern.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2020 |
| Country | Croatia |
| Region | Europe |
| Event Name | Zagreb 2020 |
| Local Date | 22/03/2020 |
| Local Time | 06:24:03 |
| Latitude (decimal degrees) | 45.9072 |
| Longitude (decimal degrees) | 15.9697 |
| Depth (km) | 10 |
| Mw | 5.3 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Reverse |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | us70008dx7 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.
<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~1 |
| Injured | ~27 |
| Displaced population | ~18915 |
| Affected population | ~60000 |
| Affected units | nan |
| Damaged units | 20000 Buildings |
| Collapsed units | 6350 Buildings |
| Economic losses | 1800-6800 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |