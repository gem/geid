<!-- <div align='center'>
<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Global_Earthquake_Model_Logo.png/440px-Global_Earthquake_Model_Logo.png" alt="GEM Foundation" width="300"/>
</p> -->

<div align='center'>
    <p align="center">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Global_Earthquake_Model_Logo.png/440px-Global_Earthquake_Model_Logo.png" alt="GEM Foundation" width="300" style="border: none; outline: none;"/>
    </p>
    <!-- Links with badges, no box around them -->
    <a href='../World/'>
        <img src='https://img.shields.io/badge/Global_coverage-gray?style=for-the-badge' style="border: none; outline: none;">
    </a>
    <a href='../contribute_guidelines.md'>
        <img src='https://img.shields.io/badge/Contribute-orange?style=for-the-badge' style="border: none; outline: none;">
    </a>
    <a href='../LICENSE.txt'>
        <img src='https://img.shields.io/badge/LICENSE-blue?style=for-the-badge' style="border: none; outline: none;">
    </a>
</div>



<!-- <a href='./earthquake_scenarios/'>
    <img src='https://img.shields.io/badge/Earthquake_Scenarios-green?style=for-the-badge'>
</a> -->


# 🔎 Global Earthquake Impact Database (GEID) - European Repository

## ✨ Overview

The Global Earthquake Impact Database (GEID) provides comprehensive earthquake and impact data to support the validation and verification of seismic risk models [^1]. Developed by the GEM Foundation and its partners, GEID enhances the OpenQuake scenario damage and loss calculator by integrating USGS ShakeMaps [^2] [^3] [^4], data from other providers (e.g., INGV, EFEHR), and scientific literature. This allows users to generate cross-correlated ground motion fields, assess risk metrics using different rupture models, and compare results with past events. GEID complements the [USGS ShakeMap](https://earthquake.usgs.gov/data/shakemap/) Atlas, which covers nearly all damaging earthquakes of the past 120 years, and AtlasCat, which provides aggregate loss data. By incorporating additional spatially detailed earthquake and impact records, GEID strengthens seismic risk assessment capabilities within OpenQuake [^4].


>The v2023.0.0 release of Europe’s Earthquake Dataset within the Global Earthquake Impact Database (GEID) is now available! 🚀 🥳 🚀
This repository hosts the most up-to-date version of data for the countries in Europe.

<div align='center'>
    <img src="../World/eq_events_europe.png" alt="Europe events" width="700"/>
</div>

This database is open and aims at being a community effort, that enables users to add new events 
(see [contributing guidelines](../contribute_guidelines.md)) or to provide additional data to 
existing entries. We aim to continue expanding the GEID by leveraging on data often collected within 
the scope of GEM projects, as well as data previously collected as part of the 
[GEM Earthquake Consequences Database](https://www.globalquakemodel.org/gempublications/Introduction-to-the-GEM-Earthquake-Consequences-Database-(GEMECD)).

# 🌍 Country list
The following countries are covered in this repository. 

|COUNTRY                                     |ISO_3|
|--------------------------------------------|-----|
|Albania                                     |ALB  |
|Croatia                                     |HRV  |
|Cyprus                                      |CYP  |
|Greece                                      |GRC  |
|Iceland                                     |ISL  |
|Italy                                       |ITA  |
|Netherlands                                 |NLD  |
|Romania                                     |ROU  |
|Serbia                                      |SRB  |
|Spain                                       |ESP  |
|Türkiye (Turkey)                            |TUR  |

</details>

The following events are available in Europe. Additionally, a global summary of impact data can be found in the [World folder](../World).

<details>
<summary> List with available events
</summary>

|     | Region                    | Country     |   Year | Event Name                                                                                |   Mw |   Depth (km) | Max Intensity (MMI)          |
|----:|:--------------------------|:------------|-------:|:------------------------------------------------------------------------------------------|-----:|-------------:|:-----------------------------|
|  1  | Europe                    | Albania     |   2019 | [Durres](Albania/20191126_M6.4_Albania)                                                   | 6.4  |        22    | VIII                         |
|  2  | Europe                    | Croatia     |   2020 | [Zagreb 2020](Croatia/20200322_M5.1_Zagreb)                                               | 5.1  |        10    | VIII                         |
|  3  | Europe                    | Croatia     |   2020 | [Petrijna 2020](Croatia/20201229_M6.3_Petrijna)                                           | 6.3  |        10    | IX                           |
|  4  | Europe                    | Cyprus      |   1996 | [Cyprus](Cyprus/19961009_M6.8_Cyprus)                                                     | 6.8  |        33    | VI                           |
|  5  | Europe                    | Greece      |   1981 | [GulfofCorinth 1981](Greece/19810000_Sequence_GulfOfCorinth/19810225_M6.4_GulfofCorinth)  | 6.4  |        33    | IX                           |
|  6  | Europe                    | Greece      |   1981 | [GulfofCorinth 1981](Greece/19810000_Sequence_GulfOfCorinth/19810224_M6.7_GulfofCorinth)  | 6.7  |        33    | IX                           |
|  7  | Europe                    | Greece      |   1986 | [Kalamata 1986](Greece/19860913_M6.0_Kalamata)                                            | 6    |        11.2  | VIII                         |
|  8  | Europe                    | Greece      |   1988 | [Elia 1988](Greece/19881016_M5.88_Elia)                                                   | 5.9  |        25.2  | VII                          |
|  9  | Europe                    | Greece      |   1995 | [Aigio 1995](Greece/19950615_M6.4_Aigio)                                                  | 6.4  |        14.2  | VIII                         |
|  10 | Europe                    | Greece      |   1995 | [KozaniGrevena 1995](Greece/19950513_M6.5_KozaniGrevena)                                  | 6.5  |        14    | VIII                         |
|  11 | Europe                    | Greece      |   1999 | [Athens 1999](Greece/19990907_M5.9_Athens)                                                | 5.9  |        10    | IX                           |
|  12 | Europe                    | Greece      |   2014 | [Kefalonia 2014](Greece/20140000_Sequence_Kefalonia/20140126_M6.1_Kefalonia)              | 6.1  |         8    | VIII                         |
|  13 | Europe                    | Greece      |   2014 | [Kefalonia 2014](Greece/20140000_Sequence_Kefalonia/20140203_M6.0_Kefalonia)              | 6    |         5    | VII                          |
|  14 | Europe                    | Greece      |   2015 | [Lefkada 2015](Greece/20151117_M6.5_Lefkada)                                              | 6.5  |        11    | VIII                         |
|  15 | Europe                    | Greece      |   2017 | [AegeanSea 2017](Greece/20170612_M6.3_AegeanSea)                                          | 6.3  |        12    | VII                          |
|  16 | Europe                    | Iceland     |   2000 | [Iceland 2000](Iceland/20000620_M6.46_Iceland)                                            | 6.5  |        10    | IX                           |
|  17 | Europe                    | Iceland     |   2000 | [Iceland](Iceland/20000617_M5.87_Iceland)                                                 | 5.9  |        10    | VIII                         |
|  18 | Europe                    | Iceland     |   2008 | [Iceland 2008](Iceland/20080529_M6.32_Iceland)                                            | 6.3  |         9    | VIII                         |
|  19 | Europe                    | Italy       |   1980 | [Irpinia 1980](Italy/19801123_M6.9_Irpinia)                                               | 6.9  |        10    | X                            |
|  20 | Europe                    | Italy       |   1990 | [Augusta 1990](Italy/19901213_M5.61_Augusta)                                              | 5.6  |        11.1  | VIII                         |
|  21 | Europe                    | Italy       |   1997 | [UmbriaMarche 1997](Italy/19970000_Sequence_UmbriaMarche/19970926_M5.97_UmbriaMarche)     | 6    |        10    | VIII                         |
|  22 | Europe                    | Italy       |   1997 | [UmbriaMarche 1997](Italy/19970000_Sequence_UmbriaMarche/19971014_M5.86_UmbriaMarche)     | 5.9  |        10    | VII                          |
|  23 | Europe                    | Italy       |   1997 | [UmbriaMarche 1997](Italy/19970000_Sequence_UmbriaMarche/19970926_M5.72_UmbriaMarche)     | 5.7  |        10    | VIII                         |
|  24 | Europe                    | Italy       |   2002 | [Molise 2002](Italy/20020000_Sequence_Molise/20021101_M5.72_Molise)                       | 5.8  |        10    | VII                          |
|  25 | Europe                    | Italy       |   2002 | [Molise 2002](Italy/20020000_Sequence_Molise/20021031_M5.74_Molise)                       | 5.9  |        10    | VII                          |
|  26 | Europe                    | Italy       |   2004 | [Gardone 2004](Italy/20041124_M4.99_Gardone)                                              | 5.1  |        17.2  | VIII                         |
|  27 | Europe                    | Italy       |   2009 | [Laquila 2009](Italy/20090000_Sequence_Laquila/20090407_M5.4_Laquila)                     | 5.4  |        15.1  | VI                           |
|  28 | Europe                    | Italy       |   2009 | [Laquila 2009](Italy/20090000_Sequence_Laquila/20090406_M6.18_Laquila)                    | 6.2  |         8.8  | VIII                         |
|  29 | Europe                    | Italy       |   2012 | [EmiliaRomagna 2012](Italy/20120000_Sequence_EmiliaRomagna/20120520_M5.8_EmiliaRomagna)   | 5.8  |         6.3  | VIII                         |
|  30 | Europe                    | Italy       |   2012 | [EmiliaRomagna 2012](Italy/20120000_Sequence_EmiliaRomagna/20120529_M5.6_EmiliaRomagna)   | 5.6  |        10.2  | VIII                         |
|  31 | Europe                    | Italy       |   2016 | [CentralItaly 2016](Italy/20162017_Sequence_CentralItaly/20161030_M6.5_CentralItaly)      | 6.5  |         8    | IX                           |
|  32 | Europe                    | Italy       |   2016 | [CentralItaly 2016](Italy/20162017_Sequence_CentralItaly/20161026_M6.09_CentralItaly)     | 6.1  |        10    | VIII                         |
|  33 | Europe                    | Italy       |   2016 | [CentralItaly 2016](Italy/20162017_Sequence_CentralItaly/20160824_M6.21_CentralItaly)     | 6.2  |         4.44 | IX                           |
|  34 | Europe                    | Italy       |   2017 | [CentralItaly 2017](Italy/20162017_Sequence_CentralItaly/20170118_M5.95_CentralItaly)     | 5.95 |         7    | VII                          |
|  35 | Europe                    | Netherlands |   1992 | [Roermond 1992](Netherlands/19920413_M5.3_Roermond)                                       | 5.3  |        21.2  | VIII                         |
|  36 | Europe                    | Romania     |   1990 | [Vrancea 1990](Romania/19900530_Sequence_Vrancea/19900530_M6.95_Vrancea)                  | 7    |        89.3  | VIII                         |
|  37 | Europe                    | Romania     |   1990 | [Vrancea 1990](Romania/19900530_Sequence_Vrancea/19900531_M6.31_Vrancea)                  | 6.3  |        88.2  | V                            |
|  38 | Europe                    | Serbia      |   2010 | [Kraljevo](Serbia/20101103_M5.52_Kraljevo)                                                | 5.5  |         0.9  | VI                           |
|  39 | Europe                    | Spain       |   2011 | [Lorca 2011](Spain/20110511_M5.1_Lorca)                                                   | 5.1  |         1    | VI                           |
|  40 | Europe                    | Turkey      |   1992 | [Erzincan](Turkey/19920313_M6.68_Erzincan)                                                | 6.7  |        27.2  | VIII                         |
|  41 | Europe                    | Turkey      |   1995 | [Dinar](Turkey/19951001_M6.42_Dinar)                                                      | 6.4  |        33    | VIII                         |
|  42 | Europe                    | Turkey      |   1998 | [AdanaCeyhan 1998](Turkey/19980627_M6.28_AdanaCeyhan)                                     | 6.3  |        33    | VIII                         |
|  43 | Europe                    | Turkey      |   1999 | [Izmit](Turkey/19990817_M7.53_Izmit)                                                      | 7.6  |        17    | X                            |
|  44 | Europe                    | Turkey      |   1999 | [Duzce 1999](Turkey/19991112_M6.71_Duzce)                                                 | 6.7  |        10    | IX                           |
|  45 | Europe                    | Turkey      |   2011 | [Van 2011](Turkey/20111023_M7.1_Van)                                                      | 7.1  |        18    | VIII                         |
|  46 | Europe                    | Turkey      |   2020 | [AegeanSea 2020](Turkey/20201030_M7_AegeanSea)                                            | 7    |        21    | VIII                         |
|  47 | Europe                    | Turkey      |   2023 | [CentralTurkey 2023](Turkey/20230206_M7.8_KahramanmarasGaziantep)                         | 7.8  |        10    | XII                          |
</details>



# 🚀 Model versions

Each version of the archive that is released can be accessed by changing from the `main` branch to the `tag` of a given version.
The `main` branch could contain the work-in-progress of the next version of the model.

| Version   | Release Notes                                                            |
|-----------|--------------------------------------------------------------------------|
| [v2023.0.0](https://github.com/gem/geid/tree/v2023.0.0) | First release with 100 earthquake scenario events.|

# 🌟 Contributors

The authors are grateful for the input from dozens of collaborators. 

# Citation
If you use this repository, please cite it using the following DOI: 

[![DOI](https://zenodo.org/badge/652540199.svg)](https://doi.org/10.5281/zenodo.8425466)

# License
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

# Funding

This repository has been developed within the [**Geo-INQUIRE**](https://www.geo-inquire.eu/) project, with funding received from the **European Union's Horizon Europe programme** under grant agreement **No. 101058518**.

<!-- Funding Logos Section (Geo-INQUIRE and EU) -->
<div align="left">
    <br> <!-- Line break to separate sections -->
    <div style="display: inline-flex; align-items: center; gap: 20px;">
        <!-- First logo (EU Funded) -->
        <img src="../World/EN_fundedbyEU_VERTICAL_RGB_NEG.png" alt="EU Funded" width="150" style="border: none; outline: none;"/>
        <!-- Second logo (Geo-INQUIRE), centered vertically -->
        <img src="../World/Geo-INQUIRE_logo_2_crop.jpg" alt="Geo-INQUIRE" width="150" style="border: none; outline: none; align-self: center;"/>
    </div>
</div>



# 🤔 Frequently asked questions

### How to contribute?

You can follow the instructions indicated in the [contributing guidelines](../contribute_guidelines.md).

### Which version am I seeing? How to change the version?

By default, you will see the files in the repository in the `main` branch. Each version of the model that is released can be accessed is marked with a `tag`. By changing the tag version at the top of the repository, you can see the files for a given version.

Note that the `main` branch could contain the work-in-progress of the next version of the model.

### How do I download the data for a given version?

For each version, a related zip file is available in the [release section](https://github.com/gem/global_exposure_model/releases).

# References
[^1]: Villar-Vega, M., Silva, V. (2017). Assessment of earthquake damage considering the characteristics of past events in South America. Earthquake Engineering and Soil Dynamics, 99:86-96.
[^2]: Silva V, Horspool N (2019). Combining USGS ShakeMaps and the OpenQuake engine for damage and loss assessment. Earthquake Engineering and Structural Dynamics. 48(6):634-652.
[^3]: Worden, C. B., Thompson, E. M., Hearne, M. G., & Wald, D. J. (2020). ShakeMap Manual Online: technical manual, user’s guide, and software guide, U. S. Geological Survey. URL: http://usgs.github.io/shakemap/. DOI: https://doi.org/10.5066/F7D21VPQ.
[^4]: Wald, D. J., Worden, C. B., Thompson, E. M., & Hearne, M. G. (2022). ShakeMap operations, policies, and procedures. Earthquake Spectra, 38(1), 756–777. DOI: https://doi.org/10.1177/87552930211030298.
[^5]: Engler, D. T., Worden, C. B., Thompson, E. M., & Jaiswal, K. S. (2022). Partitioning Ground Motion Uncertainty When Conditioned on Station Data. Bulletin of the Seismological Society of America, 112(2), 1060–1079. DOI: https://doi.org/10.1785/0120210177.