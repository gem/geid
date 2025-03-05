# 🌎 1997 M5.7 UmbriaMarche earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1997 M5.7 UmbriaMarche earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1997 Umbria and Marche earthquake` struck central Italy on September 26, with two significant tremors occurring on that day. The foreshock, rated at Mw 5.7, occurred at 02:33 local time, followed by the mainshock at 11:40 local time, measuring Mw 6.0. The epicenter of both events was near Annifo, and the tremors were assigned intensities of VIII for the foreshock and X for the mainshock on the Mercalli intensity scale. The towns most severely affected included Foligno, Nocera Umbra, and Assisi, where the iconic Basilica of St. Francis sustained significant damage. The earthquake led to over 11 fatalities and 100 injuries. It also resulted in economic losses exceeding 4500 million USD due to widespread destruction of buildings, infrastructure, and cultural heritage sites. The earthquake sequence, spanning from May 1997 to April 1998, included thousands of aftershocks, more than 30 of which exceeded a magnitude of 3.5. Fortunately, there were no reports of liquefaction, tsunamis, or major landslides. On October 14, 1997, an aftershock measuring Mw 5.5 and MMI VII struck the region, further exacerbating the damage caused by the initial tremors. This aftershock, occurring at 16:23 local time, affected the already weakened infrastructure in Foligno, Nocera Umbra, and Assisi, intensifying the physical and psychological toll on the local population, who were still grappling with the aftermath of the September earthquake.

| FIELD | DESCRIPTION |
|:------|:------------|
| Year | 1997 |
| Country | Italy |
| Region | Europe |
| Event Name | UmbriaMarche 1997 |
| Local Date | 26/09/1997 |
| Local Time | 02:33:12 |
| Latitude (decimal degrees) | 43.048 |
| Longitude (decimal degrees) | 12.879 |
| Depth (km) | 10 |
| Mw | 5.7 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Normal |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp000880n |



## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file.

