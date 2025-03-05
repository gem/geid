# 🌎 2004 M5.1 Gardone earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2004 M5.1 Gardone earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2004 Gardone earthquake` struck northern Italy on November 24, 2004, at approximately 23:59 local time, with a moment magnitude (Mw) of 5.1. The earthquake registered a Maximum Mercalli Intensity (MMI) of VIII, signifying strong shaking that caused notable disruptions. The epicenter was located near Gardone Val Trompia in the Lombardy region, with the most severe impacts felt in nearby towns such as Sarezzo and other areas within the province of Brescia. The event caused significant structural damage, resulting in economic losses estimated at 215 million EUR, though no fatalities were reported. Minor injuries were documented, but the region avoided secondary hazards such as liquefaction, tsunamis, or substantial landslides, which could have worsened the situation. Despite its moderate magnitude, the earthquake served as a reminder of the seismic risks present in the region.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2004 |
| Country | Italy |
| Region | Europe |
| Event Name | Gardone 2004 |
| Local Date | 24/11/2004 |
| Local Time | 23:59:40 |
| Latitude (decimal degrees) | 45.626 |
| Longitude (decimal degrees) | 10.559 |
| Depth (km) | 17.2 |
| Mw | 5.1 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Reverse |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp000d94j |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | nan |
| Injured | nan |
| Displaced population | 2000-2300 |
| Affected population | nan |
| Affected units | 1200-4147 Buildings |
| Damaged units | 500 Buildings |
| Collapsed units | 40 Buildings |
| Economic losses | 215 M EUR |
| Insured losses | nan |
| Earthquake-triggered effects | nan |