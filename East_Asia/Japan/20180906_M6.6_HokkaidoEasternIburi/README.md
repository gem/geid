# 🌎 2018 M6.6 HokkaidoEasternIburi earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2018 M6.6 HokkaidoEasternIburi earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2018 Hokkaido Eastern Iburi earthquake` struck on September 6, 2018, at 03:08 local time, with a moment magnitude of Mw 6.6. The epicenter was located in the eastern Iburi region of Hokkaido, Japan, specifically in the town of Atsuma, within the Hokkaido Prefecture. The earthquake was felt across a wide region, including Sapporo, the largest city in Hokkaido, as well as other areas in the eastern and southern parts of the island. The earthquake's shaking reached an intensity of X on the Modified Mercalli Intensity (MMI) scale in the most affected areas. The event caused severe damage, with over 40 fatalities and more than 660 injuries reported. It triggered numerous landslides, particularly in mountainous areas, and caused debris flows, which compounded the destruction. Additionally, fires broke out at a petroleum facility and a thermal power plant, adding to the devastation. While no significant tsunamis were observed, liquefaction occurred in certain regions, further compromising infrastructure. Following the main shock, aftershocks continued, including a significant aftershock on February 21, 2019, with a magnitude of M_JMA 5.7, though it did not cause further major damage. The earthquake's economic impact was considerable, with reported losses totaling approximately 1250 million USD, marking it as one of the most destructive earthquakes in the region in recent years.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2018 |
| Country | Japan |
| Region | East Asia |
| Event Name | HokkaidoEasternIburi 2018 |
| Local Date | 06/09/2018 |
| Local Time | 03:08:58 |
| Latitude (decimal degrees) | 42.686 |
| Longitude (decimal degrees) | 141.929 |
| Depth (km) | 35 |
| Mw | 6.6 |
| Max Intensity (MMI) | X |
| Fault mechanism | Reverse |
| Tectonic region type | Active Shallow Crustal |
| USGS event ID | us2000h8ty |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 41-44 |
| Injured | 660-762 |
| Displaced population | 1989-12000 |
| Affected population | nan |
| Affected units | nan |
| Damaged units | 14170-15000  |
| Collapsed units | ~462  |
| Economic losses | 1250-2000 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides, Debris flows, fires |