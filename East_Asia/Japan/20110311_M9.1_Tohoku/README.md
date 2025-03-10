# 🌎 2011 M9.1 Tōhoku earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 2011 M9.1 Tōhoku earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `2011 Tōhoku undersea megathrust earthquake` occurred on 11 March 2011 at 14:46 local time, striking the Pacific Ocean approximately 72 km east of the Oshika Peninsula in the Tōhoku region of Japan, with a moment magnitude of Mw 9.1. The epicenter of the earthquake was located at a depth of approximately 32 km. This catastrophic event triggered massive tsunamis, causing extensive devastation along the coastlines, particularly in the regions of Miyagi, Fukushima, and Iwate. The earthquake reached a maximum intensity of VIII on the Modified Mercalli Intensity (MMI) scale, resulting in widespread destruction. The disaster led to over 13000 fatalities, with more than 5300 individuals reported as injured. Economic losses were estimated between $169000 and $309000 million USD, positioning it as one of the most costly natural disasters in history. Along with the earthquake and tsunami, significant landslides and extensive liquefaction were observed, especially in the affected coastal areas. The aftermath also saw numerous fires erupting, further exacerbating the damage. The event was followed by a series of aftershocks, including a powerful 7.9 magnitude aftershock, and was preceded by a smaller 7.2 magnitude foreshock. The catastrophe was further amplified by the Fukushima nuclear disaster, which led to the release of radioactive material and the mass evacuation of nearby residents.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 2011 |
| Country | Japan |
| Region | East Asia |
| Event Name | Tōhoku 2011 |
| Local Date | 11/03/2011 |
| Local Time | 14:46:18 |
| Latitude (decimal degrees) | 38.297 |
| Longitude (decimal degrees) | 142.373 |
| Depth (km) | 29 |
| Mw | 9.1 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Thrust/reverse |
| Tectonic region type | Subduction interface |
| USGS event ID | official20110311054624120 30 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 13135-22312 |
| Injured | 5314-6242 |
| Displaced population | 130927-500000 |
| Affected population | ~368820 |
| Affected units | >332395 |
| Damaged units | 144300-280920 |
| Collapsed units | 121778-400000 |
| Economic losses | 169000-309000 M USD |
| Insured losses | 37500 M USD |
| Earthquake-triggered effects | Tsunami |