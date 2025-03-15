# 🌎 2014 M6.1 Kefalonia earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2014 M6.1 Kefalonia earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2014 Kefalonia earthquake` sequence began with a mainshock on January 26, 2014, at 15:55 local time, with a magnitude of 6.1. The epicenter was located near Kefalonia Island in the Ionian Sea, affecting cities like Lixouri and Argostoli. The earthquake caused significant damage with a Maximum Mercalli Intensity (MMI) of VIII, leading to around 175 million USD in economic losses and at least 23 injuries. Liquefaction was observed, but tsunamis and large landslides were not. The sequence continued with a strong aftershock on February 3, 2014, of magnitude 6.0, causing further damage, particularly to weakened structures, with aftershocks continuing for weeks.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2014 |
| Country | Greece |
| Region | Europe |
| Event Name | Kefalonia 2014 |
| Local Date | 26/01/2014 |
| Local Time | 13:55:42 |
| Latitude (decimal degrees) | 38.2082 |
| Longitude (decimal degrees) | 20.4528 |
| Depth (km) | 8 |
| Mw | 6.1 |
| Max Intensity (MMI) | VII |
| Fault mechanism | Strike-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usb000m8ch |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./20140126_M6.1_Kefalonia/4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./20140126_M6.1_Kefalonia/4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | nan |
| Injured | 0-23 |
| Displaced population | nan |
| Affected population | ~2000 |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | nan |
| Economic losses | 178 M USD |
| Insured losses | 8 M USD |
| Earthquake-triggered effects | nan |