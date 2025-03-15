# 🌎 1983 M5.6 Popayán earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1983 M5.6 Popayán earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1983 Popayán earthquake` occurred on 31 March 1983 at 08:12 AM local time in Popayán, Colombia. This earthquake, with a moment magnitude of 5.6, had a significant impact on the region, particularly in Popayán, known for its historic and architectural heritage. The epicenter of the earthquake was located southwest of Popayán at a depth of 12-15 kilometers. The earthquake caused widespread devastation, especially in Popayán, but also affected neighboring towns such as Cajete, Cajibío, Julumito, Figueroa, Rio Hondo, and Santa Ana. Over 13000 buildings were damaged, with more than 2470 houses collapsing. The earthquake resulted in over 200 fatalities, with more than 1200 people injured, and the total economic loss amounted to over $38 million USD. The destruction of local infrastructure, including power outages, water shortages, and communication disruptions, exacerbated the situation. In the aftermath, public health concerns, particularly related to stomach and respiratory issues, began to emerge among survivors. In addition to structural damage, landslides and ground cracks were reported in several affected regions. There were no tsunamis or significant fires, but the area experienced persistent aftershocks that continued until the end of April 1983. The earthquake’s intensity was classified as MMI VIII, highlighting its devastating effects on the region. As a result of the widespread damage, new regulations were enacted to require earthquake-resistant building materials in regions at risk of seismic activity.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1983 |
| Country | Colombia |
| Region | South America |
| Event Name | Popayán 1983  |
| Local Date | 31/03/1983 |
| Local Time | 08:12:00 |
| Latitude (decimal degrees) | 2.364 |
| Longitude (decimal degrees) | -76.696 |
| Depth (km) | 15 |
| Mw | 5.6 |
| Max Intensity (MMI) | VIII |
| Fault mechanism | Strike-Slip |
| Tectonic region type | Active Shallow Crust |
| USGS event ID | usp0001u34 |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_all.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 200-350  |
| Injured | 1200-7500 |
| Displaced population | 10000-30000 |
| Affected population | 10000-36200  |
| Affected units | nan |
| Damaged units | 13650-14000  |
| Collapsed units | 2470-4964  |
| Economic losses | 38-50 M USD |
| Insured losses | 4 M USD |
| Earthquake-triggered effects | Landslides |