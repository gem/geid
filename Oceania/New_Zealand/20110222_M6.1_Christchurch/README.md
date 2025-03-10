# 🌎 2011 M6.1 Christchurch earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2011 M6.1 Christchurch earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2011 Christchurch earthquake`, which struck on Tuesday, 22 February at 12:51 local time, had a moment magnitude of 6.1. The epicentre was located 10 kilometres southeast of Christchurch, near the town of Lyttelton, and it caused extensive devastation across the Christchurch region, with the central business district being particularly affected. The earthquake reached a maximum intensity of IX on the Modified Mercalli Intensity (MMI) scale. The economic impact was significant, with losses estimated at approximately 15000 million USD. Tragically, over 180 lives were lost, and more than 1500 people were injured. Liquefaction was widely observed, leading to severe damage to infrastructure, while landslides occurred in surrounding areas. Notably, no tsunamis or large fires were reported. The event was preceded by numerous aftershocks, some of which caused additional damage, and was part of a series of seismic events, following a larger earthquake that had affected the region in September 2010.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2011 |
| Country | New Zealand |
| Region | Oceania |
| Event Name | Christchurch 2011 |
| Local Date | 22/02/2011 |
| Local Time | 12:51:42 |
| Latitude (decimal degrees) | -43.583 |
| Longitude (decimal degrees) | 172.68 |
| Depth (km) | 5.9 |
| Mw | 6.1 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Oblique thrust |
| Tectonic region type | Active shallow crustal |
| USGS event ID | usp000huvq |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 1.63 g, observed at Heathcote Valley Primary School site (station code: HVSC). If no seismic station data were available for the event, the generated ground motion fields are shown w

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 181-185 |
| Injured | 1500-7171 |
| Displaced population | nan |
| Affected population | ~301500 |
| Affected units | nan |
| Damaged units | ~100000 |
| Collapsed units | nan |
| Economic losses | 15000 M USD |
| Insured losses | 3500-12000 M USD |
| Earthquake-triggered effects | Liquefaction, landslides |