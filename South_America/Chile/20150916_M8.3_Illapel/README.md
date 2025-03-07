# 🌎 2015 M8.3 Illapel earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2015 M8.3 Illapel earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2015 Illapel earthquake` occurred off the coast of Chile on September 16, 2015, at 19:54 local time, with a moment magnitude of 8.3. The epicenter was located approximately 46 km offshore from Illapel in the Coquimbo region. The earthquake resulted in significant damage, particularly in coastal cities such as Coquimbo, Tongoy, and La Serena, as well as the capital, Santiago, where the event was felt with an intensity of VIII on the Mercalli Intensity scale. Tragically, the earthquake claimed the lives of 13 individuals, with over 14 people injured. Furthermore, the event triggered a powerful tsunami causing widespread flooding and extensive property damage along the Chilean coastline. In Coquimbo, large fishing vessels were swept into the streets. The earthquake also induced liquefaction, landslides, and rockfalls, severely impacting infrastructure such as roads, bridges, and buildings. Following the main shock, a series of aftershocks ensued, including a significant 7.0 magnitude aftershock that struck just 24 minutes later. Economically, the disaster had a profound impact, with damage estimated at over 600 million USD, particularly in the Coquimbo region, where thousands of buildings were destroyed. The combination of intense ground shaking and the resulting tsunami makes the 2015 Illapel earthquake one of Chile's most complex and devastating seismic events.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2015 |
| Country | Chile |
| Region | South America |
| Event Name | Illapel 2015 |
| Local Date | 16/09/2015 |
| Local Time | 19:54:33 |
| Latitude (decimal degrees) | -31.5729 |
| Longitude (decimal degrees) | -71.6744 |
| Depth (km) | 22.44 |
| Mw | 8.3 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Reverse |
| Tectonic region type | Subduction Intraslab |
| USGS event ID | us20003k7a |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 13-19 |
| Injured | 14-34 |
| Displaced population | >16646 |
| Affected population | 688-681499 |
| Affected units | nan |
| Damaged units | 1791-10685  |
| Collapsed units | 1069-2872  |
| Economic losses | 600-900 M USD |
| Insured losses | 350 M USD |
| Earthquake-triggered effects | Tsunami, Landslides |