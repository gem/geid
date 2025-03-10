# 🌎 2020 M7.4 Oaxaca earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2020 M7.4 Oaxaca earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The powerful `2020 Oaxaca earthquake` struck the Mexican state of Oaxaca on June 23, 2020, at 10:29 local time, with a moment magnitude of 7.4. Its epicenter was located near the town of La Crucecita, approximately 23 kilometers south of Santa María Huatulco, in the Pacific coastal region. The earthquake generated severe ground shaking, reaching a maximum Modified Mercalli Intensity (MMI) of VIII. The impact was most pronounced in Oaxaca, though its effects were felt as far as Mexico City, over 500 kilometers away. The disaster resulted in at least 10 fatalities, 23 injuries, and widespread structural damage, with estimated economic losses exceeding $75 million USD. Landslides disrupted transportation in hilly areas, while localized liquefaction was reported in low-lying regions. Although no significant tsunamis or fires occurred, a tsunami warning was briefly issued along the Pacific coast. The earthquake was preceded by minor foreshocks and followed by numerous aftershocks, including one with a magnitude of 5.5, compounding the damage in already affected areas.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2020 |
| Country | Mexico |
| Region | North America |
| Event Name | Oaxaca 2020 |
| Local Date | 23/06/2020 |
| Local Time | 10:29:03 |
| Latitude (decimal degrees) | 15.784 |
| Longitude (decimal degrees) | -96.12 |
| Depth (km) | 22.6 |
| Mw | 7.4 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Reverse |
| Tectonic region type | Subduction Interface |
| USGS event ID | us6000ah9t |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~10 |
| Injured | 23-25 |
| Displaced population | ~139 |
| Affected population | ~24393 |
| Affected units | >8000  |
| Damaged units | 8123-10285  |
| Collapsed units | nan |
| Economic losses | 75 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Tsunami, Landslides |