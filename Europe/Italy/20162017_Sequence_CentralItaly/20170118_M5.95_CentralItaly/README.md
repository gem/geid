# 🌎 2017 M5.95 CentralItaly earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2017 M5.95 CentralItaly earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

A series of major earthquakes struck central Italy between the Marche and Umbria regions, beginning in August 2016 and continuing into 2017. The sequence commenced with a powerful tremor on 24 August 2016, registering a magnitude of 6.21. The epicenter, located near Norcia in the Umbria region, caused widespread devastation in cities such as Amatrice, Accumoli, and Arquata del Tronto. The earthquake resulted in over 296 fatalities, more than 360 injuries, and caused economic losses estimated at $5000 million USD. Significant landslides were reported in the mountainous areas surrounding the epicenter, although there were no instances of liquefaction or tsunamis.

On 26 October 2016, a second major earthquake struck with a magnitude of 6.09. The epicenter was near Visso in the Marche region, affecting towns such as Visso, Ussita, and Castelluccio. While this earthquake caused only 1 direct fatality, it inflicted further damage on already weakened structures from the earlier tremor. Landslides were again reported, though no liquefaction or tsunamis occurred. The economic losses from this event were estimated at $200 million USD, adding to the escalating toll of the series.

The largest earthquake in the sequence occurred on 30 October 2016, with a magnitude of 6.5. Once again, the epicenter was near Norcia in Umbria, affecting Norcia, Amatrice, Visso, and Preci. This earthquake resulted in 2 fatalities, approximately 20 injuries, and economic losses estimated at $200 million USD. Landslides were reported in the mountainous regions, though no liquefaction or tsunamis were observed.

The series culminated with a fourth significant earthquake on 18 January 2017. This tremor, with a magnitude of 5.95, struck near Montereale in the Abruzzo region, affecting cities such as Montereale, Campotosto, and Amatrice. The earthquake caused at least 29 fatalities and over 11 injuries, exacerbating the damage to already weakened infrastructure. Economic losses from this event were estimated at $18 million USD. Landslides were again reported, but there were no instances of liquefaction or tsunamis.

This sequence of earthquakes caused extensive damage to both historical and modern infrastructure, displacing thousands and further hindering recovery efforts. The continued seismic activity underscored the ongoing vulnerability of the region to earthquakes. The total fatalities and injuries from the series reached 328 and 380, respectively, with economic losses exceeding $5400 million USD.

| FIELD | DESCRIPTION |
|:------|:------------|
| Year | 2017 |
| Country | Italy |
| Region | Europe |
| Event Name | CentralItaly 2017 |
| Local Date | 18/01/2017 |
| Local Time | 10:14:10 |
| Latitude (decimal degrees) | 42.6012 |
| Longitude (decimal degrees) | 13.2268 |
| Depth (km) | 7 |
| Mw | 5.9 |
| Max Intensity (MMI) | VII |
| Fault mechanism | Normal |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | us10007twj |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file.