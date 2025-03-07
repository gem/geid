# 🌎 1981 M6.7 GulfofCorinth earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1981 M6.7 GulfofCorinth earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

On February 24, 1981, at 20:53:38 local time, the Gulf of Corinth region in Greece was struck by a powerful earthquake with a magnitude of 6.7 Mw. The epicenter was located at a depth of 33 km. The event reached a maximum intensity of IX on the Mercalli Intensity (MMI) scale, indicating severe damage in the affected areas. This earthquake was part of a sequence that caused widespread destruction in the Corinth–Athens region, resulting in the collapse of nearly 8000 buildings and leading to 20–22 reported fatalities. 

| FIELD | DESCRIPTION |
|:------|:------------|
| Year | 1981 |
| Country | Greece |
| Region | Europe |
| Event Name | GulfofCorinth 1981 |
| Local Date | 24/02/1981 |
| Local Time | 20:53:38 |
| Latitude (decimal degrees) | 38.222 |
| Longitude (decimal degrees) | 22.934 |
| Depth (km) | 33 |
| Mw | 6.7 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Normal |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0001ccb |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file.