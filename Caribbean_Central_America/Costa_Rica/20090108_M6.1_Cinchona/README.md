# 🌎 2009 M6.1 Cinchona earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2009 M6.1 Cinchona earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance

The `2009 Cinchona earthquake` in Costa Rica occurred on January 8, with a moment magnitude of 6.1 and a maximum intensity of IX on the Modified Mercalli Intensity (MMI) scale. The earthquake struck at 13:21 local time, with its epicenter located near Cinchona, approximately 50 kilometers north of the capital, San José. The most affected areas included the central and northwestern regions of the country, particularly the provinces of Alajuela and Heredia, with significant damage in towns like Vara Blanca and Sarchí. The earthquake caused widespread infrastructure damage, resulting in reported economic losses exceeding 100 million USD. Tragically, more than 23 people lost their lives, and over 90 others were injured. Although no tsunamis were reported, landslides were extensive, particularly in the mountainous regions, severely disrupting transportation and impacting local communities. Liquefaction was not observed, and fires were minimal. Aftershocks followed the main event, with several occurring in the days that followed.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2009 |
| Country | Costa Rica |
| Region | Caribbean Central America |
| Event Name | Cinchona |
| Local Date | 08/01/2009 |
| Local Time | 13:21:00 |
| Latitude (decimal degrees) | 10.116 |
| Longitude (decimal degrees) | -84.106 |
| Depth (km) | 4.6 |
| Mw | 6.1 |
| Max Intensity (MMI) | IX in Cinchona e Isla Bonita  |
| Fault mechanism | Strike slip |
| Tectonic region type | Active shallow crustal  |
| USGS event ID | usp000gscg |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 23-98 |
| Injured | 91-100 |
| Displaced population | 1244-2326 |
| Affected population | ~128527 |
| Affected units | nan |
| Damaged units | 518 Buildings |
| Collapsed units | 518 Buildings |
| Economic losses | 100-200 M USD |
| Insured losses | 100 M USD |
| Earthquake-triggered effects | nan |