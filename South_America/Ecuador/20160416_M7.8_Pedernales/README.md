# 🌎 2016 M7.8 Pedernales earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2016 M7.8 Pedernales earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2016 Ecuador earthquake`, also known as the Pedernales Earthquake, occurred on April 16, 2016, at 06:58 local time, with a moment magnitude of Mw 7.8. The epicenter was located between the Pedernales and Cojimíes parishes of the Pedernales canton in the Manabí province on the Ecuadorian coast. The earthquake reached a maximum MMI of IX, indicating severe shaking and extensive damage in affected areas. The earthquake was strongly felt across multiple regions, particularly in Manabí, Esmeraldas, Guayas, Santa Elena, Los Ríos, Santo Domingo, El Oro, and northern highlands provinces such as Carchi, Imbabura, and Pichincha. In neighboring countries, it was also perceptible in Colombia and Peru, as well as in Venezuela and Panama. The earthquake caused extensive damage, with over 650 reported fatalities and over 6200 injuries. The economic losses were estimated to exceed 1300 million USD. Notably, the earthquake was preceded by a 4.8 magnitude foreshock, and it was followed by numerous aftershocks, with 11 aftershocks greater than magnitude 6 recorded as of December 31, 2017. The earthquake's impact included widespread liquefaction, landslides, and tsunami warnings, although the tsunami threat was later lifted. Despite significant damage, there were no major fires reported.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2016 |
| Country | Ecuador |
| Region | South America |
| Event Name | Pedernales 2016 |
| Local Date | 16/04/2016 |
| Local Time | 06:58:34 |
| Latitude (decimal degrees) | 0.31 |
| Longitude (decimal degrees) | -80.12 |
| Depth (km) | 17 |
| Mw | 7.8 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Reverse |
| Tectonic region type | Shallow upper crustal |
| USGS event ID | us20005j32 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 650-700  |
| Injured | 6274-230000 |
| Displaced population | 28678-386985 |
| Affected population | 383090-1000000000 |
| Affected units | nan |
| Damaged units | 9180-26672  |
| Collapsed units | 6998-36149  |
| Economic losses | 1300-3300 M USD |
| Insured losses | 560 M USD |
| Earthquake-triggered effects | Tsunami, Landslides |