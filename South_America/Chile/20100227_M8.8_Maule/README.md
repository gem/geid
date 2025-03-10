# 🌎 2010 M8.8 Maule earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2010 M8.8 Maule earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2010 Chilean earthquake` and tsunami, widely referred to as "27F," struck on February 27, 2010, at 03:34 local time, with a moment magnitude (Mw) of 8.8. The epicenter was located off the coast of the Maule Region, approximately 8 km west of Curanipe. The earthquake reached a maximum intensity of VIII on the Modified Mercalli Intensity (MMI) scale, significantly impacting regions such as Maule, Biobío, Valparaíso, Metropolitana de Santiago, and O'Higgins. It inflicted devastating damage on cities including Concepción, Talcahuano, Constitución, and Curicó. This catastrophic event resulted in over 480 fatalities and 500–12000 injuries, with economic losses estimated at over $4000 million USD. The earthquake triggered a series of tsunamis, with wave heights recorded at 2.6 m in Valparaíso and 2.34 m in Talcahuano, wreaking additional havoc on coastal areas such as Robinson Crusoe Island. Reports also documented occurrences of liquefaction, landslides, and widespread power outages. The earthquake was accompanied by an extensive aftershock sequence, with over 283 events exceeding magnitude 5.0, including two significant magnitude 7.0 aftershocks near Pichilemu on March 11. This seismic event marked the culmination of a 170-year seismic silence along the subduction zone between the 1960 Valdivia earthquake and the 1985 Valparaíso earthquake.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2010 |
| Country | Chile |
| Region | South America |
| Event Name | Maule 2010 |
| Local Date | 27/02/2010 |
| Local Time | 03:34:00 |
| Latitude (decimal degrees) | -36.1723 |
| Longitude (decimal degrees) | -73.142 |
| Depth (km) | 30 |
| Mw | 8.8 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Reverse |
| Tectonic region type | Subduction |
| USGS event ID | official20100227063411530 30 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 486-562 |
| Injured | 500-12000 |
| Displaced population | 800000-2000000 |
| Affected population | 800000-1861222 |
| Affected units | ~1500000  |
| Damaged units | 126883-500000  |
| Collapsed units | 81444-81449  |
| Economic losses | 15000-37280 M USD |
| Insured losses | 4000-9941 M USD |
| Earthquake-triggered effects | Tsunami, Landslides |