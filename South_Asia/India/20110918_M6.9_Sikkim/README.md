# 🌎 2011 M6.9 Sikkim earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2011 M6.9 Sikkim earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2011 Sikkim earthquake`, also referred to as the 2011 Himalayan earthquake, occurred on September 18, 2011, at 18:10 local time, registering a moment magnitude of 6.9. Its epicenter was located near the Kanchenjunga Conservation Area, situated along the border between India and Nepal, at a depth of 50 km. The event reached a Maximum Modified Mercalli Intensity (MMI) of VIII, signifying intense shaking across the affected regions. The earthquake predominantly impacted northeastern India, Nepal, Bhutan, and southern Tibet, with the most significant damage reported in Sikkim, Darjeeling, and portions of West Bengal. The disaster resulted in an estimated 111-112 fatalities and over 177 injuries, with economic losses approximated at 22.3 million USD. While no tsunamis or fires were reported, the event triggered widespread landslides and mudslides, particularly in the mountainous areas, causing severe disruptions to infrastructure. Multiple aftershocks followed the main earthquake, exacerbating damage in already affected regions, while no significant foreshocks were recorded prior to the primary seismic event.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2011 |
| Country | India |
| Region | South Asia |
| Event Name | Sikkim 2011 |
| Local Date | 18/09/2011 |
| Local Time | 18:10:51 |
| Latitude (decimal degrees) | 27.73 |
| Longitude (decimal degrees) | 88.155 |
| Depth (km) | 50 |
| Mw | 6.9 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Strike-slip |
| Tectonic region type | Subduction intraslab |
| USGS event ID | usp000j88b |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 111-112 |
| Injured | 177-710 |
| Displaced population | 5000-7882 |
| Affected population | ~575200 |
| Affected units | nan |
| Damaged units | 34000-39000 |
| Collapsed units | nan |
| Economic losses | 22.3 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides, mudslides |