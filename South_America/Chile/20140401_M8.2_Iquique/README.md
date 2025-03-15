# 🌎 2014 M8.2 Iquique earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2014 M8.2 Iquique earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2014 Iquique earthquake` occurred off the coast of Chile on April 1st at 20:46 local time, registering a moment magnitude of 8.2. The epicenter was situated approximately 95 km northwest of Iquique. The earthquake's intensity, as measured by the Modified Mercalli Intensity (MMI) scale, was VIII, with the strongest shaking experienced in areas near the epicenter, particularly in Iquique and Alto Hospicio. This major seismic event followed a series of foreshocks, including an Mw 6.7 earthquake on March 16, and triggered a tsunami with waves reaching up to 2.11 meters, impacting the coastal cities of Iquique, Pisagua, and Arica. The most affected regions included the communes of Alto Hospicio and Iquique within the Arica y Parinacota, Tarapacá, and Antofagasta regions. The earthquake resulted in more than 6 fatalities and over 28 injuries, alongside widespread power outages and significant infrastructure damage. Economic losses were estimated at approximately 100 million USD, though these were mitigated by the distance from the epicenter and the improved structural performance of buildings compared to the 2010 Maule earthquake. While liquefaction and landslides were not widely observed, the tsunami effects were notable. Following the mainshock, numerous aftershocks occurred, including several with magnitudes above Mw 6.0.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2014 |
| Country | Chile |
| Region | South America |
| Event Name | Iquique 2014 |
| Local Date | 01/04/2014 |
| Local Time | 20:46:50 |
| Latitude (decimal degrees) | -19.572 |
| Longitude (decimal degrees) | -70.908 |
| Depth (km) | 38.9 |
| Mw | 8.2 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Reverse |
| Tectonic region type | Subduction Interface |
| USGS event ID | usc000nzvd |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 6-7 |
| Injured | 28-200 |
| Displaced population | nan |
| Affected population | ~513387 |
| Affected units | nan |
| Damaged units | 2500-9780  |
| Collapsed units | nan |
| Economic losses | 100 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Tsunami, Landslide |