# 🌎 1990 M6.31 Vrancea earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1990 M6.31 Vrancea earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1990 Vrancea earthquake` was part of a sequence of seismic events in the region. It occurred on May 31, 1990, at 03:17 local time, with a moment magnitude of 6.31. This earthquake was the second shock in the sequence, following a larger initial shock on May 30, 1990. The epicenter of the earthquake was located in the Vrancea region of southeastern Romania. The most affected areas were Bucharest, Ploiești, and surrounding regions, where significant damage occurred. The earthquake's shaking reached V on the Modified Mercalli Intensity (MMI) scale. While no tsunamis or fires were observed, landslides were noted in some areas, particularly in the mountainous regions. Aftershocks followed the main event, contributing to further damage, but no foreshocks were recorded prior to the earthquake.

| FIELD | DESCRIPTION |
|:------|:------------|
| Year | 1990 |
| Country | Romania |
| Region | Europe |
| Event Name | Vrancea 1990 |
| Local Date | 31/05/1990 |
| Local Time | 03:17 |
| Latitude (decimal degrees) | 45.811 |
| Longitude (decimal degrees) | 26.769 |
| Depth (km) | 88.2 |
| Mw | 6.31 |
| Max Intensity (MMI) | V |
| Fault mechanism | Reverse |
| Tectonic region type | Subduction Intraslab |
| USGS event ID | usp00049za |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file.