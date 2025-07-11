# Metadata

[[_TOC_]]

# Scope
The following sections present the parameters and definitions used in the different files of the database.

They include:

- The `earthquake_information.csv` in the home folder of each event
- The impact files at different administrative levels (e.g., `Impact_All_ID_0.csv`)
- The global summary files available in the [World](./World/) folder

# Earthquake Characteristics

- **Year:**: Year of phenomenon occurrence.

- **Country:** Country (or countries) impacted by the event.

- **Region:** Name of the region or areas most affected by the event (it can include multiple countries).

- **Event Name:**  The name of the event. \*

- **Local Date:** Date of occurrence at the location of the even. Format: `DD/MM/YYYY`.

- **Local Time:** Local time of occurrence. \* Format: `HH/MM/SS`.

- **Latitude (decimal degrees):** Latitude of the epicenter. \*

- **Longitude (decimal degrees):** Longitude of the epicenter. \*

- **Depth (km):** Hypocentral depth. \*

- **Mw:** Moment magnitude. \*

- **Max Intensity (MMI):** Modified Mercalli Intensity (MMI). \*

- **Fault mechanisim:** Faulting motion that produced the earthquake: strike-slip fault, normal fault, thrust fault (reverse fault).

- **Tectonic region type:** Tectonic features associated to the event. For example, active shallow crust, subduction interface, subduction intraslab, stable continental.

- **USGS event ID:** Link to the USGS event page.

- **Wikipedia page:** Link to the Wikipedia event page.

> \* Source of information can be the USGS or local sources when reporting more detailed information.


# Impact data

## General details


- **ID_0:** National level identifier, equivalent to the [ISO3166 alpha-3 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) for the country (e.g., AFG, COL).

- **NAME_0:** Name for the country, following [GEM Global Risk Model](https://github.com/gem/global_exposure_model#-region-and-country-list) convention. Spaces should be used rather than an underscore.

- **ID_n:** Identifier for the country divisions at administrative level n.

- **NAME_n:** Name of the country divisions at administrative level n.

- **INDUCED_EFFECTS:** Other phenomena that occurred as a result of the earthquake: Tsunamis, Landslides, Liquefaction, Avalanche, Floods, Fire, Eruptions, Stampedes, etc.

- **FLAG:** When _True_, it highlights that the reported values are not in agreement with the consequences reported by other references.

- **REFERENCE:** Source of the reported information.

- **COMMENTS:** Comments and noteworthy details.

- Optional information

	- **TAXONOMY:** Description of the physical characteristics and usage of the building/housing as indicated in the source of reference.

	- **GEM_TAXONOMY:** String identifying the physical characteristics and usage of the buildings according to [GEM Building Taxonomy](https://platform.openquake.org/taxtweb/).

	- **OCCUPANCY:** The type of activity (function) that the building is primarily used for (e.g., Residential, Commercial, Education, etc).

## Human impact

- **AFFECTED_POPULATION:** Number of people reported as affected due to the earthquake occurance and its secondary effects. No differentiation regarding the level of affectance is included. The metric reports the population affected from immediate impacts, such as deaths, injuries, being homeless, being displaced, or being evacuated because of building damaged, as well as population affected by induced earthquake effects, such as landslides, tsunamis or burns from fires.

- **DISPLACED_POPULATION:** Number of people reported as displaced. This number could be unspecified and could consist of displaced, relocated, or evacuated due to the significant damage to their homes as well as the number of homeless and sheltered. If there are some sources in which the number of relocated, evacuated, homeless, and sheltered have been presented separately, adding the extra columns with the related headers is recommended.

- **FATALITIES:** Number of people that died due to the earthquake direct or indirect effects (such as ground shaking, tsunamis, landslides, etc. 
`Fatalities = Direct deaths (shaking) + indirect deaths (due to tsunamis, landslide, heart attack,...) + Missing`

- **FATALITIES_GROUND_SHAKING:** Number of people that died directly due to the ground shaking.

- **INJURIES:** Number of people physically injured due to the earthquake occurrence (directly or indirectly). It considers all levels of injuries.<br>
`Injured = Direct injuries + indirect injuries`.<br>


## Detailed human impact data

When detailed information is available regarding human impact (e.g., injury levels or cause of injury):

- Create a new file that with the additional details at the corresponding administrative level.
- The file should be called `Impact_Human_ID_n.csv`, where n stands for the administrative level n.
- The file should include the columns already indicated in Impact_All_ID_0.

For **injury levels**, report the injury levels as indicated in the source of reference. In addition, consider the following levels:

- **INJURIES_LIGHT:** Number of injured people who demand medical aid from physicians, such as bandages or observation. Note that those injuries that can be self-treated are not considered.
- **INJURIES_SEVERE:** Number of injured people needing medical aid from physicians to a greater extent as well as requiring medical technology such as x-rays or surgery, such as facial wounds, fractures, burns (third-degree or second-degree), dehydration, or exposure.
- **INJURIES_CRITICAL:** Number of injured people needing adequate and instantaneous medical aid from physicians to save them and avoid losing their life, such as internal head trauma, brain damage, spinal column injuries, uncontrolled bleeding, punctured organ, and internal organ failures due to crushing.

For **DISPLACED_POPULATION**, report the details as indicated in the source of reference. In addition, consider the following levels:

- **HOMELESS:** Number of people who are reported as having been homeless due to heavy damage or destruction of their houses as well. Some of these people may be accommodated in shelters, in hotels/rentals, or with family/friends.
- **SHELTERED:** Number of people who are reported as having been accommodated by national authorities or other organizations.

In addition, is possible to specify

- **CAUSE_OF_INJURY/DEATH:** Specific reasons why people were injured or died (e.g., chimeny collapse, tsunami, landslides).

## Building impact

- **AFFECTED_UNITS:** Number of units (e.g., buildings) reported as affected and the level of damage is unspecified.

- **DAMAGED_UNITS:** Number of units (e.g., buildings) that reported any level of damage due to the earthquake and its secondary effects, but is not considered destroyed.

>**Note**
> The number of destroyed units is not considered within `DAMAGED_UNITS`, since most reports separate damaged and destroyed buildings

- **DESTROYED_UNITS:** Number of units (e.g., buildings) reported as totally destroyed or collapsed.

- **UNIT_TYPES:** Type of damaged units: _Buildings_, _Dwellings_, or _Households_.

## Detailed building impact data

When detailed information is available regarding building impact, i.e. damage states or damage description:

- Create a new file that with the additional details at the corresponding administrative level.
- The file should be called `Impact_Buildings_ID_n.csv`, where n stands for the administrative level n.

Report the level of damage as indicated in the source of reference. In addition, consider the damage states suggested by [EMS-98](https://www.franceseisme.fr/EMS98_Original_english.pdf): 

- **DS1_SLIGHT:** No damage in structural components and negligible to slight damage in non-structural components.
- **DS2_MODERATE:** Slight damage in structural components and moderate damage in non-structural components.
- **DS3_EXTENSIVE:** Moderate damage in structural components and substantial to heavy damage in non-structural components.
- **DS4_COMPLETE:** Substantial to heavy damage in structural components and very heavy damage in non-structural components.
- **DS5_COLLAPSE:** Destruction. Total or near total collapse.

In addition, is possible to specify

- **CAUSE_OF_DAMAGE:** Specific reasons why buildings were damaged (e.g., tsunami, landslides).

## Economic impact

- **ECONOMIC_LOSSES:** Economic losses reported after the earthquake (it might include or not indirect losses). 
Currency units are based on the source of reference and reported in the `CURRENCY` column. Values unadjusted for inflation.

- **RECONSTRUCTION_COST:** Economic resources invested in reconstructing the physical damage caused by the earthquake and its induced effects. Values unadjusted for inflation.

- **INSURED_LOSSES:** Economic losses covered by insurance companies. Currency units based on the source of 
reference and reported in the `CURRENCY` column. Values unadjusted for inflation.

- **CURRENCY:** Currency units for economic impact, following the [ISO3 code](https://www.iso.org/iso-4217-currency-codes.html) (e.g., USD, EUR, etc).

_Note: In the dataset, blank cells indicate missing or unavailable information and they should not be interpreted as zero. These values reflect cases where the original data source did not report a value. 