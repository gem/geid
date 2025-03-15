# 🌎 1981 M6.4 GulfofCorinth earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1981 M6.4 GulfofCorinth earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

On February 25, 1981, at 02:35:53 local time, a significant earthquake struck the Gulf of Corinth region in Greece. With a magnitude of 6.4 Mw, this event occurred at a depth of 33 km. The maximum intensity reached IX on the Mercalli Intensity (MMI) scale, indicating severe damage in the affected areas. This event was part of a broader sequence of earthquakes that impacted the region.

| FIELD | DESCRIPTION |
|:------|:------------|
| Year | 1981 |
| Country | Greece |
| Region | Europe |
| Event Name | GulfofCorinth 1981 |
| Local Date | 25/02/1981 |
| Local Time | 02:35:53 |
| Latitude (decimal degrees) | 38.125 |
| Longitude (decimal degrees) | 23.141 |
| Depth (km) | 33 |
| Mw | 6.4 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Normal |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0001ccv |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file.