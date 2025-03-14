# 🌎 2012 M6.2 Ahar-Varzaghan earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2012 M6.2 Ahar-Varzaghan earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `second earthquake in the 2012 East Azerbaijan sequence` occurred on August 11, 2012, with a moment magnitude of 6.2 and a maximum MMI of VIII. It struck shortly after the main shock, at 17:04 local time, with its epicenter near the same area of Ahar and Varzaghan. This aftershock further affected the already impacted regions, including Ahar and Varzaghan, exacerbating the damage and casualties. The event contributed to the overall toll, with additional fatalities and injuries reported. Like the first earthquake, landslides were observed, but there was no liquefaction, tsunamis, or fires. The aftershock continued to disrupt the region, with ongoing aftershocks felt in the following days.

| FIELD | DESCRIPTION |
|:------|:------------|
| Year | 2012 |
| Country | Iran |
| Region | Middle East |
| Event Name | Ahar-Varzaghan |
| Local Date | 11/08/2012 |
| Local Time | 17:04:00 |
| Latitude (decimal degrees) | 38.45 |
| Longitude (decimal degrees) | 46.75 |
| Depth (km) | 12 |
| Mw | 6.2 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Thrust |
| Tectonic region type | Active Crustal |
| USGS event ID | usp000jq5p |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 0.534g, observed at location (38.507°N, 46.64°E), corresponding to the Varzaqan region. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file.