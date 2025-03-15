# 🌎 1995 M6.9 Kobe earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1995 M6.9 Kobe earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The powerful `1995 Kobe earthquake` struck the southern part of Hyōgo Prefecture, Japan, with a significant impact on the Hanshin region, on January 17, 1995, at 05:46 local time. This devastating event, with a moment magnitude (Mw) of 6.9, was classified with an MMI of IX in many affected areas. The epicenter, located near the city of Awaji, caused widespread destruction, particularly in the cities of Kobe, Osaka, and surrounding regions. The earthquake resulted in over 5200 fatalities, more than 34000 injuries, and extensive damage to infrastructure. Economic losses were estimated to exceed 100000 million USD. The disaster triggered severe consequences, including liquefaction, landslides, and widespread fires, particularly in Kobe, where flames ravaged much of the city. While no significant tsunami was recorded, the earthquake was followed by a series of aftershocks, some of which were particularly strong, exacerbating the already catastrophic effects on the region.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1995 |
| Country | Japan |
| Region | East Asia |
| Event Name | Kobe 1995 |
| Local Date | 17/01/1995 |
| Local Time | 05:46:52 |
| Latitude (decimal degrees) | 34.583 |
| Longitude (decimal degrees) | 135.018 |
| Depth (km) | 21.9 |
| Mw | 6.9 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Right-lateral strike slip |
| Tectonic region type | Active Shallow Crustal |
| USGS event ID | usp0006rew |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 5297-6434 |
| Injured | 34492-43792 |
| Displaced population | 251301–310000 |
| Affected population | ~541636 |
| Affected units | >200000 |
| Damaged units | 274182-400000 |
| Collapsed units | 100000-186175 |
| Economic losses | 100000-136000 M USD |
| Insured losses | 3000 M USD |
| Earthquake-triggered effects | Fires |