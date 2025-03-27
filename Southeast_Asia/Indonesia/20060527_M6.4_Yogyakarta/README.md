# 🌎 2006 M6.4 Yogyakarta earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2006 M6.4 Yogyakarta earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2006 Yogyakarta earthquake` struck Indonesia on May 27, 2006, at 5:54 AM local time. With a magnitude of 6.4, the epicenter was located near the Indian Ocean, approximately 25 kilometers south of the city of Yogyakarta, in the Bantul District of Central Java. The earthquake caused widespread devastation in the region, with Yogyakarta and surrounding areas, such as Bantul, Klaten, and Sleman, being the most affected. The disaster resulted in over 5100 fatalities and more than 36000 injuries, with hundreds of thousands of homes damaged or destroyed. The economic losses were estimated at around $40 million USD (at the time of the event). Although there was no tsunami, the earthquake triggered landslides in the affected areas and caused significant ground shaking that led to liquefaction in some locations, further complicating the recovery efforts. However, there were no reports of fires resulting from the earthquake.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2006 |
| Country | Indonesia |
| Region | Southeast Asia |
| Event Name | Yogyakarta |
| Local Date | 27/05/2006 |
| Local Time | 05:54:00 |
| Latitude (decimal degrees) | -7.961 |
| Longitude (decimal degrees) | 110.446 |
| Depth (km) | 12.5 |
| Mw | 6.4 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Strike slip |
| Tectonic region type | Shallow crustal  |
| USGS event ID | usp000ej1c |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 0.336 g, observed at the YOGI Station. However, various studies estimate that the event's maximum PGA ranged between 0.50 and 0.60 g. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 5176-5782 |
| Injured | 36299-137883 |
| Displaced population | 600000-699295 |
| Affected population | ~2340745 |
| Affected units | nan |
| Damaged units | 127000-451000 Buildings |
| Collapsed units | 127000-154000 Buildings |
| Economic losses | 3100 M USD |
| Insured losses | 40 M USD |
| Earthquake-triggered effects | Ground movement |