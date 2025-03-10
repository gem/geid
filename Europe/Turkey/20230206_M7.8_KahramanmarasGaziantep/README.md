# 🌎 2023 M7.8 CentralTurkey earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2023 M7.8 CentralTurkey earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The devastating `2023 Central Turkey earthquake` struck central and southern Turkey, and northern and western Syria on February 6, 2023, at 4:17 AM local time. Measuring 7.8 on the moment magnitude scale, it was the strongest earthquake in Turkey since 1939. The epicenter, located near Gaziantep, experienced a maximum intensity of XII on the Mercalli scale. A powerful aftershock of magnitude 7.7 followed later that day. Widespread damage and a tragic death toll exceeding 53000 were reported across the region. This event, one of the strongest earthquakes ever recorded in the Levant, left over 114000 injuries and caused immense economic losses exceeding $100000 million in Turkey alone. The international community responded with a massive rescue effort, highlighting the global impact of this disaster.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2023 |
| Country | Turkey |
| Region | Europe |
| Event Name | CentralTurkey 2023 |
| Local Date | 06/02/2023 |
| Local Time | 04:17:34 |
| Latitude (decimal degrees) | 37.2199 |
| Longitude (decimal degrees) | 37.0189 |
| Depth (km) | 10 |
| Mw | 7.8 |
| Max Intensity (MMI) | XII |
| Fault mechanism | Strike-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | us6000jllz |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 53227-55690 |
| Injured | 114770-129500 |
| Displaced population | ~1500000 |
| Affected population | nan |
| Affected units | ~140000  |
| Damaged units | ~42500  |
| Collapsed units | ~15910  |
| Economic losses | 103000 M USD |
| Insured losses | 1000 M USD |
| Earthquake-triggered effects | nan |