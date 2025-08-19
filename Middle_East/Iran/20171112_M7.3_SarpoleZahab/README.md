# 🌎 2017 M7.3 Sarpole-Zahab earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2017 M7.3 Sarpole-Zahab earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2017 Sarpole-Zahab earthquake` in Iran occurred on November 12, with a moment magnitude of 7.3 and a maximum intensity of IX on the Modified Mercalli Intensity (MMI) scale. The earthquake struck at 21:48 local time, with its epicenter near the town of Sarpole-Zahab in Kermanshah province, close to the Iran-Iraq border. The most affected areas included Kermanshah province, particularly the cities of Sarpole-Zahab and Qasr-e Shirin, along with parts of Iraq. The disaster caused extensive damage, resulting in over 430 fatalities and more than 6600 injuries. Economic losses were estimated to exceed $80 million USD. In addition to the main shock, widespread landslides further exacerbated the devastation, though no tsunamis, fires, or liquefaction were reported. Aftershocks continued to impact the region, compounding the challenges faced by affected communities.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2017 |
| Country | Iran |
| Region | Middle East |
| Event Name | Sarpole-Zahab |
| Local Date | 12/11/2017 |
| Local Time | 21:48:16 |
| Latitude (decimal degrees) | 34.81 |
| Longitude (decimal degrees) | 45.91 |
| Depth (km) | 18.1 |
| Mw | 7.3 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Thrust |
| Tectonic region type | Active Crustal |
| USGS event ID | us2000bmcg |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 0.69g, observed at location (34.46°N, 45.87°E), corresponding to the Sarpole Zahab region in western Iran. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 436-660 |
| Injured | 6603-15249 |
| Displaced population | 7000-200000 |
| Affected population | 200000-1645450 |
| Affected units | nan |
| Damaged units | 14500-90000  |
| Collapsed units | 2000-18000  |
| Economic losses | 84-750 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides, Rockfalls, Liquefaction |