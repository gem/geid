# 🤓 CONTRIBUTE TO THE Global Earthquake Impact Database 

You can contribute by improving the information available for a given event(s), or you can include a new one.

To help with this process, the [src](./src/) folder contains Jupyter notebooks that facilitate both the collection and formatting of event information.


🔁 Two Ways to Contribute

1. Via GitHub (Recommended for Users Familiar with Git)
If you're comfortable using GitHub:

    1. Fork this repository by clicking the "Fork" button at the top right of the page.
    2. Clone your fork to your computer:
    
          >git clone "URL-for-GitHub-repository"

    3. Create a new branch for your contribution:

          >git checkout -b add-new-event

    4. Make your changes to the appropriate .csv files or notebooks. Please follow the structure and standards described in this repository.

    5. Commit and push your changes:
    
          >git commit -am "Add data for [Event Name]"
          >git push origin add-new-event

    6. Open a Pull Request (PR) on GitHub and provide a brief description of your contribution.

     📘 New to GitHub? See:

     GitHub Docs: [Fork Repo](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

     GitHub Docs: [About Pull Requests](https://docs.github.com/en/pull-requests)

2. By Email
If you're not familiar with Git, you can email your information to _risk@globalquakemodel.org_.
Make sure to include enough detail and, if possible, refer to the existing data structure for consistency.

💬 What Makes a Valuable Contribution?

To include a new earthquake scenario, at least, the following information needs to be collected:

- Impact
- Recording stations
- Rupture geometries

## 0. Create a new event

To get familiar with the event, we recommend to check the excellent compilation of bibliography available at the International Seismological Center http://www.isc.ac.uk/event_bibliography/bibsearch.php

### Initialize the event folder using existing USGS ShakeMap data

In the notebook `0_initialize_folder_with_usgs.ipynb`, indicate the name of the event, country, magnitude, USGS ShakeMap code to generate the initial structure of the folder.

The notebook will:

- Create folders and subfolders according to the database structure, and download all required USGS data (recording stations and ruptures).

- Create READMEs and summaries.

>**NOTE**

>- The event folder will be created in the corresponding `country` folder as a draft version, i.e., its `name` will include the `DRAFT_` prefix.

>- If the event affects multiple countries, `country` refers to the one in which the epicenter is located.

>- For `Sequence` of events, check the example for [2002 Molise sequence](../Italy/20020000_Sequence_Molise).

## 1. Recording_Stations

- Download all recording station information available. Store the information in the raw format, with the corresponding links in the `README.md` file.<br>
Data should keep, as much as possible, the original format.<br>
Because recording data is heavy and we should not distribute it, store it in the 
[Google Drive](https://drive.google.com/drive/folders/0AHlkLIHROGCrUk9PVA) folder.

- Using the notebook `1_1_station_json_usgs_to_csv.ipynb`, create the `Stations_USGS.csv` file starting from the USGS file `stations.json` (downloaded in step 0).<br>
The code filters the entrances with null values, adjusts the file to the standard format, and shows a map with the USGS reported recording stations (which is not saved). You will need to fill the user input section with the name of the event (`DRAFT_NameEvent`).<br>
_NOTE: if the file `stations.json` is empty, do not include it in the database._

- For each of the other sources of data, a file `Stations_SourceName.csv` should be generated manually.<br>
The files must include the columns `['STATION_ID', 'STATION_NAME', 'LATITUDE', 'LONGITUDE', 'STATION_TYPE', 'REFERENCES']`, and at least one intensity measure type with its corresponding uncertainty, for example, `['PGA_VALUE', 'PGA_LN_SIGMA']`.<br>
_NOTE: For MMI, the uncertainty should be in the form of `MMI_STDDEV`_

The table below is an example of the suggested format.

| STATION_ID | STATION_NAME  | LATITUDE | LONGITUDE | STATION_TYPE | REFERENCES   | SOIL_TYPE | PGA_VALUE | PGA_LN_SIGMA | SA(0.3)_VALUE | SA(0.3)_LN_SIGMA | VS30 | VS30_TYPE |
|------------|---------------|----------|-----------|--------------|--------------|-----------|-----------|--------------|---------------|------------------|------|-----------|
| CANAP      | ANAPOIMA      | 4.5502   | -74.5141  | seismic      | Stations_SGC | ROCA      | 0.012341  | 0            | 0.015501      | 0                | 800  | measured  |
| CARBE      | ARBELAEZ      | 4.253    | -74.437   | seismic      | Stations_SGC | ROCA      | 0.023483  | 0            | 0.036099      | 0                | 800  | measured  |
| CARME      | ARMENIA       | 4.55     | -75.66    | seismic      | Stations_SGC | SUELO     | 0.011135  | 0            | 0.020943      | 0                | 400  | measured  |
| CBOG2      | GAVIOTAS      | 4.601    | -74.06    | seismic      | Stations_SGC | COLUVION  | 0.09279   | 0            | 0.127546      | 0                | 550  | measured  |
| CBUC1      | FLORIDABLANCA | 7.072    | -73.074   | seismic      | Stations_SGC | ROCA      | 0.018366  | 0            | 0.018812      | 0                | 800  | measured  |
| CIBA1      | IBAGUE        | 4.447    | -75.235   | seismic      | Stations_SGC | SUELO     | 0.019531  | 0            | 0.025926      | 0                | 324  | inferred  |
| CIBA3      | IBAGUE        | 4.4319   | -75.188   | seismic      | Stations_SGC | SUELO     | 0.013338  | 0            | 0.024665      | 0                | 539  | inferred  |

- If macroseismic data is available, the notebook `1_2_stations_macroseismic_gmice.ipynb` includes GMICE for different regions that can be tested.

- Using the notebook `1_3_stations_unique.ipynb`, generate the `Stations_Unique.csv`.<br>
     Please note that:
     - If only one source of data exists, then the `Stations_Unique.csv` file is not required.
     - If multiple data sources are available, the notebook creates the `Stations_Unique.csv`, by combining all sources named `Stations_SourceName.csv` and using the priority indicated by the modeller (which should also be reported in the `README.md` file).
     - The notebook generates the plot `recording_stations.png`.

- To verify the integrity of the files, run from the home folder:<br>
     ```pytest tests/test_stations.py``` <br>
     _NOTE: Consider that most of test ignore events in DRAFT status. Remove the DRAFT from the folder name before running the tests._


## 2. Ruptures

- Download all rupture information available. Store the information in the raw format, with the corresponding links in the `README.md` file.<br>
_NOTE: USGS stores the information in the file `rupture.json` (named in the repo as `rupture_USGS.json`) which downloaded in step 0._

- Using the notebook `2_1_rupture_usgs_json_to_oq_rupture_xml.ipynb`, it is possible to create the `earthquake_rupture_model_USGS.xml` file starting from the USGS file `rupture_USGS.json` (downloaded in step 0). The code parses the information to follow the OpenQuake format. You will need to fill the user input section with the name of the event (`DRAFT_NameEvent`).<br>
_NOTE 1: USGS rupture json file specifies 0 for all rake angles, so the user will need to include a value for the rake angle retrieved from literature._<br>
_NOTE 2: The notebook is experimental and it only supports simple planar surfaces (for point multi-planar or complex sources, manual work will be required)._

- For the other sources of information, prepare the OpenQuake rupture file and save it as `earthquake_rupture_model_SourceName.xml`.<br>
_NOTE 1: Multiple rupture definitions are available at <http://equake-rc.info/SRCMOD/searchmodels/allevents/>. The finite source rupture geometry, if not explicitly indicated, can be inferred from the FSP (`*.fsp`) link._<br>
_NOTE 2: Other sources of information about ruptures are: Global CMT, ISC, IRIS, SCARDEC, JMA, geofon-GFZ, geoscope ipgp._<br>
_NOTE 3: If rupture geometry was not available, we used the [IPT](https://platform.openquake.org/ipt/) to generate the fault plane, which relies on the magnitude scaling relationships of Wells and Coppersmith (1994), assuming a length-to-width aspect ratio of 2. To reproduce this, refer to the src folder and use the `test.py` and `build_rupture_plane.py` scripts. These may require adjustments depending on the available rupture data (e.g., length, width, surface).

- The notebook `2_2_ruptures_readme_.ipynb`:
     - Generates the plot `earthquake_ruptures.png`
     - Adds/updates `README.md` file to include image and rupture details.
     - Include in the `REAME.md` the rupture mechanism and tectonic region type using the `earthquake_information.csv` file.<br>

     >_NOTE: When complex faults have the error `Surface does not conform with Aki & Richards convention`, the code [correct_complex_sources.py](https://github.com/gem/oq-engine/blob/master/openquake/engine/tools/correct_complex_sources.py) can be used to fix it._<br>

#### For reference:

**Rupture mechanism:**

There are different types of faulting mechanisms for each focal-mechanism end member, including strike-slip fault, normal fault, thrust fault, and or some combination. Additional info for the definition of this parameter is available at [USGS](https://www.usgs.gov/programs/earthquake-hazards/focal-mechanisms-or-beachballs), IRIS  and [PDSN](https://pnsn.org/outreach/about-earthquakes/focal-mechanisms).
```
Dip = 90°   Rake = 0°    ::  left-lateral strike-slip
Dip = 90°   Rake = 180°  ::  right lateral strike slip
Dip = 45°   Rake = 90°   ::  reverse fault
Dip = 45°   Rake = -90°  ::  normal fault

Other tips:
Fault type (Strike-slip, Normal, Thrust/reverse) is derived from rake angle:
- Rake angles within 30 of horizontal are strike-slip,
- Rake angles from 30 to 150 are reverse, and 
- Rake angles from -30 to -150 are normal. 
```

**Tectonic region type:**

Tectonic features associated to the event. For example, active shallow crust, subduction interface, subduction intraslab, stable continental. See additional guidance in [Chen et al. 2018](https://academic.oup.com/gji/article/213/2/1263/4794950).

```
- A shallow crustal earthquake, also known as a crustal earthquake, occurs within the Earth's crust, typically at depths of less than 20 km.
- An intraslab subduction earthquake, typically occurs at depths between 70 and 700 km.
- An interface subduction earthquake, also known as an intraplate earthquake, typically occurs at depths between 20 and 70 km.
```

## 3. OpenQuake_gmfs

### 3.0 Ground motion logic trees

Selection of ground motion models (GMMs or GMPEs) to be used in the calculations.

To condition the gmfs in OpenQuake, the GMMs should support separate std_ dev (inter and intra). It is possible to define a [ModifiableGMPE](https://github.com/gem/oq-engine/blob/master/openquake/qa_tests_data/event_based/case_28/gmmLt.xml), and assign a `add_between_within_stds.with_betw_ratio = 0.6`.

The following references can be used for the selection of GMMs:

- **`gmpe_logic_tree_GEM.xml`**: using the tectonic region type of the event, get the GMPEs applicable for the event based on the models available in the Global Hazard Mosaic.

- **`gmpe_logic_tree_USGS.xml`**: for USGS, get the GMPEs and weights (check notebook `3_oq_gmmLT_from_usgs_shakemap.ipynb`).

### 3.1 Create `stationslist.csv` file

The `stationlist` is the files used by OQ to condition the ground shaking to the observations.

Using the notebook `3_1_oq_stationlist.ipynb`, the `Stations_Unique.csv` file (generated before in the _Recording_Stations_ folder) is filtered and post-processed. The script adjusts the data to follow the OpenQuake format.<br>

This notebook:

1. Defines the IMTs to be used in the conditioning of the ground shaking.
It highlights the number of missing values for each IMT, and with the parameter `imts` the user indicates the desirable IMTs to consider. Only stations that have no-empty IMT values are selected.
Using multiple IMTs is recommended for running risk calculations, but it could decrease the number of available stations if data is not complete.

2. Separate files for stationlist are created: only seismic stations (`stationlist_seismic.csv`) and all stations (seismic and macroseismic, `stationlist_all.csv`).<br>
The files are saved in the _OpenQuake_gmfs_ folder. (For the first version only the file with the seismic station is being used)

3. Prepares the `site_model_stations.csv`, indicating Vs30 values at station's location.<br>
When Vs30 values are not included in the source data, a reference USGS Vs30 proxy is used for inferring the values.

_NOTE: Manual editions to this file might be needed during the calibration process. Be sure to change the path of the vs30 reference file from USGS._

### 3.2 Site model and hazard sites

Using the notebook `3_2_oq_vs30_uniform_grid.ipynb`, it is possible to create a site model with a spaced grid using the reference data (such as the USGS Vs30 proxy).

The user defines the grid spacing and the maximum distance from a given hypocenter definition (referenced to a given rupture file). The notebook also saves a map with the Vs30 values.

_NOTE: For calibration and visualization purposes, it is convenient to create a fine grid (1 to 2 km) close to the epicentre and coarser grids at larger distances. The grid should cover, at least, up to a distance in which the estimated PGA <= 0.05g._

### 3.3 Generate job files and run oq scenarios to get the gmfs for the event

Using the notebook `3_3_run_oq_scenarios.ipynb`, it is possible to generate the job files (both for the unconditioned and station conditioned cases) for all the combinations the user would like to include: Rupture models, GMPEs and directly run the calculations of the gmfs. The code will automatically save both log files and also the gmfs of the calculations.

The user needs to define the Name of the event and the combinations of Rupture Models + GMPEs that they want to run. The analyses will be saved in the ´Sensitivity´ folder that will be generated automatically.

### 3.4 Generate the calculations summary file

Using the notebook `3_4_calculations_summary.ipynb`, create the summary file for all the calculations in the Sensitivity folder. This file will help in choosing the combination presenting the lowest bias among all of them. The user should provide the name of the event at the begining of the file.

### 3.5 Plot the gmfs and save the ones reporting the lowest bias or the on

- Finally using the `3_5_plot_gmfs.ipynb` should generate the gmf plots for any of the previous runs. The user can specify the ids of the files they want to plot, or leave `None` for it to generate all the gmf plots from the log files in the Sensitivity folder. 

Once the script runs check the `README` just to be certain that all of the plots are being included and can be seen correctly.


## 4. Impact data

The goal is to collect as much information as possible at the minimum geographical detail for the human, building and economic impact caused by the event (e.g. fatalities, injured, displaced population, affected population, buildings affected, buildings damaged, buildings collapsed, economic losses, insured losses, induced effects).

The definition of the attributes reported in the impact files are described in [metadata](https://gitlab.openquake.org/risk/ecd/-/blob/main/metadata.md#impact-data). Follow the format and the definition suggested.

When collecting data, consider:

- There are 3 types of information collected:
     - `Impacts_All_ID_X.csv`: includes all impact data for different administrative regions: ID_0 (national level), ID_1 (administrative level 1), ID_2 (administrative level 2), ID_3 (administrative level 3). When available, building level information is included.
     - `Impact_Buildings_ID_X.csv`: it includes datasets describing the physical damage substained by buildings, dwellings or households due to the earthquake and its induced effects. Additional information regarding damage states and cause of damage among other details can be included.
     - `Impact_Human_ID_X.csv`: it includes datasets describing the human impact due to the earthquake and its induced effects. Additional information regarding injury levels, cause of death among other details can be included.

- The collected data should report the original damage states or injuries levels (as indicated by the source of reference), in addition to the values required (mandatory) in the database.

- Report range of values with no spaces (e.g `10-25` or `>230`) and numbers without commas or dots (e.g. `1200` instead of `1,200`).

- In the dataset, blank cells indicate missing or unavailable information and they should not be interpreted as zero. These values reflect cases where the original data source did not report a value. 

The section helps to clarify FAQs regarding impact data collection.

### 4.1 Human impact

**FATALITIES:**

- Any information about the cause of death? Are they mentioned disaggregated numbers based on the cause of the death? What about Missing? If there is some information about the above questions, you can create dedicated columns to report the values, and add a note in the `COMMENT` column. But in any case, the summation should be presented in the `FATALITIES` column.<br>
- Does `FATALITIES_GROUND_SHAKING` include missing people?.<br>
Yes. Make sure you report final numbers after full coverage, not interim reports in the aftermath of the event which may signal several missing values.

**INJURIES:**

`Injured = Direct injuries + indirect injuries`

- When detailed information is available regarding injury levels, refer to [metadata.md](./metadata#aditional-impact-details.md) to summarize data based using the proposed structure (e.g. `INJURIES_LIGHT`, `INJURIES_SEVERE`, `INJURIES_CRITICAL`).
- Any information about the cause of injury? Are they mentioned disaggregated numbers based on the cause of the injury? If there is information about the above questions, you can create a dedicated file to report the values, and add a note in the `COMMENT` column. But in any case, the summation should be presented in the `INJURED` column.
- When information is available only for a few injury levels, shall it be reported?
Yes. Add the necessary columns to report the data (keeping the original injury level definition, e.g. `HOSPITALIZED`). Moreover, report the values in the equivalent injury level proposed in the database (e.g. `INJURIES_CRITICAL`), and overall number in the `INJURIES` column (in this case the sum of the different injury levels).

>**Note**
> The references for the proposed injury levels are:
> - [Spence et al 2007](https://www.earth-prints.org/handle/2122/3421). Earthquake disaster scenario prediction and loss modelling for urban areas. Page #66.
> - [FEMA 2003](https://www.fema.gov/sites/default/files/2020-09/fema_hazus_earthquake-model_technical-manual_2.1.pdf). HAZUS-MH Technical Manual. Developed by the Department of Homeland Security, Federal Emergency Management Agency. Page #562.

**AFFECTED_POPULATION:**

This value is only reported when the source of reference explicitly indicates "affected" and it does not provide differentiation regarding the level of affectance.

- If there is no explicit information about the `AFFECTED_POPULATION`, leave the value empty (_do not sum_ `fatalities + injuries + displaced_population`).
- If the affected population has been disaggregated (it includes death, injuries, etc), present that number in the `Impact_Human_ID_X` file.
- What to do with sources in which there are more displaced than affected?<br>
Typically, the number of `Affected_Population` should be more than `Displaced_Population` because `Affected_Population` is the summation of Fatalities, Injuries, and Displaced_Population. If you encounter `Displaced_Population` more than `Affected_Population`, indicate `True` in the column `FLAG` to indicate it as not reliable.

**DISPLACED_POPULATION:**

This value is only reported when the source of reference explicitly indicates "displaced" and it does not provide differentiation regarding the level of displacement (homless, sheltered, evacuated).

- If there is no explicit information about the `DISPLACED_POPULATION`, leave the value empty (_do not sum_ `homeless + sheltered + evacuated`).
- If the displaced population has been disaggregated (it includes homeless, sheltered, evacuated),  present that number in the `Impact_Human_ID_X` file.
- What value should be reported in the `earthquake_summary.csv` file? when all the sources report the displaced population dissagregated?

     - If non of the soruces provide a reasonable estimate for the `DISPLACED_POPULATION`, leave the value empty. 
     - When information is dissagregated, add additional rows to explicitly report  `HOMELESS`, `SHELTERED` or `EVACUATED`.

### 4.2 Building impact

**AFFECTED_UNITS:**

- This value is reported when the source of reference does not differenciate between the damage levels.
- Do not sum the damage units to report this value. Only report it when explicitly indicated as affected unites.

**DAMAGED_UNITS:**

>**Warning**
> The number of totally destroyed or collapsed units is not included, unless exctrictly necessary.

- If the source of reference indicate _"... x number of units were damaged or destroyed"_, then the value should be reported under `DAMAGED_UNITS` and a note indicating this should be added in the `COMMENTS` column.
- Examples of damage unit collection:
     - X number of units damaged: Put X under `DAMAGED_UNITS`
     - X number of units damaged or destroyed: Put X under `DAMAGED_UNITS`
     - X number of units destroyed (or completely destroyed): Put X under `DESTROYED_UNITS`
- When detailed information is available regarding damage states, refer to [metadata.md](./metadata#aditional-building-details.md) to summarize data based using the proposed structure (e.g. `DS1_SLIGHT`, `DS3_MODERATE`).
- Add extra columns and present data per damage level keeping the orioginal classification in the in the `Impact_Building_ID_X` file . In addition, the number of units in the recomended damage states can be added.

### 4.3 Economic impact

**ECONOMIC_LOSSES:**

- Currency units are based on the source of reference and reported in the `CURRENCY` column.
- Reported values unadjusted for inflation.
- If the reference includes multiple currencies, then a row per currency is required
- The losses do not account for the "recovery" cost
- If there is information regarding the source of the loss, e.g. direct loss, indirect, etc, report it in different columns.

### 4.4 Minimum Required Impact Metrics
To ensure consistency and usefulness of the dataset, we aim to collect at least the following core impact metrics for each event, as defined in the `earthquake_information.csv` file:
- Fatalities
- Injured
- Displaced population
- Affected population
- Affected units
- Damaged units
- Collapsed units
- Economic losses

These attributes represent the minimum expected information when contributing new events. Contributors are encouraged to provide as much detail as possible, ideally at the finest geographical resolution available.

## 5. Final details
- Update this database, figure and home README using the notebook `6_ecd_readme.ipynb`
- Verify the integrity of all files by running in the terminal ```pytest tests/``` from the home folder
- Create a `pull request` to include the new event in the `main` branch.
