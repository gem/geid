# 🌎 2011 M7.1 Van earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2011 M7.1 Van earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2011 Van earthquake`, a magnitude 7.1 event, struck eastern Turkey on October 23, 2011, at 13:41 local time. The maximum Mercalli intensity reached VIII. The epicenter was located near the city of Van. This powerful earthquake caused widespread devastation, particularly in the cities of Van and Erciş. The death toll was tragically high, with over 600 fatalities and 2600 injuries reported. Economic losses were nearly 1500 million USD, and the earthquake triggered numerous landslides and some localized liquefaction. 

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2011 |
| Country | Turkey |
| Region | Europe |
| Event Name | Van 2011 |
| Local Date | 23/10/2011 |
| Local Time | 13:41:23 |
| Latitude (decimal degrees) | 38.721 |
| Longitude (decimal degrees) | 43.508 |
| Depth (km) | 18 |
| Mw | 7.1 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Reverse |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp000j9rr |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~604 |
| Injured | 2608-4152 |
| Displaced population | 22000-150000 |
| Affected population | 32938-700000 |
| Affected units | 4882-40300 Buildings |
| Damaged units | 5739-33016 Buildings |
| Collapsed units | 2262-2309 Buildings |
| Economic losses | 1500 M USD |
| Insured losses | 90 M USD |
| Earthquake-triggered effects | nan |