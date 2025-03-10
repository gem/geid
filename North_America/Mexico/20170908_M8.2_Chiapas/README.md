# 🌎 2017 M8.2 Chiapas earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2017 M8.2 Chiapas earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2017 Chiapas earthquake` struck the southern coast of Mexico on September 8, 2017, at 11:49 PM local time, registering a moment magnitude (Mw) of 8.2. This event stands as one of the most powerful earthquakes in Mexico's history. The epicenter was located in the Gulf of Tehuantepec, approximately 87 km southwest of Pijijiapan, Chiapas. The earthquake was strongly felt across southern Mexico, with a peak Modified Mercalli Intensity (MMI) of VII reported in the hardest-hit regions, including Chiapas and Oaxaca. The disaster triggered widespread liquefaction and landslides, particularly in coastal and mountainous areas. A minor tsunami followed, producing waves up to 1.75 meters, though no significant fires were recorded. The earthquake resulted in 61 fatalities and left 250 injured, with estimated economic losses exceeding $2300 million USD, as extensive damage was inflicted on buildings, infrastructure, and communities. Preceded by minor foreshocks and followed by numerous aftershocks, including one measuring 6.1, this catastrophic event left an indelible mark on the region.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2017 |
| Country | Mexico |
| Region | North America |
| Event Name | Chiapas 2017 |
| Local Date | 08/09/2017 |
| Local Time | 23:49:17 |
| Latitude (decimal degrees) | 14.761 |
| Longitude (decimal degrees) | -94.103 |
| Depth (km) | 45.9 |
| Mw | 8.2 |
| Max Intensity (MMI) | VII |
| Fault mechanism | Normal |
| Tectonic region type | Subduction Intraslab |
| USGS event ID | us2000ahv0 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 61-102 |
| Injured | 250-900 |
| Displaced population | ~458392 |
| Affected population | 1200250-2500000  |
| Affected units | nan |
| Damaged units | 94027-209863  |
| Collapsed units | 41000-56504  |
| Economic losses | 2300-4000 M USD |
| Insured losses | 14000-2000 M MXN |
| Earthquake-triggered effects | Tsunami, Landslide |