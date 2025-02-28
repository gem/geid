
<div align='center'>
<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Global_Earthquake_Model_Logo.png/440px-Global_Earthquake_Model_Logo.png" alt="GEM Foundation" width="300"/>
</p>
<a href='./earthquake_scenarios/'>
    <img src='https://img.shields.io/badge/Earthquake_Scenarios-green?style=for-the-badge'>
</a>
<a href='./World/'>
    <img src='https://img.shields.io/badge/Global_coverage-gray?style=for-the-badge'>
</a>
<a href='./contribute_guidelines.md'>
    <img src='https://img.shields.io/badge/Contribute-orange?style=for-the-badge'>
</a>
<a href='./LICENSE.txt'>
    <img src='https://img.shields.io/badge/LICENSE-blue?style=for-the-badge'>
</a>
</div>

# 🔎 Global Earthquake Impact Database (GEID)

The development of probabilistic seismic risk assessment (PSRA) models requires stress-testing 
the various components of the models, often through the assessment of damage and losses 
considering the characteristics of past events[^1]. In this context, the GEM Foundation and 
its partners have expanded the OpenQuake scenario damage and loss calculator to use directly 
USGS ShakeMaps[^2][^3][^4], or earthquake data from other providers (e.g., INGV, EFEHR) or the 
scientific literature. This functionality allows users to generate cross-correlated ground 
motion fields considering recordings from seismic stations [^5], to compute a number of 
risk metrics based on different rupture solutions and ground motion models, and to compare the 
results against past observations and damage reports. An overview of the functionalities implemented 
within the OpenQuake engine can be found at https://github.com/gem/oq-engine/issues/8317.

# ✨ Overview

The Global Earthquake Impact Database (GEID) aims to provide both earthquake and impact data 
for users to perform earthquake scenarios using GEM or their own models for validation 
and verification purposes. This database serves as a complement to the 
[USGS ShakeMap](https://earthquake.usgs.gov/data/shakemap/) Atlas and AtlasCat. 
The former resource has ShakeMaps for a comprehensive catalogue of nearly all 
near-damaging and damaging events worldwide for the past 120 years and can be used directly 
for impact assessment within the OpenQuake engine [^4]. The latter provides aggregate losses 
for each event separated by cause. The GEID builds upon these sources of data by collecting additional 
earthquake and impact information, often documented spatially and with greater detail.

> The v2023.0.0 release for the Global Earthquake Impact Database (GEID) is available! 🥳 🚀

<div align='left'>
    <img src="./World/eq_events.png" alt="GEID events" width="700"/>
</div>

This database is open and aims at being a community effort, that enables users to add new events 
(see [contributing guidelines](./contribute_guidelines.md)) or to provide additional data to 
existing entries. We aim to continue expanding the GEID by leveraging on data often collected within 
the scope of GEM projects, as well as data previously collected as part of the 
[GEM Earthquake Consequences Database](https://www.globalquakemodel.org/gempublications/Introduction-to-the-GEM-Earthquake-Consequences-Database-(GEMECD)).

## 🗺️ Database coverage

The database is compatible with GEM's Global Models, and the folders are organized according to regions and countries/territories, as specified in the map and table below.

<p align="center">
  <img src="./World/World_Regions.png" alt="World regions" width="600">
</p>

<details>
<summary> 🌍 Regions, countries and territories
</summary>

| REGION                    | COUNTRIES AND TERRITORIES |
|---------------------------|---------------------------|
| Africa                    | Algeria, Angola, Benin, Botswana, Burkina_Faso, Burundi, Cameroon, Cape_Verde, Central_African_Republic, Chad, Comoros, Congo, Democratic_Republic_of_the_Congo, Djibouti, Egypt, Equatorial_Guinea, Eritrea, Eswatini, Ethiopia, Gabon, Gambia, Ghana, Guinea, Guinea_Bissau, Ivory_Coast, Kenya, Lesotho, Liberia, Libya, Madagascar, Malawi, Mali, Mauritania, Mauritius, Morocco, Mozambique, Namibia, Niger, Nigeria, Rwanda, Sao_Tome_and_Principe, Senegal, Seychelles, Sierra_Leone, Somalia, South_Africa, South_Sudan, Sudan, Tanzania, Togo, Tunisia, Uganda, Zambia, Zimbabwe |
| Caribbean_Central_America | Anguilla, Antigua_and_Barbuda, Aruba, Bahamas, Barbados, Belize, British_Virgin_Islands, Cayman_Islands, Costa_Rica, Cuba, Dominica, Dominican_Republic, El_Salvador, Grenada, Guadeloupe, Guatemala, Haiti, Honduras, Jamaica, Martinique, Montserrat, Nicaragua, Panama, Puerto_Rico, Saint_Kitts_and_Nevis, Saint_Lucia, Saint_Vincent_and_the_Grenadines, Trinidad_and_Tobago, Turks_and_Caicos_Islands, US_Virgin_Islands |
| Central_Asia              | Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan, Uzbekistan |
| East_Asia                 | China, Hong_Kong, Japan, Macao, North_Korea, South_Korea, Taiwan |
| Europe                    | Albania, Andorra, Austria, Belarus, Belgium, Bosnia_and_Herzegovina, Bulgaria, Croatia, Cyprus, Czechia, Denmark, Estonia, Finland, France, Germany, Gibraltar, Greece, Hungary, Iceland, Ireland, Isle_of_Man, Italy, Kosovo, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Moldova, Monaco, Montenegro, Netherlands, North_Macedonia, Norway, Poland, Portugal, Romania, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Turkey, Ukraine, United_Kingdom |
| Middle_East               | Afghanistan, Armenia, Azerbaijan, Bahrain, Georgia, Iran, Iraq, Israel, Jordan, Kuwait, Lebanon, Oman, Pakistan, Palestine, Qatar, Saudi_Arabia, Syria, United_Arab_Emirates, Yemen |
| North_America             | Canada, Mexico, United_States_of_America |
| North_Asia                | Mongolia, Russia |
| Oceania                   | American_Samoa, Australia, Cook_Islands, Fiji, Guam, Kiribati, Marshall_Islands, Micronesia, Nauru, New_Caledonia, New_Zealand, Niue, Northern_Mariana_Islands, Palau, Papua_New_Guinea, Samoa, Solomon_Islands, Tonga, Tuvalu, Vanuatu |
| South_America             | Argentina, Bolivia, Brazil, Chile, Colombia, Ecuador, French_Guiana, Guyana, Paraguay, Peru, Suriname, Uruguay, Venezuela |
| South_Asia                | Afghanistan, Bangladesh, Bhutan, India, Nepal, Pakistan, Sri_Lanka |
| Southeast_Asia            | Brunei, Cambodia, Indonesia, Laos, Malaysia, Myanmar, Philippines, Singapore, Thailand, Timor_Leste, Vietnam |

</details>

The following events are available, with a global summary of impact data available in the [World folder](./World).

<details>
<summary> List with available events
</summary>

|     | Region                    | Country     |   Year | Event Name                                                                           |   Mw |   Depth (km) | Max Intensity (MMI)          |
|----:|:--------------------------|:------------|-------:|:-------------------------------------------------------------------------------------|-----:|-------------:|:-----------------------------|
|   0 | Africa                    | Algeria     |   2003 | [Boumerdes 2003](./Africa/Algeria/20030521_M6.8_Boumerdes)                           | 6.8  |        12    | IX-X                         |
|   1 | Africa                    | Botswana    |   2017 | [Moijabana 2017](./Africa/Botswana/20170403_M6.5_Moijabana)                          | 6.46 |        23.5  | VIII                         |
|   2 | Africa                    | Egypt       |   1992 | [Cairo 1992](./Africa/Egypt/19921012_M5.9_Cairo)                                     | 5.8  |        21.5  | VIII                         |
|   3 | Africa                    | Malawi      |   1989 | [Salima](./Africa/Malawi/19890310_M6.2_Salima)                                       | 6.27 |        28.2  | VIII                         |
|   4 | Africa                    | Malawi      |   2009 | [Karonga](./Africa/Malawi/20091219_M6.0_Karonga)                                     | 6    |         6    | VII                          |
|   5 | Africa                    | Morocco     |   2004 | [AlHoceima 2004](./Africa/Morocco/20040224_M6.3_AlHoceima)                           | 6.3  |        12.2  | IX                           |
|   6 | Africa                    | Morocco     |   2023 | [MarrakeshSafi 2023](./Africa/Morocco/20230908_M6.8_MarrakeshSafi)                   | 6.8  |        19    | VIII                         |
|   7 | Africa                    | Tanzania    |   2016 | [Bukoba 2016](./Africa/Tanzania/20160910_M5.9_Bukoba)                                | 5.9  |        40    | VII                          |
|   8 | Caribbean Central America | Costa Rica  |   1991 | [Limon](./Caribbean_Central_America/Costa_Rica/19910422_M7.6_Limon)                  | 7.6  |        10    | VIII                         |
|   9 | Caribbean Central America | Costa Rica  |   2009 | [Cinchona](./Caribbean_Central_America/Costa_Rica/20090108_M6.1_Cinchona)            | 6.2  |         4.6  | IX in Cinchona e Isla Bonita |
|  10 | Caribbean Central America | Costa Rica  |   2012 | [Nicoya](./Caribbean_Central_America/Costa_Rica/20120905_M7.6_Nicoya)                | 7.6  |        15.4  | VII                          |
|  11 | Caribbean Central America | Costa Rica  |   2017 | [Puntarenas 2017](./Caribbean_Central_America/Costa_Rica/20171113_M6.5_Puntarenas)   | 6.5  |        22    | VIII                         |
|  12 | Caribbean Central America | El Salvador |   2001 | [Subduction 2001](./Caribbean_Central_America/El_Salvador/20010113_M7.7_Subduction)  | 7.7  |        39    | VIII                         |
|  13 | Caribbean Central America | El Salvador |   2001 | [San Vicente 2001](./Caribbean_Central_America/El_Salvador/20010213_M6.6_SanVicente) | 6.6  |        13    | VIII                         |
|  14 | Caribbean Central America | Haiti       |   2010 | [Haiti](./Caribbean_Central_America/Haiti/20100112_M7.0_Haiti)                       | 7    |        13    | IX                           |
|  15 | Caribbean Central America | Haiti       |   2021 | [Haiti](./Caribbean_Central_America/Haiti/20210814_M7.2_Haiti)                       | 7.2  |        10    | VIII                         |
|  16 | East Asia                 | Japan       |   1995 | [Kobe 1995](./East_Asia/Japan/19950117_M6.9_Kobe)                                    | 6.9  |        21.9  | IX                           |
|  17 | East Asia                 | Japan       |   2011 | [Tōhoku 2011](./East_Asia/Japan/20110311_M9.1_Tohoku)                                | 9.1  |        29    | VIII                         |
|  18 | East Asia                 | Japan       |   2016 | [Kumamoto 2016](./East_Asia/Japan/20160416_M7.0_Kumamoto)                            | 7    |        10    | IX                           |
|  19 | East Asia                 | Japan       |   2018 | [Osaka 2018](./East_Asia/Japan/20180618_M5.5_Osaka)                                  | 5.5  |        10.3  | VIII                         |
|  20 | East Asia                 | Japan       |   2018 | [HokkaidoEasternIburi 2018](./East_Asia/Japan/20180906_M6.6_HokkaidoEasternIburi)    | 6.6  |        35    | X                            |
|  21 | East Asia                 | Japan       |   2019 | [Yamagata 2019](./East_Asia/Japan/20190618_M6.4_Yamagata)                            | 6.4  |        12    | VII                          |
|  22 | Europe                    | Albania     |   2019 | [Durres](./Europe/Albania/20191126_M6.4_Albania)                                     | 6.4  |        22    | VIII                         |
|  23 | Europe                    | Croatia     |   2020 | [Zagreb 2020](./Europe/Croatia/20200322_M5.1_Zagreb)                                 | 5.3  |        10    | VIII                         |
|  24 | Europe                    | Croatia     |   2020 | [Petrijna 2020](./Europe/Croatia/20201229_M6.3_Petrijna)                             | 6.4  |        10    | IX                           |
|  25 | Europe                    | Cyprus      |   1996 | [Cyprus](./Europe/Cyprus/19961009_M6.8_Cyprus)                                       | 6.8  |        33    | VI                           |
|  26 | Europe                    | Greece      |   1981 | [GulfofCorinth 1981](./Europe/Greece/19810225_M6.4_GulfofCorinth)                    | 6.4  |        33    | IX                           |
|  27 | Europe                    | Greece      |   1981 | [GulfofCorinth 1981](./Europe/Greece/19810224_M6.7_GulfofCorinth)                    | 6.7  |        33    | IX                           |
|  28 | Europe                    | Greece      |   1981 | [GulfofCorinth 1981](./Europe/Greece/19810000_Sequence_GulfOfCorinth)                | 6.7  |        33    | IX                           |
|  29 | Europe                    | Greece      |   1986 | [Kalamata 1986](./Europe/Greece/19860913_M6.0_Kalamata)                              | 6    |        11.2  | VIII                         |
|  30 | Europe                    | Greece      |   1988 | [Elia 1988](./Europe/Greece/19881016_M5.88_Elia)                                     | 5.9  |        25.2  | VII                          |
|  31 | Europe                    | Greece      |   1995 | [Aigio 1995](./Europe/Greece/19950615_M6.4_Aigio)                                    | 6.5  |        14.2  | VIII                         |
|  32 | Europe                    | Greece      |   1995 | [KozaniGrevena 1995](./Europe/Greece/19950513_M6.5_KozaniGrevena)                    | 6.6  |        14    | VIII                         |
|  33 | Europe                    | Greece      |   1999 | [Athens 1999](./Europe/Greece/19990907_M5.9_Athens)                                  | 6    |        10    | IX                           |
|  34 | Europe                    | Greece      |   2014 | [Kefalonia 2014](./Europe/Greece/20140000_Sequence_Kefalonia)                        | 6.1  |         8    | VII                          |
|  35 | Europe                    | Greece      |   2014 | [Kefalonia 2014](./Europe/Greece/20140126_M6.1_Kefalonia)                            | 6.1  |         8    | VIII                         |
|  36 | Europe                    | Greece      |   2014 | [Kefalonia 2014](./Europe/Greece/20140203_M6.0_Kefalonia)                            | 6    |         5    | VII                          |
|  37 | Europe                    | Greece      |   2015 | [Lefkada 2015](./Europe/Greece/20151117_M6.5_Lefkada)                                | 6.5  |        11    | VIII                         |
|  38 | Europe                    | Greece      |   2017 | [AegeanSea 2017](./Europe/Greece/20170612_M6.3_AegeanSea)                            | 6.3  |        12    | VII                          |
|  39 | Europe                    | Iceland     |   2000 | [Iceland 2000](./Europe/Iceland/20000620_M6.46_Iceland)                              | 6.5  |        10    | IX                           |
|  40 | Europe                    | Iceland     |   2000 | [Iceland](./Europe/Iceland/20000617_M5.87_Iceland)                                   | 6.5  |        10    | VIII                         |
|  41 | Europe                    | Iceland     |   2008 | [Iceland 2008](./Europe/Iceland/20080529_M6.32_Iceland)                              | 6.3  |         9    | VIII                         |
|  42 | Europe                    | Italy       |   1980 | [Irpinia 1980](./Europe/Italy/19801123_M6.9_Irpinia)                                 | 6.9  |        10    | X                            |
|  43 | Europe                    | Italy       |   1990 | [Augusta 1990](./Europe/Italy/19901213_M5.61_Augusta)                                | 5.6  |        11.1  | VIII                         |
|  44 | Europe                    | Italy       |   1997 | [UmbriaMarche 1997](./Europe/Italy/19970926_M5.97_UmbriaMarche)                      | 6    |        10    | VIII                         |
|  45 | Europe                    | Italy       |   1997 | [UmbriaMarche 1997](./Europe/Italy/19971014_M5.86_UmbriaMarche)                      | 5.5  |        10    | VII                          |
|  46 | Europe                    | Italy       |   1997 | [UmbriaMarche 1997](./Europe/Italy/19970926_M5.72_UmbriaMarche)                      | 5.7  |        10    | VIII                         |
|  47 | Europe                    | Italy       |   1997 | [UmbriaMarche 1997](./Europe/Italy/19970000_Sequence_UmbriaMarche)                   | 5.7  |        10    | X                            |
|  48 | Europe                    | Italy       |   2002 | [Molise 2002](./Europe/Italy/20020000_Sequence_Molise)                               | 5.9  |        10    | VIII                         |
|  49 | Europe                    | Italy       |   2002 | [Molise 2002](./Europe/Italy/20021101_M5.72_Molise)                                  | 5.8  |        10    | VII                          |
|  50 | Europe                    | Italy       |   2002 | [Molise 2002](./Europe/Italy/20021031_M5.74_Molise)                                  | 5.9  |        10    | VII                          |
|  51 | Europe                    | Italy       |   2004 | [Gardone 2004](./Europe/Italy/20041124_M4.99_Gardone)                                | 5.1  |        17.2  | VIII                         |
|  52 | Europe                    | Italy       |   2009 | [Laquila 2009](./Europe/Italy/20090407_M5.4_Laquila)                                 | 5.5  |        15.1  | VI                           |
|  53 | Europe                    | Italy       |   2009 | [Laquila 2009](./Europe/Italy/20090000_Sequence_Laquila)                             | 6.3  |         8.8  | X                            |
|  54 | Europe                    | Italy       |   2009 | [Laquila 2009](./Europe/Italy/20090406_M6.18_Laquila)                                | 6.3  |         8.8  | VIII                         |
|  55 | Europe                    | Italy       |   2012 | [EmiliaRomagna 2012](./Europe/Italy/20120000_Sequence_EmiliaRomagna)                 | 6    |         6.3  | VIII                         |
|  56 | Europe                    | Italy       |   2012 | [EmiliaRomagna 2012](./Europe/Italy/20120520_M5.8_EmiliaRomagna)                     | 6    |         6.3  | VIII                         |
|  57 | Europe                    | Italy       |   2012 | [EmiliaRomagna 2012](./Europe/Italy/20120529_M5.6_EmiliaRomagna)                     | 5.8  |        10.2  | VIII                         |
|  58 | Europe                    | Italy       |   2016 | [CentralItaly](./Europe/Italy/20162017_Sequence_CentralItaly)                        | 6.6  |         4.44 | IX                           |
|  59 | Europe                    | Italy       |   2016 | [CentralItaly 2016](./Europe/Italy/20161030_M6.5_CentralItaly)                       | 6.6  |         8    | IX                           |
|  60 | Europe                    | Italy       |   2016 | [CentralItaly 2016](./Europe/Italy/20161026_M6.09_CentralItaly)                      | 6.1  |        10    | VIII                         |
|  61 | Europe                    | Italy       |   2016 | [CentralItaly 2016](./Europe/Italy/20160824_M6.21_CentralItaly)                      | 6.2  |         4.44 | IX                           |
|  62 | Europe                    | Italy       |   2017 | [CentralItaly 2017](./Europe/Italy/20170118_M5.95_CentralItaly)                      | 5.7  |         7    | VII                          |
|  63 | Europe                    | Netherlands |   1992 | [Roermond 1992](./Europe/Netherlands/19920413_M5.3_Roermond)                         | 5.4  |        21.2  | VIII                         |
|  64 | Europe                    | Romania     |   1990 | [Vrancea 1990](./Europe/Romania/19900530_M6.95_Vrancea)                              | 7    |        89.3  | VIII                         |
|  65 | Europe                    | Romania     |   1990 | [Vrancea 1990](./Europe/Romania/19900530_Sequence_Vrancea)                           | 7    |        89.3  | VIII                         |
|  66 | Europe                    | Romania     |   1990 | [Vrancea 1990](./Europe/Romania/19900531_M6.31_Vrancea)                              | 6.3  |        88.2  | V                            |
|  67 | Europe                    | Serbia      |   2010 | [Kraljevo](./Europe/Serbia/20101103_M5.52_Kraljevo)                                  | 5.5  |         0.9  | VI                           |
|  68 | Europe                    | Spain       |   2011 | [Lorca 2011](./Europe/Spain/20110511_M5.1_Lorca)                                     | 5.1  |         1    | VI                           |
|  69 | Europe                    | Turkey      |   1992 | [Erzincan](./Europe/Turkey/19920313_M6.68_Erzincan)                                  | 6.7  |        27.2  | VIII                         |
|  70 | Europe                    | Turkey      |   1995 | [Dinar](./Europe/Turkey/19951001_M6.42_Dinar)                                        | 6.4  |        33    | VIII                         |
|  71 | Europe                    | Turkey      |   1998 | [AdanaCeyhan 1998](./Europe/Turkey/19980627_M6.28_AdanaCeyhan)                       | 6.3  |        33    | VIII                         |
|  72 | Europe                    | Turkey      |   1999 | [Izmit](./Europe/Turkey/19990817_M7.53_Izmit)                                        | 7.6  |        17    | X                            |
|  73 | Europe                    | Turkey      |   1999 | [Duzce 1999](./Europe/Turkey/19991112_M6.71_Duzce)                                   | 7.2  |        10    | IX                           |
|  74 | Europe                    | Turkey      |   2011 | [Van 2011](./Europe/Turkey/20111023_M7.1_Van)                                        | 7.1  |        18    | VIII                         |
|  75 | Europe                    | Turkey      |   2020 | [AegeanSea 2020](./Europe/Turkey/20201030_M7_AegeanSea)                              | 7    |        21    | VIII                         |
|  76 | Europe                    | Turkey      |   2023 | [CentralTurkey 2023](./Europe/Turkey/20230206_M7.8_KahramanmarasGaziantep)           | 7.8  |        10    | XII                          |
|  77 | Middle East               | Iran        |   1978 | [Tabas](./Middle_East/Iran/19780916_M7.3_Tabas)                                      | 7.3  |        33    | IX                           |
|  78 | Middle East               | Iran        |   1990 | [Manjil-Rudbar](./Middle_East/Iran/19900620_M7.4_Manjil-Rudbar)                      | 7.4  |        18.5  | IX                           |
|  79 | Middle East               | Iran        |   1997 | [Golestan](./Middle_East/Iran/19970228_M6.1_Golestan)                                | 6.1  |        10    | VIII                         |
|  80 | Middle East               | Iran        |   1997 | [Qayen](./Middle_East/Iran/19970510_M7.2_Qayen)                                      | 7.2  |        10    | IX                           |
|  81 | Middle East               | Iran        |   2003 | [Bam](./Middle_East/Iran/20031226_M6.6_Bam)                                          | 6.6  |        10    | IX                           |
|  82 | Middle East               | Iran        |   2005 | [Zarand](./Middle_East/Iran/20050222_M6.5_Zarand)                                    | 6.5  |        14    | VIII                         |
|  83 | Middle East               | Iran        |   2012 | [Ahar-Varzaghan](./Middle_East/Iran/20120811_M6.2_Ahar-Varzaghan)                    | 6.2  |        12    | VIII                         |
|  84 | Middle East               | Iran        |   2012 | [Ahar-Varzaghan](./Middle_East/Iran/20120811_M6.4_Ahar-Varzaghan)                    | 6.4  |        11    | VII                          |
|  85 | Middle East               | Iran        |   2012 | [Ahar-Varzaghan](./Middle_East/Iran/20120000_Sequence_Ahar-Varzaghan)                | 6.4  |        11    | VII                          |
|  86 | Middle East               | Iran        |   2017 | [Sarpole-Zahab](./Middle_East/Iran/20171112_M7.3_SarpoleZahab)                       | 7.3  |        18.1  | IX                           |
|  87 | North America             | Mexico      |   1985 | [Mexico Michoacan ](./North_America/Mexico/19850919_M8.1_Michoacan)                  | 8.1  |        15    | VII                          |
|  88 | North America             | Mexico      |   1999 | [Oaxaca 1999](./North_America/Mexico/19990930_M7.4_Oaxaca)                           | 7.4  |        39    | VIII                         |
|  89 | North America             | Mexico      |   2017 | [Puebla 2017](./North_America/Mexico/20170919_M7.1_Puebla)                           | 7.1  |        51.2  | VIII                         |
|  90 | North America             | Mexico      |   2017 | [Chiapas 2017](./North_America/Mexico/20170908_M8.2_Chiapas)                         | 8.2  |        45.9  | VII                          |
|  91 | North America             | Mexico      |   2020 | [Oaxaca 2020](./North_America/Mexico/20200623_M7.4_Oaxaca)                           | 7.4  |        22.6  | VIII                         |
|  92 | North America             | Mexico      |   2021 | [Guerrero 2021](./North_America/Mexico/20210907_M7.1_Guerrero)                       | 7.1  |        10    | VIII                         |
|  93 | Oceania                   | Australia   |   1989 | [Newcastle](./Oceania/Australia/19891227_M5.4_Newcastle)                             | 5.4  |        10    | VIII                         |
|  94 | Oceania                   | New Zealand |   2010 | [Canterbury 2010](./Oceania/New_Zealand/20100904_M7.0_Canterbury)                    | 7    |        12    | VIII                         |
|  95 | Oceania                   | New Zealand |   2011 | [Christchurch 2011](./Oceania/New_Zealand/20110222_M6.1_Christchurch)                | 6.1  |         5.9  | IX                           |
|  96 | South America             | Chile       |   1960 | [Valdivia 1960](./South_America/Chile/19600522_M9.5_Valdivia)                        | 9.5  |        25    | IX                           |
|  97 | South America             | Chile       |   2010 | [Maule 2010](./South_America/Chile/20100227_M8.8_Maule)                              | 8.8  |        30    | VIII                         |
|  98 | South America             | Chile       |   2014 | [Iquique 2014](./South_America/Chile/20140401_M8.2_Iquique)                          | 8.2  |        38.9  | VIII                         |
|  99 | South America             | Chile       |   2015 | [Illapel 2015](./South_America/Chile/20150916_M8.3_Illapel)                          | 8.3  |        22.44 | VIII                         |
| 100 | South America             | Colombia    |   1983 | [Popayán 1983 ](./South_America/Colombia/19830331_M5.6_Popayan)                      | 5.6  |        15    | VIII                         |
| 101 | South America             | Colombia    |   1994 | [Cacua 1994](./South_America/Colombia/19940606_M6.8_Cauca)                           | 6.8  |        10    | IX                           |
| 102 | South America             | Colombia    |   1999 | [Armenia 1999](./South_America/Colombia/19990125_M6.1_Armenia)                       | 6.1  |        15    | IX                           |
| 103 | South America             | Colombia    |   2004 | [Pizarro 2004](./South_America/Colombia/20041115_M7.2_Pizarro)                       | 7.2  |        15    | VIII                         |
| 104 | South America             | Colombia    |   2008 | [Quetame 2008](./South_America/Colombia/20080524_M5.9_Quetame)                       | 5.9  |        10    | VII                          |
| 105 | South America             | Colombia    |   2023 | [El Calvario](./South_America/Colombia/20230817_M6.1_ElCalvario)                     | 6.1  |        10    | VII                          |
| 106 | South America             | Ecuador     |   2016 | [Pedernales 2016](./South_America/Ecuador/20160416_M7.8_Pedernales)                  | 7.8  |        17    | IX                           |
| 107 | South America             | Peru        |   2007 | [Pisco 2007](./South_America/Peru/20070815_M7.9_Pisco)                               | 7.9  |        40    | VIII                         |
| 108 | South Asia                | India       |   2011 | [Sikkim 2011](./South_Asia/India/20110918_M6.9_Sikkim)                               | 6.9  |        50    | VIII                         |
| 109 | South Asia                | Nepal       |   2015 | [Gorkha 2015](./South_Asia/Nepal/20150425_M7.8_Gorkha)                               | 7.8  |         8.22 | IX                           |
| 110 | South Asia                | Pakistan    |   2005 | [Kashmir](./South_Asia/Pakistan/20051008_M7.6_Kashmir)                               | 7.6  |        26    | IX                           |
| 111 | Southeast Asia            | Indonesia   |   2006 | [Yogyakarta](./Southeast_Asia/Indonesia/20060527_M6.4_Yogyakarta)                    | 6.4  |        12.5  | VIII                         |
| 112 | Southeast Asia            | Indonesia   |   2009 | [Padang ](./Southeast_Asia/Indonesia/20090930_M7.6_Padang)                           | 7.6  |        81    | VIII                         |

</details>

# 🚀 Model versions

Each version of the archive that is released can be accessed by changing from the `main` branch to the `tag` of a given version.
The `main` branch could contain the work-in-progress of the next version of the model.

| Version   | Release Notes                                                            |
|-----------|--------------------------------------------------------------------------|
| [v2023.0.0](https://github.com/gem/geid/tree/v2023.0.0) | First release with 100 earthquake scenario events.|

# 🌟 Contributors

The authors are grateful for the input from dozens of collaborators. 

# License
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

# 🤔 Frequently asked questions

### How to contribute?

You can follow the instructions indicated in the [contributing guidelines](./contribute_guidelines.md).

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

