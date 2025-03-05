# 🌎 1996 M6.8 Cyprus earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1996 M6.8 Cyprus earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1996 Cyprus earthquake`, with a magnitude of M6.8, struck on October 9, 1996, at approximately 11:10 local time. The earthquake had its moment magnitude (Mw) of 6.8 and its epicenter located off the southwestern coast of Cyprus, near Paphos, a region that experienced significant shaking. The earthquake produced a Modified Mercalli Intensity (MMI) of VI in the most affected areas, causing widespread damage in cities like Paphos and Limassol. The event resulted in around $20 million USD in economic losses and claimed 2 lives, with at least 5 injuries reported. While liquefaction and landslides were observed in localized areas, no tsunamis or fires were reported. The mainshock was preceded by foreshocks and followed by several aftershocks, which added to the anxiety of the affected communities. The earthquake remains a significant event in Cyprus's seismic history due to its impact on infrastructure and the local economy.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1996 |
| Country | Cyprus |
| Region | Europe |
| Event Name | Cyprus |
| Local Date | 09/10/1996 |
| Local Time | 11:10:52 |
| Latitude (decimal degrees) | 34.556 |
| Longitude (decimal degrees) | 32.126 |
| Depth (km) | 33 |
| Mw | 6.8 |
| Max Intensity (MMI) | VI |
| Fault mechanism | Strike-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0007r4u |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 0-2 |
| Injured | 0-5 |
| Displaced population | nan |
| Affected population | nan |
| Affected units | nan |
| Damaged units | 570.0 Buildings |
| Collapsed units | 70.0 Buildings |
| Economic losses | 20 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | nan |