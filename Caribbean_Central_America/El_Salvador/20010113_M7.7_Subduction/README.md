# 🌎 2001 M7.7 Subduction earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2001 M7.7 Subduction earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance

The `January 2001 El Salvador earthquake`, with a moment magnitude of 7.7, occurred on January 13 at 11:45 AM local time. Its epicenter was situated near the Pacific coast, approximately 90 kilometers south of the capital, San Salvador, within the region of La Libertad. The earthquake was strongly felt across El Salvador, particularly impacting the western and central regions, including the cities of San Salvador, Santa Tecla, and Sonsonate. The earthquake reached a maximum intensity of VIII on the Modified Mercalli Intensity (MMI) scale. It resulted in substantial destruction, with estimated economic losses exceeding $750 million USD. Tragically, between 650 and 1500 lives were lost, and over 3400 individuals sustained injuries. In addition to the initial event, numerous aftershocks, several exceeding a magnitude of 5.0, followed. Liquefaction, landslides, and fires were observed in various areas, and while no major tsunami was reported, some port workers did report witnessing tsunami waves. The earthquake was part of a sequence of seismic events, and although some foreshocks occurred, the primary event caused the most devastation.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2001 |
| Country | El Salvador |
| Region | Caribbean Central America |
| Event Name | Subduction 2001 |
| Local Date | 13/01/2001 |
| Local Time | 11:45:00 |
| Latitude (decimal degrees) | 12.83 |
| Longitude (decimal degrees) | -88.79 |
| Depth (km) | 39 |
| Mw | 7.7 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Normal |
| Tectonic region type | Subduction Intraslab |
| USGS event ID | usp000a7m5 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 0.601 (g) in the N-S direction, observed at the UCA Armenia  (13.744 N, 9.501 W) (Bommer_et_al_2002). If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 683-1500 |
| Injured | 3440-5565 |
| Displaced population | 45857-81486 |
| Affected population | 1160316-1692942 |
| Affected units | ~222773  |
| Damaged units | 84682-277953  |
| Collapsed units | 38628-108261  |
| Economic losses | 753-2000 M USD |
| Insured losses | 290 M USD |
| Earthquake-triggered effects | Landslides, Tsunami |