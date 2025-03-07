# 🌎 1990 M6.95 Vrancea earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1990 M6.95 Vrancea earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1990 Vrancea earthquake` occurred on May 30, 1990, at 13:40 local time in Romania. The epicenter was located near the town of Focșani, in the Vrancea seismic region. This powerful earthquake, with a moment magnitude of 6.95, was felt in Bucharest, Bacău, and other areas in southeastern Romania, as well as in parts of neighboring Moldova. The earthquake caused significant damage, particularly in Bucharest, where many buildings were affected. The Maximum Intensity (MMI) was reported as VIII. While no tsunamis were observed, the event triggered landslides and liquefaction in some areas, and fires were reported due to ruptured gas lines.

| FIELD | DESCRIPTION |
|:------|:------------|
| Year | 1990 |
| Country | Romania |
| Region | Europe |
| Event Name | Vrancea 1990 |
| Local Date | 30/05/1990 |
| Local Time | 13:40 |
| Latitude (decimal degrees) | 45.841 |
| Longitude (decimal degrees) | 26.668 |
| Depth (km) | 89.3 |
| Mw | 6.95 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Reverse |
| Tectonic region type | Subduction Intraslab |
| USGS event ID | usp00049yk |



## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file.