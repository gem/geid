# 🌎 2016 Central Italy earthquake sequence
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2016 Central Italy earthquake sequence.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

A series of major earthquakes struck central Italy between the Marche and Umbria regions, beginning in August 2016 and continuing into 2017. The sequence commenced with a powerful tremor on 24 August 2016, registering a magnitude of 6.0. The epicenter, located near Norcia in the Umbria region, caused widespread devastation in cities such as Amatrice, Accumoli, and Arquata del Tronto. The earthquake resulted in over 296 fatalities, more than 368 injuries, and caused economic losses estimated at $5000 million USD. Significant landslides were reported in the mountainous areas surrounding the epicenter, although there were no instances of liquefaction, tsunamis or fires.

On 26 October 2016, a second major earthquake struck with a magnitude of 5.9. The epicenter was near Visso in the Marche region, affecting towns such as Visso, Ussita, and Castelluccio. While this earthquake did not cause direct victimes, it inflicted further damage on already weakened structures from the earlier tremor. Landslides were again reported, though no liquefaction, tsunamis or fires occurred. The economic losses from this event were estimated at $200 million USD, adding to the escalating toll of the series.

The largest earthquake in the sequence occurred on 30 October 2016, with a magnitude of 6.6. Once again, the epicenter was near Norcia in Umbria, affecting Norcia, Amatrice, Visso, and Preci. This earthquake resulted in approximately 20 injuries, and thousands of displaced people. Landslides were reported in the mountainous regions, though no liquefaction, tsunamis or fires were observed.

The series culminated with a fourth significant earthquake on 18 January 2017. This tremor, with a magnitude of 5.5, struck near Montereale in the Abruzzo region, affecting cities such as Montereale, Campotosto, and Amatrice. The earthquake caused 5 direct fatalities. This series of earthquakes, in combination with a winter storm, appeared to have triggered an avalanche near Farindola that destroyed a hotel, killing 29 and injuring 11. Economic losses from this event were estimated at $18 million USD. Landslides were again reported, but there were no instances of liquefaction, tsunamis or fires.

This sequence of earthquakes caused extensive damage to both historical and modern infrastructure, displacing thousands and further hindering recovery efforts. The continued seismic activity underscored the ongoing vulnerability of the region to earthquakes. Ground shaking caused 301 fatalities and around 400 injuries, with economic losses exceeding $5400 million USD.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2016 |
| Country | Italy |
| Region | Europe |
| Event Name | CentralItaly |
| Local Date | 24/08/2016 |
| Local Time | 01:36:32 |
| Latitude (decimal degrees) | 42.723 |
| Longitude (decimal degrees) | 13.1877 |
| Depth (km) | 4.44 |
| Mw | 6.0 |
| Max Intensity (MMI) | IX |
| Fault mechanism | Normal |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | us10006g7d |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was 1.42 g, observed at Castelsantangelo sul Nera (Macerata), on 26 October 2016. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./20160824_M6.21_CentralItaly/4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./20160824_M6.21_CentralItaly/4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 301-304 |
| Injured | 410-440 |
| Displaced population | 28000-100000 |
| Affected population | nan |
| Affected units | nan |
| Damaged units | nan |
| Collapsed units | nan |
| Economic losses | 5400 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides |