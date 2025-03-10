# 🌎 2010 M7.0 Canterbury earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2010 M7.0 Canterbury earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2010 Canterbury earthquake`, also referred to as the Darfield earthquake, struck on September 4, 2010, at 4:35 AM local time in New Zealand. With a moment magnitude of 7.0 and a maximum intensity of VIII (MMI), the earthquake caused significant shaking throughout the region. The epicenter was located near Darfield, approximately 40 km west of Christchurch, within the Canterbury region. Christchurch, along with neighboring towns such as Rolleston and Lyttelton, experienced extensive structural damage, making them the most heavily impacted areas. The earthquake resulted in estimated economic losses of approximately 6500 million USD, largely due to property damage and business disruptions. While no direct fatalities were reported, injuries ranged from 2 to 2256 individuals. Widespread liquefaction was observed, particularly in eastern Christchurch, where large areas of land experienced ground subsidence and significant damage. A series of aftershocks followed the main event, including a notable one on December 23, 2011, while foreshocks were also felt in the lead-up to the earthquake. Remarkably, the earthquake did not trigger any tsunamis or fires.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2010 |
| Country | New Zealand |
| Region | Oceania |
| Event Name | Canterbury 2010 |
| Local Date | 04/09/2010 |
| Local Time | 04:35:47 |
| Latitude (decimal degrees) | -43.522 |
| Longitude (decimal degrees) | 171.83 |
| Depth (km) | 12 |
| Mw | 7.0 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Strike slip |
| Tectonic region type | Active shallow crustal |
| USGS event ID | usp000hk46 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~0 |
| Injured | 2-2256 |
| Displaced population | nan |
| Affected population | ~300002 |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | nan |
| Economic losses | 6500 M USD |
| Insured losses | 2000-5000 M USD |
| Earthquake-triggered effects | nan |