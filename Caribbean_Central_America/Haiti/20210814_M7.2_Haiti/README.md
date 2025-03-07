# 🌎 2021 M7.2 Haiti earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2021 M7.2 Haiti earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2021 Haiti earthquake` struck on 14 August 2021, at 08:29 local time, with a magnitude of 7.2 on the Tiburon Peninsula in the Caribbean nation of Haiti. This powerful seismic event had a moment magnitude of 7.2 and reached a maximum intensity of VIII on the Modified Mercalli Intensity (MMI) scale. The epicenter was located near Petit-Trou-de-Nippes, approximately 150 kilometers (93 miles) west of the capital, Port-au-Prince. The earthquake primarily devastated the southwestern regions of Haiti, including the cities of Les Cayes, Jérémie, and their surrounding areas. This catastrophe resulted in over 2500 fatalities and left more than 12500 injured. Economic losses were estimated at $1600 million USD, with extensive destruction to buildings, infrastructure, and homes. In the aftermath, widespread landslides and instances of liquefaction were reported in the affected zones. Although no significant tsunamis were recorded, aftershocks exacerbated the difficulties faced by the impacted communities. While some fires were reported, their impact was minor compared to the widespread landslides and severe ground shaking.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2021 |
| Country | Haiti |
| Region | Caribbean Central America |
| Event Name | Haiti |
| Local Date | 14/08/2021 |
| Local Time | 08:29:08 |
| Latitude (decimal degrees) | 18.4335 |
| Longitude (decimal degrees) | -73.4822 |
| Depth (km) | 10 |
| Mw | 7.2 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Oblique-reverse |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | us6000f65h |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 2529-2577 |
| Injured | 12500-12763 |
| Displaced population | ~220000 |
| Affected population | 702763-800000 |
| Affected units | nan |
| Damaged units | 137000-137585 |
| Collapsed units | 53815-115000 |
| Economic losses | 1600 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides |