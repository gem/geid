# 🌎 2003 M6.6 Bam earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2003 M6.6 Bam earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

 The `2003 Bam earthquake`, with a moment magnitude of 6.6, struck Iran on December 26, 2003, at 5:26 AM local time. The epicenter was situated near the city of Bam, in the southeastern Kerman province, at a depth of 10 km. The earthquake caused widespread devastation in Bam and the surrounding areas, particularly damaging buildings in the ancient city of Bam, which was largely reduced to rubble. The earthquake's maximum intensity was recorded at IX on the Modified Mercalli Intensity (MMI) scale, signifying violent shaking and extensive destruction. The estimated number of fatalities exceeded 25000, with more than 14000 individuals injured. Economic losses from the disaster were reported to exceed 32.7 million USD. While no tsunamis were observed, liquefaction and landslides were noted in certain regions, further contributing to the devastation. Aftershocks followed the main quake, including one with a magnitude of 6.4, but no significant foreshocks were reported in the lead-up to the event. The earthquake profoundly impacted the region, underscoring the vulnerability of older, less-seismic-resistant structures in earthquake-prone areas.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2003 |
| Country | Iran |
| Region | Middle East |
| Event Name | Bam |
| Local Date | 26/12/2003 |
| Local Time | 05:26:26 |
| Latitude (decimal degrees) | 29.09 |
| Longitude (decimal degrees) | 58.35 |
| Depth (km) | 10 |
| Mw | 6.6 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Strike Slip |
| Tectonic region type | Active Crustal |
| USGS event ID | usp000cg2d |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 25000-50000 |
| Injured | 14300-200000 |
| Displaced population | 45000-75600 |
| Affected population | 142000-200000 |
| Affected units | nan |
| Damaged units | 2381-20246 Buildings |
| Collapsed units | 10176-52756 Buildings |
| Economic losses | 32.7-1500 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |