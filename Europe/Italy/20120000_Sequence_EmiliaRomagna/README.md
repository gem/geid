# 🌎 2012 M6 EmiliaRomagna earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2012 M6 EmiliaRomagna earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

In May 2012, Northern Italy was impacted by two significant earthquakes, collectively known as the 2012 Emilia earthquakes. The first earthquake, registering a magnitude of 5.8, occurred on 20 May 2012 at 04:03 local time in the Emilia-Romagna region, approximately 36 kilometers north of Bologna. The epicenter was located between the towns of Finale Emilia, Bondeno, and Sermide. Nine days later, on 29 May 2012, a second earthquake with a magnitude of 5.6 struck the same region, with its epicenter near Medolla, at a depth of approximately 10 kilometers. This sequence of events led to 26 fatalities and more than 50 injuries, particularly due to further damage to buildings already weakened by the earlier quake. The most severely impacted towns included Finale Emilia, Bondeno, Sermide, and Medolla. The economic losses were estimated at €10000 million EUR. While landslides were observed in several areas, there were no significant reports of liquefaction or tsunamis. The 2012 Emilia earthquakes underscored the vulnerabilities of both historic and modern infrastructure in the region, highlighting the critical need for enhanced seismic preparedness and building resilience.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2012 |
| Country | Italy |
| Region | Europe |
| Event Name | EmiliaRomagna 2012 |
| Local Date | 20/05/2012 |
| Local Time | 04:03:52 |
| Latitude (decimal degrees) | 44.89 |
| Longitude (decimal degrees) | 11.23 |
| Depth (km) | 6.3 |
| Mw | 6 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Inverse |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp000jkn8 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./20120520_M5.8_EmiliaRomagna/4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./20120520_M5.8_EmiliaRomagna/4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 7-26 |
| Injured | 50-350 |
| Displaced population | ~15000 |
| Affected population | 11050-15000 |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | nan |
| Economic losses | 10000 M EUR -15800 M USD |
| Insured losses | 1300 M USD |
| Earthquake-triggered effects | nan |