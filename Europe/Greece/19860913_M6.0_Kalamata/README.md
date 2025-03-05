# 🌎 1986 M6 Kalamata earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1986 M6 Kalamata earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1986 Kalamata earthquake` struck the southern Peloponnese region of Greece on September 13th at 20:24 local time. The maximum Mercalli intensity reached VIII. This magnitude 6.0 earthquake, with an epicenter near the coastal city of Kalamata, caused significant damage and loss of life. The city of Kalamata and the surrounding areas were most heavily impacted, with numerous buildings collapsing or sustaining severe structural damage. At least 20 people were killed, and 300 more were injured. Economic losses were substantial, estimated at around 745 million USD. The earthquake triggered numerous landslides, and some localized liquefaction was observed.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1986 |
| Country | Greece |
| Region | Europe |
| Event Name | Kalamata 1986 |
| Local Date | 13/09/1986 |
| Local Time | 20:24:31 |
| Latitude (decimal degrees) | 37.014 |
| Longitude (decimal degrees) | 22.176 |
| Depth (km) | 11.2 |
| Mw | 6 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Normal |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0002y1v |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~20 |
| Injured | ~300 |
| Displaced population | nan |
| Affected population | ~45300 |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | 1500 Buildings |
| Economic losses | 0-745 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |