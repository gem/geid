# 🌎 1991 M7.6 Limon earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1991 M7.6 Limon earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance

The `1991 Costa Rica earthquake`, also known as the Limon earthquake, occurred on April 22, 1991, at 15:57 local time. It had a moment magnitude of 7.6 and an MMI of VIII, indicating strong to severe shaking. The epicenter was located near Cahuita, in the province of Limon, on the Caribbean coast of Costa Rica. The earthquake primarily affected the regions of Limon, San José, and parts of Puntarenas. The reported fatalities were over 47, with more than 100 people reported as injured. The earthquake caused significant economic losses, amounting to over 40 million USD. The event triggered various geotechnical phenomena, including landslides and liquefaction in some areas, particularly along the coastal regions. Fortunately, no significant tsunami was observed, though the earthquake caused extensive damage to infrastructure and homes. Following the main shock, multiple aftershocks were recorded, compounding the challenges faced by local communities during the recovery period.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1991 |
| Country | Costa Rica |
| Region | Caribbean Central America |
| Event Name | Limon |
| Local Date | 22/04/1991 |
| Local Time | 15:57:00 |
| Latitude (decimal degrees) | 9.685 |
| Longitude (decimal degrees) | -83.073 |
| Depth (km) | 10 |
| Mw | 7.6 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Reverse |
| Tectonic region type | Shallow crustal  |
| USGS event ID | usp0004qpg |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 47-127 |
| Injured | 109-895 |
| Displaced population | 7439-10900 |
| Affected population | ~6320 |
| Affected units | nan |
| Damaged units | 7869 Buildings |
| Collapsed units | 4452 Buildings |
| Economic losses | 43-510 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Tsunami, landslides, liquefaction |