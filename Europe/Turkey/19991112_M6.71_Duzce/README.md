# 🌎 1999 M6.71 Duzce earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1999 M6.71 Duzce earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1999 Düzce earthquake`, a magnitude 6.71 event, struck northwestern Turkey on November 12, 1999, at 18:57 local time. The epicenter was located near the city of Düzce, along the North Anatolian Fault. This powerful earthquake followed the devastating İzmit earthquake that occurred earlier that year. The Düzce earthquake caused significant damage and loss of life, although the impact was less severe than the İzmit event. The death toll was estimated at around 845, and 4948 injuries were reported. Economic losses were roughly 1000 million USD, and the earthquake triggered numerous landslides and some localized liquefaction.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1999 |
| Country | Turkey |
| Region | Europe |
| Event Name | Duzce 1999 |
| Local Date | 12/11/1999 |
| Local Time | 18:57:19 |
| Latitude (decimal degrees) | 40.758 |
| Longitude (decimal degrees) | 31.161 |
| Depth (km) | 10 |
| Mw | 6.71 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Strike-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0009hev |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 845-894 |
| Injured | ~4948 |
| Displaced population | ~55000 |
| Affected population | ~224948 |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | nan |
| Economic losses | 1000 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |