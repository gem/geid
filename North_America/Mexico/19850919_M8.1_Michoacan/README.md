# 🌎 1985 M8.1 Mexico earthquake
[[_TOC_]]

# 📂 The repository

This repository hosts detailed information about the 1985 M8.1 Mexico earthquake.

Available information in the folders:

1. Impact
2. Ruptures
3. Recording stations
4. OpenQuake_gmfs


# 🚀 The earthquake at a glance 

The `1985 Mexico City earthquake` struck on September 19, 1985, at 07:17 AM local time, with a moment magnitude (Mw) of 8.1. Its epicenter was located off the coast of Michoacán, approximately 350 kilometers (220 miles) west of Mexico City. The earthquake reached a Modified Mercalli Intensity (MMI) of VII, causing widespread devastation across Mexico City and its surrounding regions. The most severely affected areas included downtown Mexico City and nearby neighborhoods, where the soft, lakebed soil amplified seismic waves, leading to catastrophic building collapses. Estimated economic losses ranged from $3000 to $8000 million USD, while the tragedy claimed at least 3100 lives, with some reports suggesting fatalities as high as 50000. The disaster was exacerbated by liquefaction, which triggered significant ground subsidence and structural failures. Although the earthquake generated several tsunamis, they were relatively minor. Landslides caused destruction in areas like Atenquique, Jalisco, and near Jala, Colima, while rockslides disrupted highways near Ixtapa. Sand blows and ground cracks were reported at Lazaro Cardenas. Numerous aftershocks, including a powerful 7.5 magnitude event on September 20, compounded the destruction and heightened fears. This earthquake remains one of Mexico's most devastating natural disasters.

| FIELD | DESCRIPTION |
|:-------|:-------------|
| Year | 1985 |
| Country | Mexico |
| Region | North America |
| Event Name | Mexico Michoacan  |
| Local Date | 19/09/1985 |
| Local Time | 07:17:49 |
| Latitude (decimal degrees) | 18.419 |
| Longitude (decimal degrees) | -102.468 |
| Depth (km) | 15 |
| Mw | 8.1 |
| Max Intensity (MMI) |  VII |
| Fault mechanism | Reverse |
| Tectonic region type | Subduction Intrerface |
| USGS event ID | usp0002jwe |

## Estimated and observed ground shaking

The folder [OpenQuake_gmfs](./OpenQuake_gmfs/) contains the input files required to generate ground motion fields, considering different rupture solutions and conditioning the ground shaking to the recording stations for the event, where available. The figures below present an example of the results, illustrating the median ground motion fields with and without conditioning. These results are based on the rupture and ground motion model that demonstrates the lowest nominal bias. The maximum recorded Peak Ground Acceleration (PGA) was [insert value here], observed at [insert location here]. If no seismic station data were available for the event, the generated ground motion fields are shown without conditioning to recording stations, as illustrated in the figures.

<img src="./4_OpenQuake_gmfs/median_gmf_stations_none.png" height="250">
<img src="./4_OpenQuake_gmfs/median_gmf_stations_seismic.png" height="250">

## ☄️ Consequences

The information collected for the consequences of the event and the corresponding references is available in the [Impact](./Impact) folder. When available, information at different geographical levels is provided considering the building damage, economic losses and human impact.

A summary of the main consequences of the event is available in the [earthquake_information.csv](./earthquake_information.csv) file:

| Attribute | Value |
|:-------|:-------------|
| Fatalities | 3192-50000 |
| Injured | 30000-150000 |
| Displaced population | nan |
| Affected population | 80600-2130204 |
| Affected units | nan |
| Damaged units | 3000-100000   |
| Collapsed units | 757-30000  |
| Economic losses | 3000-8000 M USD |
| Insured losses | nan |
| Earthquake-triggered effects | Landslides, Tsunami, Liquefaction |