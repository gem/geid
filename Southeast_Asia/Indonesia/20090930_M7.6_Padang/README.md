# 🌎 2009 M7.6 Padang  earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2011 M6.9 Sikkim earthquake in India.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2009 Sumatra earthquake`, which struck Indonesia on September 30, 2009, had a magnitude of 7.6. Its epicentre was located near the coast of Sumatra, approximately 50 kilometers from the city of Padang. Occurring at 17:16 local time, the earthquake caused extensive damage, particularly in Padang and the surrounding regions of West Sumatra. The shaking was recorded at a maximum intensity of VIII on the Modified Mercalli Intensity (MMI) scale. The economic losses from the disaster were substantial, estimated at over $2200 million USD. Tragically, more than 1100 fatalities were reported, along with over 1200 injuries. The earthquake triggered landslides, especially in the hilly areas around Padang, and caused severe damage to infrastructure. Liquefaction was observed in several locations, further worsening the devastation. Although no significant tsunamis were generated, the aftershocks and fires contributed to additional destruction in the affected areas.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2009 |
| Country | Indonesia |
| Region | Southeast Asia |
| Event Name | Padang  |
| Local Date | 30/09/2009 |
| Local Time | 17:16:00 |
| Latitude (decimal degrees) | -0.72 |
| Longitude (decimal degrees) | 99.867 |
| Depth (km) | 81 |
| Mw | 7.6 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Oblique reverse |
| Tectonic region type | Subduction intraslab  |
| USGS event ID | usp000h237 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 0.3g. Since this value was measured in an area with stiff soil, it is likely that the shaking in Padang, which sits on alluvial deposits, was stronger. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 1100-1195 |
| Injured | 1214-2181 |
| Displaced population | 451000-1250000 |
| Affected population | 1200000-2500000 |
| Affected units | nan |
| Damaged units | 144000-181665 Buildings |
| Collapsed units | 181665 Buildings |
| Economic losses | 2200-2300 M USD |
| Insured losses | 100 M USD |
| Earthquake-triggered effects | Landslides, Tsunami |