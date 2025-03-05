# 🌎 1988 M5.9 Elia earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1988 M5.9 Elia earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1988 Elia earthquake` struck southwestern Greece on October 16, 1988, at 15:34 local time. Its epicenter was located in the straits separating the island of Zakynthos from the Peloponnese Peninsula. This magnitude 5.9 event, with a maximum intensity of VII on the Modified Mercalli Intensity scale, caused significant damage in Zakynthos town and parts of the Peloponnese. Homes, businesses, and infrastructure suffered considerable damage. Economic losses were substantial, reaching tens of millions of drachmas. The earthquake resulted in fatalities and numerous injuries. Liquefaction was observed near coastal areas, while landslides occurred in several parts of the affected region, further complicating recovery efforts.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1988 |
| Country | Greece |
| Region | Europe |
| Event Name | Elia 1988 |
| Local Date | 16/10/1988 |
| Local Time | 15:34:05 |
| Latitude (decimal degrees) | 37.938 |
| Longitude (decimal degrees) | 20.932 |
| Depth (km) | 25.2 |
| Mw | 5.9 |
| Max Intensity (MMI) | VII |
| Fault mechanism | Strike-slip |
| Tectonic region type | Subduction Interface |
| USGS event ID | usp0003mvg |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | nan |
| Injured | nan |
| Displaced population | ~25 |
| Affected population | nan |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | nan |
| Economic losses | nan |
| Insured losses | nan |
| Earthquake-triggered effects | nan |