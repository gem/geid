# 🌎 1980 M6.9 Irpinia earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1980 M6.9 Irpinia earthquake in southern Italy.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1980 Irpinia earthquake` struck southern Italy on November 23, 1980, at 19:34 local time, unleashing catastrophic destruction across the region. With a magnitude of 6.9 and a maximum Mercalli intensity (MMI) of X, the earthquake caused severe devastation. The epicenter was located near Conza della Campania, situated in the heart of Campania. Among the hardest-hit areas were the cities of Avellino, Sant'Angelo dei Lombardi, Lioni, and Balvano, which bore the brunt of the disaster. Tragically, the earthquake claimed approximately 3000 lives and left over 9000 people injured, with countless more displaced. The economic impact was staggering, amounting to an estimated $20000 million USD in losses. While landslides compounded the destruction in the region, there were no recorded instances of liquefaction, tsunamis or fires linked to the event. This earthquake remains a somber chapter in Italy’s history, ranking among its most devastating natural disasters.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1980 |
| Country | Italy |
| Region | Europe |
| Event Name | Irpinia 1980 |
| Local Date | 23/11/1980 |
| Local Time | 19:34:53 |
| Latitude (decimal degrees) | 40.914 |
| Longitude (decimal degrees) | 15.366 |
| Depth (km) | 10 |
| Mw | 6.9 |
| Max Intensity (MMI) | X |
| Fault mechanism | Normal |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0001ay4 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 0.31 g, observed at Sturno (Avellino). If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | ~3000 |
| Injured | ~9000 |
| Displaced population | ~280000 |
| Affected population | ~400000 |
| Affected units | nan |
| Damaged units | ~755000 Dwellings |
| Collapsed units | 75000-77000 Dwellings |
| Economic losses | 20000 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides |