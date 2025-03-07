# 🌎 2020 M6.3 Petrijna earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2020 M6.3 Petrijna earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2020 Petrinja earthquake`, with a magnitude of M6.3, struck central Croatia on December 29, 2020, at 12:19 local time. This powerful event reached a maximum intensity of IX on the Modified Mercalli Intensity (MMI) scale. The epicenter was near the town of Petrinja, approximately 47 kilometers southeast of Zagreb. The earthquake caused extensive destruction in Petrinja and the surrounding areas, including the cities of Sisak and Glina, where numerous buildings sustained severe damage or were completely destroyed. The economic losses were estimated at over 4187 million USD. Tragically, the earthquake claimed at least 8 lives and left over 36 people injured. Liquefaction was observed in the affected region, compounding the structural damage; however, no landslides, tsunamis, or fires were reported. The mainshock was preceded by foreshocks, notably a M5.2 event on December 28, and followed by a series of aftershocks, the largest being a M4.9 tremor later on the same day.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2020 |
| Country | Croatia |
| Region | Europe |
| Event Name | Petrijna 2020 |
| Local Date | 29/12/2020 |
| Local Time | 12:19 |
| Latitude (decimal degrees) | 45.4244 |
| Longitude (decimal degrees) | 16.2573 |
| Depth (km) | 10 |
| Mw | 6.3 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Reverse |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | us6000d3zh |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~8 |
| Injured | ~36 |
| Displaced population | nan |
| Affected population | ~149407 |
| Affected units | nan |
| Damaged units | 34056-46000 Buildings |
| Collapsed units | 1500-3062 Buildings |
| Economic losses | 4187-6223 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |