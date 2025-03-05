# 🌎 2019 M6.4 Durres earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2019 M6.4 Durres earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

A powerful earthquake with a magnitude of 6.4 struck northwestern Albania at 02:54 local time on November 26, 2019. The epicentre was located 16 kilometres west-southwest of Mamurras. The earthquake reached a maximum intensity of VIII on the Modified Mercalli Intensity (MMI) scale, causing severe damage in the cities of Durrës, Thumanë, and nearby areas. Tragically, the disaster claimed 51 lives and left over 913 people injured, while inflicting significant economic losses estimated at approximately $700 million USD. Instances of liquefaction were observed in several locations, although no landslides, tsunamis, or fires were reported. The event was preceded by foreshocks, including a magnitude 5.6 earthquake two months earlier, and was followed by numerous aftershocks, exacerbating the devastation and challenges faced by the affected communities.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2019 |
| Country | Albania |
| Region | Europe |
| Event Name | Durres |
| Local Date | 26/11/2019 |
| Local Time | 02:54:12 |
| Latitude (decimal degrees) | 41.5138 |
| Longitude (decimal degrees) | 19.5256 |
| Depth (km) | 22 |
| Mw | 6.4 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Reverse |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | us70006d0m |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~51 |
| Injured | 913-2000 |
| Displaced population | nan |
| Affected population | ~202913 |
| Affected units | nan |
| Damaged units | 83000 Buildings |
| Collapsed units | 11000 Buildings |
| Economic losses | 700-1081 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |