# 🌎 2014 M6 Kefalonia earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2014 M6 Kefalonia earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

A powerful aftershock of the 2014 Kefalonia earthquake, with a magnitude of 6.0 and a Maximum Mercalli Intensity (MMI) of VII, struck on February 3, 2014, following the mainshock. Occurring just over a week later, this aftershock had its epicenter near the same region, further impacting the already damaged cities of Lixouri and Argostoli. Like the mainshock, it caused significant structural damage to weakened buildings, increasing the economic losses. Fortunately, no additional fatalities were reported, but the continued seismic activity hindered the region's recovery. The aftershock, though slightly less intense than the mainshock, was felt strongly in the area and led to continued tremors, extending the period of disruption for local communities.

| FIELD | DESCRIPTION |
|:------|:------------|
| Year | 2014 |
| Country | Greece |
| Region | Europe |
| Event Name | Kefalonia 2014 |
| Local Date | 03/02/2014 |
| Local Time | 03:08:46 |
| Latitude (decimal degrees) | 38.2637 |
| Longitude (decimal degrees) | 20.3897 |
| Depth (km) | 5 |
| Mw | 6 |
| Max Intensity (MMI) | VII |
| Fault mechanism | Strike-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usc000mfuh |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file.