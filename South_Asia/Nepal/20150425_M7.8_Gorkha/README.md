# 🌎 2015 M7.8 Gorkha earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2015 M7.8 Gorkha earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The April `2015 Nepal earthquake`, also referred to as the Gorkha earthquake, occurred on April 25, 2015, at 11:56 AM local time. This devastating event had a moment magnitude of 7.8 and reached a maximum intensity of IX on the Modified Mercalli Intensity (MMI) scale. The epicenter was located in the Gorkha district, approximately 77 km northwest of Kathmandu. The earthquake led to widespread destruction across central Nepal, with Kathmandu, Bhaktapur, and Lalitpur being among the most severely impacted areas. The economic losses were reported to exceed $100 million USD, and the human toll was significant, with over 8600 fatalities and more than 17900 injuries. In addition to the structural damage, the event triggered severe landslides, particularly in mountainous regions, and liquefaction was observed in certain locations. While no tsunamis or fires were reported, aftershocks continued to impact the region for weeks following the initial quake. A particularly powerful aftershock, measuring 7.3 in magnitude, struck on May 12, 2015, compounding the damage and hindering recovery efforts.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2015 |
| Country | Nepal |
| Region | South Asia |
| Event Name | Gorkha 2015 |
| Local Date | 25/04/2015 |
| Local Time | 11:56:25 |
| Latitude (decimal degrees) | 28.2305 |
| Longitude (decimal degrees) | 84.7314 |
| Depth (km) | 8.22 |
| Mw | 7.8 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Thrust/reverse |
| Tectonic region type | Subduction interface |
| USGS event ID | us20002926 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 8659-9094 |
| Injured | 17932-24000 |
| Displaced population | 95100-649815 |
| Affected population | 27723-5621790 |
| Affected units | ~8000000 |
| Damaged units | 256697-288856 |
| Collapsed units | 498852-604930 |
| Economic losses | 6000-7000 M USD |
| Insured losses | 100 M USD |
| Earthquake-triggered effects | Avalanches on Mount Everest, landslides |