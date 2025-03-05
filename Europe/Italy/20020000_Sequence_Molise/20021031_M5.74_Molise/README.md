# 🌎 2002 M5.9 Molise earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2002 M5.9 Molise earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

On 31 October 2002, at 11:32 local time, the first of two earthquakes struck the Molise and Apulia regions of Italy, registering a magnitude of 5.9 Mw. This was followed by a second earthquake on 1 November 2002, at 16:09 local time, with a magnitude of 5.8 Mw. Both seismic events reached a maximum intensity of VII on the Modified Mercalli Intensity (MMI) scale. The epicenter of the first earthquake was near San Giuliano di Puglia, a small town that suffered the most severe impact. The tragedy was compounded by the collapse of the town’s primary school, resulting in devastating casualties. Among the victims were 26 schoolchildren and one teacher, with the majority of fatalities occurring in a single 4th Year classroom. In total, the event caused approximately 30 fatalities and left over 30 individuals injured. The economic losses from the earthquake were substantial, estimated at around 796 million USD, with widespread destruction of buildings and infrastructure throughout the affected regions. While no occurrences of liquefaction, tsunamis, or landslides were reported, the disaster underscored the vulnerability of older buildings, particularly schools, to seismic activity. This tragic event emphasized the urgent need for stricter earthquake-resistant construction standards, especially for public structures critical to the safety of communities.

| FIELD | DESCRIPTION |
|:------|:------------|
| Year | 2002 |
| Country | Italy |
| Region | Europe |
| Event Name | Molise 2002 |
| Local Date | 31/10/2002 |
| Local Time | 11:32:58 |
| Latitude (decimal degrees) | 41.789 |
| Longitude (decimal degrees) | 14.872 |
| Depth (km) | 10 |
| Mw | 5.9 |
| Max Intensity (MMI) | VII |
| Fault mechanism | Strike-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp000bfqg |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file.