# 🌎 1992 M6.68 Erzincan earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1992 M6.68 Erzincan earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The devastating `1992 Erzincan earthquake` struck eastern Turkey on March 13, 1992, at 20:18 local time. Measuring 6.68 on the moment magnitude scale and reaching a maximum intensity of VIII on the Mercalli scale, the temblor originated on the North Anatolian Fault mere kilometers from Erzincan's city center. This proximity resulted in widespread damage throughout the Erzincan district and province. This event resulted in over 540 fatalities and 2000 injuries. Economic losses exceeded 667 million USD. Four aftershocks, ranging from 5.0 to 6.1 Mw, were registered according to the Ministry of Public Works and Settlements.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1992 |
| Country | Turkey |
| Region | Europe |
| Event Name | Erzincan |
| Local Date | 13/03/1992 |
| Local Time | 20:18:39 |
| Latitude (decimal degrees) | 39.71 |
| Longitude (decimal degrees) | 39.605 |
| Depth (km) | 27.2 |
| Mw | 6.68 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Strike-slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp000547c |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 541-653 |
| Injured | 2000-3850 |
| Displaced population | 36000-95000 |
| Affected population | ~250000 |
| Affected units | 15042 Buildings |
| Damaged units | 9227 Buildings |
| Collapsed units | 5500-7007 Buildings |
| Economic losses | 667-750 M USD |
| Insured losses | 10.8 M USD |
| Earthquake-triggered effects | nan |