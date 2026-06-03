
<div align='center'>
<p align="center">
    <img src="https://cloud-storage.globalquakemodel.org/public/Logos/GEM-LOGO-Red-RGB-300DPI.jpg" alt="GEM Foundation" width="300"/>
</p>
<a href='#-database-coverage'>
    <img src='https://img.shields.io/badge/Coverage-green?style=for-the-badge'>
</a>
<a href='#-methodology-highlights'>
    <img src='https://img.shields.io/badge/Contribute-blue?style=for-the-badge'>
</a>
<a href='./LICENSE.txt'>
    <img src='https://img.shields.io/badge/LICENSE-lightgrey?style=for-the-badge'>
</a>
</div>

# 🔎 Global Earthquake Adjusted Impacts Database for the Verification of Loss Models (GEAID)

The calibration of earthquake loss models typically involves repeating past events and comparing the estimated and observed losses. This process requires updating past economic losses into current values, considering changes in construction costs, building counts, and the vulnerability of the built environment. In this study, we perform a thorough literature review to identify the key drivers influencing the cost of destructive events throughout time and select several methodologies that enable adjusting historical losses considering several socio-economic factors. Then, we propose a novel methodology that integrates satellite imagery, data regarding design regulations, and economic trends to adjust the economic impact from past earthquakes. We apply this methodology to a suite of 462 seismic events since 1975. 

The database of adjusted Impacts is available in this public repository and can be used to support modelers in testing and calibrating earthquake loss models.

> The v1.0.0 release for the Global Earthquake Adjusted Impacts Database (GEAID) is available! 🥳 🚀 This repository hosts the most up-to-date version of data for the countries all around the world.

<div align='center'>
    <img src="../~GEAID/global_shakemap_pga.png" alt="Events" width="700"/>
</div>

---

## 📐 Methodology Highlights

The GEAID methodology adjusts historical earthquake losses to present-day conditions by accounting for three main components:

- Changes in economic costs (inflation)
- Changes in exposure (built environment growth)
- Changes in vulnerability (construction practices and seismic design improvements)

The adjusted loss is calculated as:

Loss_n = Loss_h × (CPI_s / CPI_t) × Built-Up Growth × VRF

where:

* **Lossₙ** = normalized (adjusted) economic loss
* **Lossₕ** = reported historical economic loss
* **CPIₛ** = Consumer Price Index for the target year
* **CPIₜ** = Consumer Price Index for the event year
* **Built-Up Growth** = ratio of built-up surface between the target year and the event year
* **VRF** = Vulnerability Reduction Factor accounting for changes in seismic design practice and building code implementation

This framework combines traditional economic normalization approaches with geospatial measurements of urban expansion and a vulnerability adjustment component, enabling a more realistic representation of how earthquake risk evolves over time.

The resulting dataset provides adjusted losses for hundreds of damaging earthquakes worldwide and is designed for use in seismic risk model calibration, validation, and scenario testing.

# 🌍 Country list
The following countries are covered in this repository. 

| COUNTRY        | ISO_3 |
|----------------|-------|
| China          | CHN   |
| Italy          | ITA   |
| Japan          | JPN   |
| United States  | USA   |
| Türkiye        | TUR   |
| Chile          | CHL   |
| Mexico         | MEX   |
| Taiwan         | TWN   |
| New Zealand    | NZL   |
| Guatemala      | GTM   |
| El Salvador    | SLV   |
| Iran           | IRN   |
| Pakistan       | PAK   |
| India          | IND   |
| Greece         | GRC   |
| Nepal          | NPL   |
| Ecuador        | ECU   |
| Indonesia      | IDN   |
| Colombia       | COL   |
| Philippines    | PHL   |
| Peru           | PER   |
| Puerto Rico    | PRI   |
| South Korea    | KOR   |

</details>

The following events are available. Additionally, a global summary of adjusted impact data can be found in the [GEAID folder](../~GEAID/adjusted_economic_losses.csv).

<details>
<summary> List with available events
</summary>


|   Number | EMDAT IDs     | Country       | ISO3   |   Latitude |   Longitude |   Year |   Month |   Day |   Magnitude |
|---------:|:--------------|:--------------|:-------|-----------:|------------:|-------:|--------:|------:|------------:|
|        1 | 1975-0053-TUR | Turkey        | TUR    |    38.474  |     40.723  |   1975 |       9 |     6 |        6.7  |
|        2 | 1975-0155-USA | United States | USA    |    42.06   |   -122.55   |   1975 |       3 |    27 |        6    |
|        3 | 1976-0024-GTM | Guatemala     | GTM    |    15.324  |    -89.101  |   1976 |       2 |     4 |        7.5  |
|        4 | 1976-0033-ECU | Ecuador       | ECU    |     0.782  |     79.804  |   1976 |       4 |     9 |        6.7  |
|        5 | 1976-0037-ITA | Italy         | ITA    |    46.356  |     13.275  |   1976 |       5 |     6 |        6.5  |
|        6 | 1976-0043-IDN | Indonesia     | IDN    |    -4.603  |    140.091  |   1976 |       6 |    26 |        7.1  |
|        7 | 1976-0047-IDN | Indonesia     | IDN    |    -8.17   |    114.888  |   1976 |       7 |    14 |        6.5  |
|        8 | 1976-0054-PHL | Philippines   | PHL    |     6.262  |    124.023  |   1976 |       8 |    17 |        7.9  |
|        9 | 1976-0068-ECU | Ecuador       | ECU    |    -0.14   |    -78.3    |   1976 |      10 |     4 |      nan    |
|       10 | 1976-0075-TUR | Turkey        | TUR    |    39.121  |     44.029  |   1976 |      11 |    24 |        7.3  |
|       11 | 1977-0050-PHL | Philippines   | PHL    |    16.773  |    122.327  |   1977 |       3 |    19 |        7    |
|       12 | 1977-0106-IDN | Indonesia     | IDN    |   -11.164  |    118.378  |   1977 |       8 |    19 |        8.3  |
|       13 | 1978-0080-JPN | Japan         | JPN    |    38.19   |    142.028  |   1978 |       6 |    12 |        7.7  |
|       14 | 1978-0081-GRC | Greece        | GRC    |    40.739  |     23.229  |   1978 |       6 |    20 |        6.4  |
|       15 | 1978-0115-IRN | Iran          | IRN    |    33.386  |     57.434  |   1978 |       9 |    16 |        7.4  |
|       16 | 1979-0032-MEX | Mexico        | MEX    |    17.813  |   -101.276  |   1979 |       3 |    14 |        7.6  |
|       17 | 1979-0054-IDN | Indonesia     | IDN    |    -8.21   |    115.95   |   1979 |       5 |    30 |        6.1  |
|       18 | 1979-0102-IDN | Indonesia     | IDN    |    -7.656  |    108.252  |   1979 |      11 |     2 |        6.1  |
|       19 | 1979-0106-COL | Colombia      | COL    |     4.805  |    -76.217  |   1979 |      11 |    23 |        6.7  |
|       20 | 1979-0113-COL | Colombia      | COL    |     1.598  |    -79.358  |   1979 |      12 |    12 |        7.7  |
|       21 | 1980-0071-NPL | Nepal         | NPL    |    29.598  |     81.092  |   1980 |       7 |    29 |        6.5  |
|       22 | 1980-0092-JPN | Japan         | JPN    |    35.45   |    139.964  |   1980 |       9 |    25 |        6.2  |
|       23 | 1980-0097-MEX | Mexico        | MEX    |    18.211  |    -98.24   |   1980 |      10 |    24 |        6.7  |
|       24 | 1980-0100-PER | Peru          | PER    |   -13.347  |    -74.545  |   1980 |      11 |    12 |        4.9  |
|       25 | 1980-0103-ITA | Italy         | ITA    |    40.914  |     15.366  |   1980 |      11 |    23 |        6.9  |
|       26 | 1980-0108-IRN | Iran          | IRN    |    34.587  |     50.652  |   1980 |      12 |    19 |        5.8  |
|       27 | 1980-0109-IRN | Iran          | IRN    |    34.503  |     50.59   |   1980 |      12 |    22 |        5.2  |
|       28 | 1980-0239-GRC | Greece        | GRC    |    39.203  |     22.729  |   1980 |       7 |    12 |        6.3  |
|       29 | 1981-0025-IDN | Indonesia     | IDN    |    -4.576  |    139.232  |   1981 |       1 |    19 |        6.8  |
|       30 | 1981-0033-GRC | Greece        | GRC    |    38.222  |     22.934  |   1981 |       2 |    24 |        6.7  |
|       31 | 1981-0056-IRN | Iran          | IRN    |    29.913  |     57.715  |   1981 |       6 |    11 |        6.7  |
|       32 | 1981-0067-IRN | Iran          | IRN    |    30.013  |     57.794  |   1981 |       7 |    28 |        7.1  |
|       33 | 1981-0081-PAK | Pakistan      | PAK    |    35.693  |     73.594  |   1981 |       9 |    12 |        6.2  |
|       34 | 1981-0091-COL | Colombia      | COL    |     8.117  |    -72.527  |   1981 |      10 |    18 |        5.4  |
|       35 | 1981-0224-ITA | Italy         | ITA    |    41.051  |     14.601  |   1981 |       2 |    14 |        4.6  |
|       36 | 1982-0031-IDN | Indonesia     | IDN    |     4.374  |     97.755  |   1982 |       2 |    24 |        5.4  |
|       37 | 1982-0036-JPN | Japan         | JPN    |    42.158  |    142.361  |   1982 |       3 |    21 |        6.7  |
|       38 | 1982-0081-SLV | El Salvador   | SLV    |    13.332  |    -89.387  |   1982 |       6 |    19 |        7.3  |
|       39 | 1982-0106-ITA | Italy         | ITA    |    43.164  |     12.586  |   1982 |      10 |    17 |        4.4  |
|       40 | 1982-0128-IDN | Indonesia     | IDN    |    -8.405  |    123.08   |   1982 |      12 |    25 |        5.9  |
|       41 | 1982-0293-PER | Peru          | PER    |   -12.69   |    -76.065  |   1982 |       3 |    28 |        6.1  |
|       42 | 1983-0058-IRN | Iran          | IRN    |    35.953  |     52.264  |   1983 |       3 |    26 |        4.9  |
|       43 | 1983-0059-COL | Colombia      | COL    |     2.461  |    -76.686  |   1983 |       3 |    31 |        4.9  |
|       44 | 1983-0067-IDN | Indonesia     | IDN    |     5.723  |     94.722  |   1983 |       4 |     3 |        6.9  |
|       45 | 1983-0070-PER | Peru          | PER    |    -4.843  |    -78.103  |   1983 |       4 |    12 |        5.2  |
|       46 | 1983-0109-PHL | Philippines   | PHL    |    18.231  |    120.86   |   1983 |       8 |    18 |        6.5  |
|       47 | 1983-0127-CHL | Chile         | CHL    |   -26.535  |    -70.563  |   1983 |      10 |     4 |        7.4  |
|       48 | 1983-0136-TUR | Turkey        | TUR    |    40.33   |     42.187  |   1983 |      10 |    30 |        6.8  |
|       49 | 1983-0174-USA | United States | USA    |    36.219  |   -120.317  |   1983 |       5 |     2 |        5.2  |
|       50 | 1983-0197-USA | United States | USA    |    19.43   |   -155.454  |   1983 |      11 |    16 |        6.4  |
|       51 | 1983-0432-IRN | Iran          | IRN    |    36.948  |     49.18   |   1983 |       7 |    22 |        5.5  |
|       52 | 1983-0514-USA | United States | USA    |    44.058  |   -113.857  |   1983 |      10 |    28 |        6.9  |
|       53 | 1984-0015-IDN | Indonesia     | IDN    |    -2.823  |    118.806  |   1984 |       1 |     8 |        6.4  |
|       54 | 1984-0038-ITA | Italy         | ITA    |    43.26   |     12.558  |   1984 |       4 |    29 |        5.8  |
|       55 | 1984-0072-IDN | Indonesia     | IDN    |    -1.3    |     98      |   1984 |       8 |    27 |        5.2  |
|       56 | 1984-0084-JPN | Japan         | JPN    |    36.39   |    138.1    |   1984 |       9 |    14 |        6.9  |
|       57 | 1985-0041-CHL | Chile         | CHL    |   -33.135  |    -71.871  |   1985 |       3 |     3 |        8    |
|       58 | 1985-0078-PAK | Pakistan      | PAK    |    36.19   |     70.896  |   1985 |       7 |    29 |        7.4  |
|       59 | 1985-0109-MEX | Mexico        | MEX    |    18.19   |   -102.533  |   1985 |       9 |    19 |        8    |
|       60 | 1986-0051-PER | Peru          | PER    |   -13.32   |    -71.57   |   1986 |       4 |     5 |        5.8  |
|       61 | 1986-0113-GRC | Greece        | GRC    |    37.02   |     22.07   |   1986 |       9 |    13 |        5.6  |
|       62 | 1986-0123-SLV | El Salvador   | SLV    |    13.4    |    -89.1    |   1986 |      10 |    10 |        7.5  |
|       63 | 1986-0177-USA | United States | USA    |    32.978  |   -117.858  |   1986 |       7 |    13 |        5.6  |
|       64 | 1986-0372-IND | India         | IND    |    32.128  |     76.374  |   1986 |       4 |    26 |        5.3  |
|       65 | 1987-0068-NZL | New Zealand   | NZL    |   -37.965  |    176.765  |   1987 |       3 |     2 |        6.5  |
|       66 | 1987-0070-ECU | Ecuador       | ECU    |     0.151  |    -77.785  |   1987 |       3 |     5 |        7.2  |
|       67 | 1987-0144-CHL | Chile         | CHL    |   -19.022  |    -69.991  |   1987 |       8 |     8 |        7.2  |
|       68 | 1987-0179-USA | United States | USA    |    34.061  |   -118.079  |   1987 |      10 |     1 |        5.9  |
|       69 | 1987-0213-IDN | Indonesia     | IDN    |    -8.247  |    124.155  |   1987 |      11 |    26 |        6.7  |
|       70 | 1987-0254-USA | United States | USA    |    33.013  |    115.838  |   1987 |      11 |    24 |        6.6  |
|       71 | 1988-0382-IND | India         | IND    |    26.755  |     86.616  |   1988 |       8 |    21 |        6.9  |
|       72 | 1988-0383-NPL | Nepal         | NPL    |    26.755  |     86.616  |   1988 |       8 |    20 |        6.7  |
|       73 | 1988-0502-CHN | China         | CHN    |    22.789  |     99.611  |   1988 |      11 |     6 |        7.6  |
|       74 | 1989-0081-CHN | China         | CHN    |    29.987  |     99.195  |   1989 |       4 |    15 |        6.4  |
|       75 | 1989-0133-USA | United States | USA    |    37.036  |   -121.88   |   1989 |      10 |    18 |        6.9  |
|       76 | 1989-0155-CHN | China         | CHN    |    23.553  |     99.526  |   1989 |       5 |     7 |        5.6  |
|       77 | 1990-0009-PHL | Philippines   | PHL    |     9.725  |    124.625  |   1990 |       2 |     8 |        6.6  |
|       78 | 1990-0029-PER | Peru          | PER    |    -6.016  |    -77.229  |   1990 |       5 |    29 |        6.6  |
|       79 | 1990-0034-IRN | Iran          | IRN    |    36.961  |     49.414  |   1990 |       6 |    21 |        7.3  |
|       80 | 1990-0040-PHL | Philippines   | PHL    |    15.658  |    121.227  |   1990 |       7 |    16 |        7.7  |
|       81 | 1990-0099-CHN | China         | CHN    |    35.986  |    100.245  |   1990 |       4 |    26 |        6.9  |
|       82 | 1990-0118-IRN | Iran          | IRN    |    28.251  |     55.462  |   1990 |      11 |     6 |        6.6  |
|       83 | 1990-0187-USA | United States | USA    |    34.14   |   -117.7    |   1990 |       2 |    28 |        5.5  |
|       84 | 1990-0189-PAK | Pakistan      | PAK    |    28.925  |     66.331  |   1990 |       3 |     4 |        6.1  |
|       85 | 1990-0250-ITA | Italy         | ITA    |    37.3    |     15.438  |   1990 |      12 |    13 |        4.7  |
|       86 | 1990-0593-IDN | Indonesia     | IDN    |     3.908  |     97.457  |   1990 |      11 |    15 |        6    |
|       87 | 1991-0033-PAK | Pakistan      | PAK    |    38.993  |     70.423  |   1991 |       1 |    31 |        6.4  |
|       88 | 1991-0165-IDN | Indonesia     | IDN    |    -8.099  |    125.681  |   1991 |       7 |     4 |        6.7  |
|       89 | 1991-0192-USA | United States | USA    |    34.1    |   -118.09   |   1991 |       6 |    28 |        5.8  |
|       90 | 1991-0368-IND | India         | IND    |    30.78   |     78.774  |   1991 |      10 |    20 |        6.1  |
|       91 | 1992-0022-TUR | Turkey        | TUR    |    39.71   |     39.605  |   1992 |       3 |    13 |        6.8  |
|       92 | 1992-0120-USA | United States | USA    |    40.415  |   -124.603  |   1992 |       4 |    25 |        6.9  |
|       93 | 1992-0163-IDN | Indonesia     | IDN    |    -8.482  |    121.93   |   1992 |      12 |    12 |        7.5  |
|       94 | 1992-0215-USA | United States | USA    |    34      |   -118.15   |   1992 |       6 |    28 |        7.4  |
|       95 | 1992-0256-CHN | China         | CHN    |    29.41   |     91.1    |   1992 |       7 |    31 |        6.5  |
|       96 | 1992-0554-USA | United States | USA    |    33.961  |   -116.32   |   1992 |       4 |    22 |        6.2  |
|       97 | 1993-0074-IND | India         | IND    |    16.4    |     74.2    |   1993 |       9 |    29 |        6.4  |
|       98 | 1993-0097-JPN | Japan         | JPN    |    43.3    |    143.691  |   1993 |       1 |    15 |        7.5  |
|       99 | 1993-0480-USA | United States | USA    |    42.314  |   -122.01   |   1993 |       9 |    21 |        5.8  |
|      100 | 1994-0002-USA | United States | USA    |     0.34   |     30.12   |   1994 |       1 |    17 |        6.6  |
|      101 | 1994-0007-IDN | Indonesia     | IDN    |    -4.967  |    104.302  |   1994 |       2 |    16 |        7.2  |
|      102 | 1994-0040-IRN | Iran          | IRN    |    30.853  |     60.596  |   1994 |       2 |    23 |        6.1  |
|      103 | 1994-0059-COL | Colombia      | COL    |    30      |    -76.2    |   1994 |       6 |     6 |        6.4  |
|      104 | 1994-0062-IDN | Indonesia     | IDN    |   -10.2    |     13.2    |   1994 |       6 |     2 |        7.2  |
|      105 | 1994-0316-JPN | Japan         | JPN    |    40.5    |    143.4    |   1994 |      12 |    28 |        7.5  |
|      106 | 1994-0518-PHL | Philippines   | PHL    |    13.352  |    121.087  |   1994 |      11 |    15 |        7.1  |
|      107 | 1994-0599-USA | United States | USA    |    34.17   |   -118.27   |   1994 |      12 |    26 |        5.3  |
|      108 | 1995-0016-JPN | Japan         | JPN    |    34.58   |    135      |   1995 |       1 |    17 |        7.2  |
|      109 | 1995-0085-GRC | Greece        | GRC    |    40.1    |     21.6    |   1995 |       5 |    13 |        6.6  |
|      110 | 1995-0148-CHN | China         | CHN    |    21.966  |     99.196  |   1995 |       7 |    12 |        7.1  |
|      111 | 1995-0171-CHL | Chile         | CHL    |   -23.34   |    -70.36   |   1995 |       7 |    30 |        7.8  |
|      112 | 1995-0203-MEX | Mexico        | MEX    |    16.8    |    -98.6    |   1995 |       9 |    14 |        7.2  |
|      113 | 1995-0233-TUR | Turkey        | TUR    |    38      |     30.1    |   1995 |      10 |     1 |        6.1  |
|      114 | 1995-0261-CHN | China         | CHN    |    25.9    |    102.2    |   1995 |      10 |    24 |        6.1  |
|      115 | 1995-0437-GRC | Greece        | GRC    |    38.4    |     22.2    |   1995 |       6 |    15 |        6.3  |
|      116 | 1996-0002-IDN | Indonesia     | IDN    |     0.729  |    119.931  |   1996 |       1 |     1 |        7    |
|      117 | 1996-0021-CHN | China         | CHN    |    25.04   |    102.41   |   1996 |       2 |     3 |        7    |
|      118 | 1996-0061-IDN | Indonesia     | IDN    |     1.1    |    137.15   |   1996 |       2 |    17 |        7.5  |
|      119 | 1996-0062-ECU | Ecuador       | ECU    |    -0.68   |     78.3    |   1996 |       3 |    28 |        5.7  |
|      120 | 1996-0136-CHN | China         | CHN    |    39.28   |     76.44   |   1996 |       3 |    19 |        6.9  |
|      121 | 1996-0461-TUR | Turkey        | TUR    |    40.754  |     35.34   |   1996 |       8 |    14 |      nan    |
|      122 | 1997-0017-IRN | Iran          | IRN    |    37.661  |     57.291  |   1997 |       2 |     4 |        5.6  |
|      123 | 1997-0035-IRN | Iran          | IRN    |    38.075  |     48.05   |   1997 |       2 |    28 |        6    |
|      124 | 1997-0095-IRN | Iran          | IRN    |    33.825  |     59.809  |   1997 |       5 |    10 |        7.3  |
|      125 | 1997-0115-IND | India         | IND    |    23.083  |     80.041  |   1997 |       5 |    22 |        6    |
|      126 | 1997-0228-ITA | Italy         | ITA    |    43      |     13      |   1997 |       9 |    26 |        5.5  |
|      127 | 1997-0240-IDN | Indonesia     | IDN    |    -4      |    119.4    |   1997 |       9 |    28 |        6    |
|      128 | 1997-0247-CHL | Chile         | CHL    |   -30.933  |    -71.22   |   1997 |      10 |    14 |        6.8  |
|      129 | 1998-0076-CHN | China         | CHN    |    41.083  |    114.5    |   1998 |       1 |    10 |        6.2  |
|      130 | 1998-0201-TUR | Turkey        | TUR    |     3.878  |     35.307  |   1998 |       6 |    28 |        6.3  |
|      131 | 1998-0384-CHN | China         | CHN    |    27.308  |    101.029  |   1998 |      11 |    19 |        5.6  |
|      132 | 1998-0403-IDN | Indonesia     | IDN    |    -2.071  |    124.891  |   1998 |      11 |    29 |        7.7  |
|      133 | 1998-0454-CHN | China         | CHN    |    26.373  |    104.021  |   1998 |      12 |     1 |        4.5  |
|      134 | 1999-0016-COL | Colombia      | COL    |     4.461  |    -75.724  |   1999 |       1 |    25 |        6.2  |
|      135 | 1999-0099-IND | India         | IND    |    30.512  |     79.403  |   1999 |       3 |    28 |        6.6  |
|      136 | 1999-0208-MEX | Mexico        | MEX    |    18.386  |    -97.436  |   1999 |       6 |    15 |        6.5  |
|      137 | 1999-0268-TUR | Turkey        | TUR    |    40.748  |     29.864  |   1999 |       8 |    17 |        7.6  |
|      138 | 1999-0302-GRC | Greece        | GRC    |    38.119  |     23.605  |   1999 |       9 |     7 |        5.8  |
|      139 | 1999-0321-TWN | Taiwan        | TWN    |    23.772  |    120.982  |   1999 |       9 |    21 |        7.7  |
|      140 | 1999-0360-MEX | Mexico        | MEX    |    16.1    |     96.7    |   1999 |       9 |    30 |        7.5  |
|      141 | 1999-0405-TWN | Taiwan        | TWN    |    23.445  |    120.506  |   1999 |      10 |    22 |        5.9  |
|      142 | 1999-0434-PER | Peru          | PER    |   -13.64   |    -74.43   |   1999 |      10 |    31 |        4.4  |
|      143 | 1999-0449-TUR | Turkey        | TUR    |    40.758  |     31.161  |   1999 |      11 |    12 |        7.2  |
|      144 | 1999-0455-CHN | China         | CHN    |    39.899  |    113.983  |   1999 |      11 |     1 |        5.6  |
|      145 | 1999-0568-IDN | Indonesia     | IDN    |    -6.845  |    105.555  |   1999 |      12 |    21 |        6.5  |
|      146 | 1999-0644-PHL | Philippines   | PHL    |    15.766  |    119.74   |   1999 |      12 |    12 |        7.3  |
|      147 | 2000-0033-CHN | China         | CHN    |    25.607  |    101.063  |   2000 |       1 |    14 |        5.9  |
|      148 | 2000-0036-CHN | China         | CHN    |    24.263  |    103.797  |   2000 |       1 |    26 |        4.9  |
|      149 | 2000-0230-IDN | Indonesia     | IDN    |    -1.105  |    123.573  |   2000 |       5 |     4 |        7.6  |
|      150 | 2000-0293-IDN | Indonesia     | IDN    |    -4.646  |    102.102  |   2000 |       6 |     4 |        6.7  |
|      151 | 2000-0449-IDN | Indonesia     | IDN    |    -6.675  |    106.845  |   2000 |       7 |    12 |        5.4  |
|      152 | 2000-0527-CHN | China         | CHN    |    25.826  |    102.194  |   2000 |       8 |    21 |        4.9  |
|      153 | 2000-0598-USA | United States | USA    |    38.3788 |   -122.413  |   2000 |       9 |     3 |        4.9  |
|      154 | 2000-0656-JPN | Japan         | JPN    |    35.456  |    133.134  |   2000 |      10 |     6 |        6.7  |
|      155 | 2001-0013-SLV | El Salvador   | SLV    |    13.049  |    -88.66   |   2001 |       1 |    13 |        7.7  |
|      156 | 2001-0023-GTM | Guatemala     | GTM    |    13.049  |    -88.66   |   2001 |       1 |    13 |        7.7  |
|      157 | 2001-0033-IND | India         | IND    |    23.419  |     70.232  |   2001 |       1 |    26 |        7.7  |
|      158 | 2001-0033-PAK | Pakistan      | PAK    |    23.419  |     70.232  |   2001 |       1 |    26 |        7.7  |
|      159 | 2001-0042-SLV | El Salvador   | SLV    |    13.671  |    -88.938  |   2001 |       2 |    13 |        6.6  |
|      160 | 2001-0064-CHN | China         | CHN    |    29.513  |    101.129  |   2001 |       2 |    23 |        5.6  |
|      161 | 2001-0099-USA | United States | USA    |    47.149  |   -122.727  |   2001 |       2 |    28 |        6.8  |
|      162 | 2001-0123-JPN | Japan         | JPN    |    34.083  |    132.526  |   2001 |       3 |    24 |        6.8  |
|      163 | 2001-0151-CHN | China         | CHN    |    24.768  |     99.061  |   2001 |       4 |    12 |        5.6  |
|      164 | 2001-0214-CHN | China         | CHN    |    27.689  |    101.003  |   2001 |       5 |    23 |        5.5  |
|      165 | 2002-0065-TUR | Turkey        | TUR    |    38.573  |     31.271  |   2002 |       2 |     3 |        6.5  |
|      166 | 2002-0129-PHL | Philippines   | PHL    |     6.033  |    124.249  |   2002 |       3 |     5 |        7.5  |
|      167 | 2002-0172-TWN | Taiwan        | TWN    |    24.279  |    122.179  |   2002 |       3 |    31 |        7.1  |
|      168 | 2002-0378-IRN | Iran          | IRN    |    35.626  |     49.047  |   2002 |       6 |    22 |        6.5  |
|      169 | 2002-0690-ITA | Italy         | ITA    |    41.789  |     14.872  |   2002 |      10 |    31 |        5.9  |
|      170 | 2002-0882-ITA | Italy         | ITA    |    38.381  |     13.701  |   2002 |       9 |     6 |        6    |
|      171 | 2003-0039-MEX | Mexico        | MEX    |    18.77   |   -104.104  |   2003 |       1 |    22 |        7.6  |
|      172 | 2003-0105-CHN | China         | CHN    |    39.61   |     77.23   |   2003 |       2 |    24 |        6.3  |
|      173 | 2003-0184-ITA | Italy         | ITA    |    44.792  |      8.892  |   2003 |       4 |    11 |        5    |
|      174 | 2003-0197-TUR | Turkey        | TUR    |    39.007  |     40.464  |   2003 |       5 |     1 |        6.4  |
|      175 | 2003-0249-JPN | Japan         | JPN    |    38.849  |    141.568  |   2003 |       5 |    26 |        7    |
|      176 | 2003-0348-CHN | China         | CHN    |    25.975  |    101.29   |   2003 |       7 |    21 |        6    |
|      177 | 2003-0354-JPN | Japan         | JPN    |    38.432  |    141.003  |   2003 |       7 |    25 |        5.5  |
|      178 | 2003-0402-CHN | China         | CHN    |    43.77   |    119.643  |   2003 |       8 |    16 |        5.4  |
|      179 | 2003-0438-IRN | Iran          | IRN    |    28.355  |     54.169  |   2003 |       7 |    10 |        5.8  |
|      180 | 2003-0476-JPN | Japan         | JPN    |    41.774  |    143.593  |   2003 |       9 |    25 |        7.4  |
|      181 | 2003-0509-CHN | China         | CHN    |    25.954  |    101.254  |   2003 |      10 |    16 |        5.6  |
|      182 | 2003-0519-CHN | China         | CHN    |    38.383  |    100.975  |   2003 |      10 |    25 |        5.8  |
|      183 | 2003-0582-CHN | China         | CHN    |    42.905  |     80.515  |   2003 |      12 |     1 |        6    |
|      184 | 2003-0623-USA | United States | USA    |    35.7005 |   -121.1    |   2003 |      12 |    22 |        6.5  |
|      185 | 2003-0630-IRN | Iran          | IRN    |    28.995  |     58.311  |   2003 |      12 |    26 |        6.6  |
|      186 | 2004-0001-IDN | Indonesia     | IDN    |    -8.31   |    115.788  |   2004 |       1 |     1 |        5.8  |
|      187 | 2004-0040-IDN | Indonesia     | IDN    |    -3.615  |    135.538  |   2004 |       2 |     5 |        7    |
|      188 | 2004-0126-CHN | China         | CHN    |    45.382  |    118.256  |   2004 |       3 |    24 |        5.5  |
|      189 | 2004-0234-IRN | Iran          | IRN    |    36.29   |     51.61   |   2004 |       5 |    28 |        6.3  |
|      190 | 2004-0406-CHN | China         | CHN    |    27.266  |    103.873  |   2004 |       8 |    10 |        5.4  |
|      191 | 2004-0532-JPN | Japan         | JPN    |    37.226  |    138.779  |   2004 |      10 |    23 |        6.6  |
|      192 | 2004-0607-IDN | Indonesia     | IDN    |    -3.609  |    135.404  |   2004 |      11 |    26 |        7.1  |
|      193 | 2005-0092-IRN | Iran          | IRN    |    30.754  |     56.816  |   2005 |       2 |    22 |        6.4  |
|      194 | 2005-0129-JPN | Japan         | JPN    |    33.807  |    130.131  |   2005 |       3 |    20 |        6.6  |
|      195 | 2005-0321-CHL | Chile         | CHL    |   -19.987  |    -69.197  |   2005 |       6 |    13 |        7.8  |
|      196 | 2005-0321-PER | Peru          | PER    |   -19.987  |    -69.197  |   2005 |       6 |    13 |        7.8  |
|      197 | 2005-0575-IND | India         | IND    |    34.539  |     73.588  |   2005 |      10 |     8 |        7.6  |
|      198 | 2005-0575-PAK | Pakistan      | PAK    |    34.539  |     73.588  |   2005 |      10 |     8 |        7.6  |
|      199 | 2006-0061-CHN | China         | CHN    |    23.282  |    101.693  |   2006 |       1 |    12 |        4.6  |
|      200 | 2006-0153-IRN | Iran          | IRN    |    33.5    |     48.78   |   2006 |       3 |    31 |        6.1  |
|      201 | 2006-0279-IDN | Indonesia     | IDN    |    -7.961  |    110.446  |   2006 |       5 |    26 |        6.3  |
|      202 | 2006-0620-CHN | China         | CHN    |    43.469  |    119.558  |   2006 |      11 |     3 |        4.7  |
|      203 | 2006-0704-USA | United States | USA    |    19.878  |   -155.935  |   2006 |      10 |    15 |        6.7  |
|      204 | 2007-0087-IDN | Indonesia     | IDN    |    -0.488  |    100.53   |   2007 |       3 |     6 |        6.3  |
|      205 | 2007-0101-JPN | Japan         | JPN    |    37.336  |    136.588  |   2007 |       3 |    25 |        6.7  |
|      206 | 2007-0217-CHN | China         | CHN    |    23.028  |    101.052  |   2007 |       6 |     2 |        6.1  |
|      207 | 2007-0258-JPN | Japan         | JPN    |    37.535  |    138.446  |   2007 |       7 |    16 |        6.6  |
|      208 | 2007-0362-PER | Peru          | PER    |   -13.386  |    -76.603  |   2007 |       8 |    15 |        8    |
|      209 | 2007-0440-IDN | Indonesia     | IDN    |    -4.438  |    101.367  |   2007 |       9 |    12 |        8.4  |
|      210 | 2007-0587-CHL | Chile         | CHL    |   -22.247  |    -69.89   |   2007 |      11 |    14 |        7.7  |
|      211 | 2008-0192-CHN | China         | CHN    |    31.002  |    103.322  |   2008 |       5 |    12 |        7.9  |
|      212 | 2008-0242-JPN | Japan         | JPN    |    39.03   |    140.881  |   2008 |       6 |    13 |        6.9  |
|      213 | 2008-0275-JPN | Japan         | JPN    |    39.802  |    141.464  |   2008 |       7 |    23 |        6.8  |
|      214 | 2008-0374-CHN | China         | CHN    |    26.241  |    101.889  |   2008 |       8 |    30 |        6    |
|      215 | 2008-0500-PAK | Pakistan      | PAK    |    30.639  |     67.351  |   2008 |      10 |    28 |        6.4  |
|      216 | 2008-0649-COL | Colombia      | COL    |     4.33   |    -73.764  |   2008 |       5 |    24 |        5.9  |
|      217 | 2009-0001-IDN | Indonesia     | IDN    |    -0.414  |    132.885  |   2009 |       1 |     3 |        7.7  |
|      218 | 2009-0059-CHN | China         | CHN    |    43.236  |     80.893  |   2009 |       1 |    25 |        5.1  |
|      219 | 2009-0112-IDN | Indonesia     | IDN    |     3.886  |    126.387  |   2009 |       2 |    11 |        7.2  |
|      220 | 2009-0136-ITA | Italy         | ITA    |    42.334  |     13.334  |   2009 |       4 |     6 |        6.3  |
|      221 | 2009-0249-CHN | China         | CHN    |    25.632  |    101.095  |   2009 |       7 |     9 |        5.7  |
|      222 | 2009-0354-IDN | Indonesia     | IDN    |    -7.782  |    107.297  |   2009 |       9 |     2 |        7    |
|      223 | 2009-0404-PHL | Philippines   | PHL    |     6.513  |    124.715  |   2009 |       9 |    18 |        5.7  |
|      224 | 2009-0421-IDN | Indonesia     | IDN    |    -8.207  |    118.631  |   2009 |       9 |    30 |        6.6  |
|      225 | 2009-0479-IDN | Indonesia     | IDN    |    -0.72   |     99.867  |   2009 |      11 |     8 |        7.6  |
|      226 | 2010-0027-USA | United States | USA    |    40.652  |   -124.692  |   2010 |       1 |    10 |        6.5  |
|      227 | 2010-0064-CHN | China         | CHN    |    30.268  |    105.668  |   2010 |       1 |    30 |        5.1  |
|      228 | 2010-0091-CHL | Chile         | CHL    |   -36.122  |    -72.898  |   2010 |       2 |    27 |        8.8  |
|      229 | 2010-0158-MEX | Mexico        | MEX    |    32.2862 |   -115.295  |   2010 |       4 |     4 |        7.2  |
|      230 | 2010-0169-CHN | China         | CHN    |    33.165  |     96.548  |   2010 |       4 |    14 |        6.9  |
|      231 | 2010-0463-NZL | New Zealand   | NZL    |   -43.522  |    171.83   |   2010 |       9 |     4 |        7    |
|      232 | 2010-0668-TWN | Taiwan        | TWN    |    22.918  |    120.795  |   2010 |       3 |     4 |        6.3  |
|      233 | 2011-0068-NZL | New Zealand   | NZL    |   -43.583  |    172.68   |   2011 |       2 |    22 |        6.1  |
|      234 | 2011-0079-CHN | China         | CHN    |    24.727  |     97.957  |   2011 |       3 |    10 |        5.5  |
|      235 | 2011-0082-JPN | Japan         | JPN    |    38.297  |    142.373  |   2011 |       3 |    11 |        9.1  |
|      236 | 2011-0170-TUR | Turkey        | TUR    |    39.149  |     29.103  |   2011 |       5 |    19 |        5.8  |
|      237 | 2011-0388-NZL | New Zealand   | NZL    |   -43.564  |    172.743  |   2011 |       6 |    13 |        5.9  |
|      238 | 2011-0389-IDN | Indonesia     | IDN    |     2.965  |     97.893  |   2011 |       9 |     5 |        6.7  |
|      239 | 2011-0397-TUR | Turkey        | TUR    |    38.721  |     43.508  |   2011 |      10 |    23 |        7.1  |
|      240 | 2011-0411-CHN | China         | CHN    |    43.648  |     82.437  |   2011 |      11 |     1 |        5.6  |
|      241 | 2012-0031-PHL | Philippines   | PHL    |     9.999  |    123.206  |   2012 |       2 |     6 |        6.7  |
|      242 | 2012-0124-MEX | Mexico        | MEX    |    16.493  |    -98.231  |   2012 |       3 |    20 |        7.4  |
|      243 | 2012-0126-CHL | Chile         | CHL    |   -35.2    |    -72.217  |   2012 |       3 |    25 |        7.1  |
|      244 | 2012-0142-ITA | Italy         | ITA    |    44.89   |     11.23   |   2012 |       5 |    20 |        6    |
|      245 | 2012-0190-CHN | China         | CHN    |    27.767  |    100.781  |   2012 |       6 |    24 |        5.5  |
|      246 | 2012-0275-IRN | Iran          | IRN    |    38.329  |     46.826  |   2012 |       8 |    11 |        6.4  |
|      247 | 2012-0338-CHN | China         | CHN    |    43.433  |     84.7    |   2012 |       6 |    29 |        6.3  |
|      248 | 2012-0350-CHN | China         | CHN    |    27.575  |    103.983  |   2012 |       9 |     7 |        5.5  |
|      249 | 2012-0407-GTM | Guatemala     | GTM    |    13.988  |    -91.895  |   2012 |      11 |     7 |        7.4  |
|      250 | 2012-0431-PHL | Philippines   | PHL    |    10.811  |    126.638  |   2012 |       8 |    31 |        7.6  |
|      251 | 2012-0536-CHN | China         | CHN    |    38.745  |     88.098  |   2012 |      12 |     7 |        5.3  |
|      252 | 2012-0604-CHN | China         | CHN    |    39.383  |     81.307  |   2012 |       3 |     9 |        5.9  |
|      253 | 2013-0058-COL | Colombia      | COL    |     1.135  |    -77.393  |   2013 |       2 |     9 |        6.9  |
|      254 | 2013-0081-CHN | China         | CHN    |    25.98   |     99.812  |   2013 |       3 |     3 |        5.2  |
|      255 | 2013-0098-IRN | Iran          | IRN    |    28.428  |     51.593  |   2013 |       4 |     9 |        6.4  |
|      256 | 2013-0116-CHN | China         | CHN    |    30.308  |    102.888  |   2013 |       4 |    20 |        6.6  |
|      257 | 2013-0140-IND | India         | IND    |    33.061  |     75.863  |   2013 |       5 |     1 |        5.7  |
|      258 | 2013-0206-TWN | Taiwan        | TWN    |    23.789  |    121.141  |   2013 |       6 |     2 |        6.2  |
|      259 | 2013-0235-IDN | Indonesia     | IDN    |     4.645  |     96.665  |   2013 |       7 |     2 |        6.1  |
|      260 | 2013-0242-CHN | China         | CHN    |    34.512  |    104.262  |   2013 |       7 |    22 |        5.9  |
|      261 | 2013-0268-NZL | New Zealand   | NZL    |   -41.704  |    174.337  |   2013 |       7 |    21 |        6.5  |
|      262 | 2013-0314-CHN | China         | CHN    |    28.2425 |     99.3502 |   2013 |       8 |    31 |        5.6  |
|      263 | 2013-0381-PAK | Pakistan      | PAK    |    26.951  |     65.5009 |   2013 |       9 |    24 |        7.7  |
|      264 | 2013-0395-PHL | Philippines   | PHL    |     9.8796 |    124.117  |   2013 |      10 |    15 |        7.1  |
|      265 | 2013-0405-GTM | Guatemala     | GTM    |    14.6056 |    -92.1207 |   2013 |       9 |     7 |        6.4  |
|      266 | 2013-0555-CHN | China         | CHN    |    31.066  |    110.412  |   2013 |      12 |    16 |        5.1  |
|      267 | 2013-0561-TWN | Taiwan        | TWN    |    23.828  |    121.215  |   2013 |       3 |    27 |        5.9  |
|      268 | 2013-0563-CHN | China         | CHN    |    25.953  |     99.782  |   2013 |       4 |    17 |        5.1  |
|      269 | 2014-0049-GRC | Greece        | GRC    |    38.2082 |     20.4528 |   2014 |       1 |    26 |        6.1  |
|      270 | 2014-0054-IRN | Iran          | IRN    |    27.1502 |     54.4482 |   2014 |       1 |     2 |        5.2  |
|      271 | 2014-0086-CHN | China         | CHN    |    35.9053 |     82.5864 |   2014 |       2 |    12 |        6.9  |
|      272 | 2014-0094-CHL | Chile         | CHL    |   -19.61   |    -70.769  |   2014 |       4 |     1 |        8.2  |
|      273 | 2014-0129-CHN | China         | CHN    |    28.174  |    103.619  |   2014 |       4 |     4 |        5.4  |
|      274 | 2014-0173-CHN | China         | CHN    |    24.974  |     97.844  |   2014 |       5 |    24 |        5.8  |
|      275 | 2014-0174-GRC | Greece        | GRC    |    40.2893 |     25.3889 |   2014 |       5 |    24 |        6.9  |
|      276 | 2014-0177-CHN | China         | CHN    |    24.9997 |     97.845  |   2014 |       5 |    30 |        5.9  |
|      277 | 2014-0281-CHN | China         | CHN    |    27.1891 |    103.409  |   2014 |       8 |     3 |        6.2  |
|      278 | 2014-0287-IRN | Iran          | IRN    |    32.5827 |     47.7037 |   2014 |       8 |    18 |        6    |
|      279 | 2014-0318-USA | United States | USA    |    38.2152 |   -122.312  |   2014 |       8 |    24 |        6.02 |
|      280 | 2014-0449-CHN | China         | CHN    |    23.3834 |    100.47   |   2014 |      10 |     7 |        6.1  |
|      281 | 2014-0464-CHN | China         | CHN    |    30.3398 |    101.737  |   2014 |      11 |    22 |        5.9  |
|      282 | 2014-0465-JPN | Japan         | JPN    |    36.6408 |    137.887  |   2014 |      11 |    22 |        6.2  |
|      283 | 2015-0078-CHN | China         | CHN    |    44.133  |     85.568  |   2015 |       2 |    22 |        5.1  |
|      284 | 2015-0125-CHN | China         | CHN    |    23.566  |     98.854  |   2015 |       3 |     1 |        5.2  |
|      285 | 2015-0144-NPL | Nepal         | NPL    |    28.23   |     84.731  |   2015 |       4 |    25 |        7.8  |
|      286 | 2015-0271-CHN | China         | CHN    |    37.4593 |     78.1542 |   2015 |       7 |     3 |        6.4  |
|      287 | 2016-0002-IND | India         | IND    |    24.804  |     93.65   |   2016 |       1 |     3 |        6.7  |
|      288 | 2016-0043-TWN | Taiwan        | TWN    |    22.938  |    120.6    |   2016 |       2 |     6 |        6.4  |
|      289 | 2016-0107-JPN | Japan         | JPN    |    32.788  |    130.7    |   2016 |       4 |    14 |        6.5  |
|      290 | 2016-0117-ECU | Ecuador       | ECU    |     0.382  |    -79.92   |   2016 |       4 |    16 |        7.8  |
|      291 | 2016-0121-JPN | Japan         | JPN    |    32.791  |    130.75   |   2016 |       4 |    16 |        7.3  |
|      292 | 2016-0313-ITA | Italy         | ITA    |    42.723  |     13.187  |   2016 |       8 |    24 |        6.2  |
|      293 | 2016-0341-KOR | South Korea   | KOR    |    35.781  |    129.216  |   2016 |       9 |    12 |        5.4  |
|      294 | 2016-0357-ITA | Italy         | ITA    |    42.934  |     13.043  |   2016 |      10 |    26 |        6.1  |
|      295 | 2016-0358-ITA | Italy         | ITA    |    42.855  |     13.088  |   2016 |      10 |    30 |        6.5  |
|      296 | 2016-0475-IDN | Indonesia     | IDN    |     5.281  |     96.108  |   2016 |      12 |     7 |        6.5  |
|      297 | 2016-0480-CHN | China         | CHN    |    39.238  |     74.047  |   2016 |      11 |    25 |        6.6  |
|      298 | 2016-0492-JPN | Japan         | JPN    |    35.37   |    133.812  |   2016 |      10 |    21 |        6.2  |
|      299 | 2016-0493-USA | United States | USA    |    35.991  |    -96.803  |   2016 |      11 |     7 |        5    |
|      300 | 2016-0526-CHN | China         | CHN    |    43.823  |     86.345  |   2016 |      12 |     8 |        5.9  |
|      301 | 2016-0536-CHN | China         | CHN    |    26.077  |     99.539  |   2016 |       5 |    18 |        4.8  |
|      302 | 2017-0015-ITA | Italy         | ITA    |    42.601  |     13.227  |   2017 |       1 |    18 |        5.3  |
|      303 | 2017-0050-PHL | Philippines   | PHL    |     9.907  |    125.452  |   2017 |       2 |    10 |        6.7  |
|      304 | 2017-0113-CHN | China         | CHN    |   nan      |    nan      |   2017 |       3 |    26 |        5    |
|      305 | 2017-0124-CHN | China         | CHN    |   nan      |    nan      |   2017 |       5 |    11 |        5.4  |
|      306 | 2017-0140-PHL | Philippines   | PHL    |    13.77   |    120.935  |   2017 |       4 |     8 |        5.9  |
|      307 | 2017-0204-IRN | Iran          | IRN    |    37.772  |     57.204  |   2017 |       5 |    13 |        5.6  |
|      308 | 2017-0247-PHL | Philippines   | PHL    |    11.111  |    124.619  |   2017 |       7 |     6 |        6.5  |
|      309 | 2017-0331-CHN | China         | CHN    |    33.193  |    103.855  |   2017 |       8 |     8 |        6.5  |
|      310 | 2017-0382-MEX | Mexico        | MEX    |    15.022  |    -93.899  |   2017 |       9 |     8 |        8.1  |
|      311 | 2017-0387-MEX | Mexico        | MEX    |    18.55   |    -98.489  |   2017 |       9 |    17 |        7.1  |
|      312 | 2017-0446-IRN | Iran          | IRN    |    34.911  |     45.959  |   2017 |      11 |    12 |        7.3  |
|      313 | 2018-0031-IDN | Indonesia     | IDN    |    -7.196  |    105.918  |   2018 |       1 |    23 |        6    |
|      314 | 2018-0059-TWN | Taiwan        | TWN    |    24.136  |    121.658  |   2018 |       2 |     6 |        6.4  |
|      315 | 2018-0183-JPN | Japan         | JPN    |    34.826  |    135.64   |   2018 |       6 |    18 |        5.5  |
|      316 | 2018-0215-CHN | China         | CHN    |    45.279  |    124.557  |   2018 |       5 |    28 |        5.1  |
|      317 | 2018-0254-IDN | Indonesia     | IDN    |    -8.274  |    116.491  |   2018 |       7 |    29 |        6.4  |
|      318 | 2018-0257-IDN | Indonesia     | IDN    |    -8.287  |    116.452  |   2018 |       8 |     5 |        6.9  |
|      319 | 2018-0281-IRN | Iran          | IRN    |    34.645  |     46.179  |   2018 |       7 |    22 |        5.9  |
|      320 | 2018-0302-IDN | Indonesia     | IDN    |    -8.325  |    116.577  |   2018 |       8 |    19 |        6.9  |
|      321 | 2018-0323-CHN | China         | CHN    |    24.332  |    102.941  |   2018 |       8 |    13 |        5    |
|      322 | 2018-0330-JPN | Japan         | JPN    |   nan      |    nan      |   2018 |       9 |     6 |        6.6  |
|      323 | 2018-0426-IRN | Iran          | IRN    |    34.304  |     45.74   |   2018 |      11 |    25 |        6.3  |
|      324 | 2019-0096-CHN | China         | CHN    |    29.498  |    104.632  |   2019 |       2 |    25 |        4.9  |
|      325 | 2019-0162-PHL | Philippines   | PHL    |    14.99   |    120.35   |   2019 |       4 |    22 |        6.1  |
|      326 | 2019-0259-CHN | China         | CHN    |    28.405  |    104.957  |   2019 |       6 |    17 |        5.8  |
|      327 | 2019-0306-USA | United States | USA    |    35.77   |   -117.599  |   2019 |       7 |     5 |        7.1  |
|      328 | 2019-0362-PHL | Philippines   | PHL    |    20.807  |    121.986  |   2019 |       7 |    27 |        6    |
|      329 | 2019-0460-PAK | Pakistan      | PAK    |    33.106  |     73.766  |   2019 |       9 |    24 |        5.6  |
|      330 | 2019-0553-IRN | Iran          | IRN    |    37.808  |     47.558  |   2019 |      11 |     8 |        5.9  |
|      331 | 2020-0007-PRI | Puerto Rico   | PRI    |    17.935  |    -66.883  |   2020 |       1 |     7 |        6.4  |
|      332 | 2020-0034-TUR | Turkey        | TUR    |    38.39   |     44.367  |   2020 |       1 |    24 |        6.7  |
|      333 | 2020-0158-PRI | Puerto Rico   | PRI    |    17.937  |    -66.727  |   2020 |       5 |     2 |        5.4  |
|      334 | 2020-0244-CHN | China         | CHN    |    27.296  |    103.281  |   2020 |       5 |    18 |        5.1  |
|      335 | 2020-0281-MEX | Mexico        | MEX    |    15.916  |    -95.953  |   2020 |       6 |    23 |        7.4  |
|      336 | 2020-0370-PHL | Philippines   | PHL    |    12.021  |    124.123  |   2020 |       8 |    18 |        6.6  |
|      337 | 2020-0466-TUR | Turkey        | TUR    |    37.913  |     26.779  |   2020 |      10 |    30 |        7    |
|      338 | 2021-0003-IDN | Indonesia     | IDN    |    -2.976  |    118.901  |   2021 |       1 |    15 |        6.2  |
|      339 | 2021-0095-IRN | Iran          | IRN    |   nan      |    nan      |   2021 |       2 |    17 |        5.6  |
|      340 | 2021-0105-JPN | Japan         | JPN    |    37.745  |    141.749  |   2021 |       2 |    13 |        7.1  |
|      341 | 2021-0134-GRC | Greece        | GRC    |    39.789  |     22.119  |   2021 |       3 |     3 |        5.8  |
|      342 | 2021-0194-JPN | Japan         | JPN    |    38.475  |    141.633  |   2021 |       3 |    20 |        7    |
|      343 | 2021-0201-CHN | China         | CHN    |    41.816  |     81.164  |   2021 |       3 |    24 |        5.4  |
|      344 | 2021-0293-CHN | China         | CHN    |    25.761  |    100.011  |   2021 |       5 |    21 |        6.1  |
|      345 | 2021-0587-CHN | China         | CHN    |    29.182  |    105.391  |   2021 |       9 |    16 |        5.4  |
|      346 | 2021-0602-MEX | Mexico        | MEX    |    16.982  |    -99.773  |   2021 |       9 |     8 |        7    |
|      347 | 2021-0627-GRC | Greece        | GRC    |    35.252  |     25.26   |   2021 |       9 |    27 |        6    |
|      348 | 2021-0738-IRN | Iran          | IRN    |    27.721  |     56.065  |   2021 |      11 |    14 |        6.3  |
|      349 | 2021-0829-CHN | China         | CHN    |   nan      |    nan      |   2021 |      12 |    24 |        5.7  |
|      350 | 2022-0004-CHN | China         | CHN    |   nan      |    nan      |   2022 |       1 |     2 |        5.4  |
|      351 | 2022-0042-IDN | Indonesia     | IDN    |    -6.86   |    105.289  |   2022 |       1 |    14 |        6.6  |
|      352 | 2022-0045-CHN | China         | CHN    |    37.828  |    101.29   |   2022 |       1 |     8 |        6.6  |
|      353 | 2022-0115-IDN | Indonesia     | IDN    |     0.216  |    100.096  |   2022 |       2 |    25 |        6.1  |
|      354 | 2022-0153-JPN | Japan         | JPN    |    37.702  |    141.587  |   2022 |       3 |    16 |        7.3  |
|      355 | 2022-0334-CHN | China         | CHN    |    30.395  |    102.958  |   2022 |       6 |     1 |        5.8  |
|      356 | 2022-0402-IRN | Iran          | IRN    |    26.899  |     55.321  |   2022 |       7 |     2 |        6.1  |
|      357 | 2022-0448-PHL | Philippines   | PHL    |    17.56   |    120.801  |   2022 |       7 |    27 |        7    |
|      358 | 2022-0567-CHN | China         | CHN    |    29.726  |    102.279  |   2022 |       9 |     5 |        6.6  |
|      359 | 2022-0611-TWN | Taiwan        | TWN    |    23.119  |    121.422  |   2022 |       9 |    18 |        6.5  |
|      360 | 2022-0623-MEX | Mexico        | MEX    |    18.497  |   -102.982  |   2022 |       9 |    19 |        7.6  |
|      361 | 2022-0703-PHL | Philippines   | PHL    |    17.662  |    120.823  |   2022 |      10 |    25 |        6.4  |
|      362 | 2022-0765-TUR | Turkey        | TUR    |    40.847  |     30.967  |   2022 |      11 |    23 |        6.1  |
|      363 | 2022-0808-USA | United States | USA    |    40.525  |    124.423  |   2022 |      12 |    20 |        6.4  |
|      364 | 2023-0012-IRN | Iran          | IRN    |    38.44   |     44.946  |   2023 |       1 |    18 |        5.7  |
|      365 | 2023-0047-IRN | Iran          | IRN    |    38.424  |     44.909  |   2023 |       1 |    28 |        5.9  |
|      366 | 2023-0054-TUR | Turkey        | TUR    |    38.055  |     36.51   |   2023 |       2 |     6 |        7.8  |
|      367 | 2023-0268-CHN | China         | CHN    |   nan      |    nan      |   2023 |       5 |     2 |        5.3  |
|      368 | 2023-0522-CHN | China         | CHN    |    37.231  |    116.391  |   2023 |       8 |     5 |        5.4  |
|      369 | 2023-0722-NPL | Nepal         | NPL    |    28.848  |     82.18   |   2023 |      11 |     3 |        5.7  |
|      370 | 2023-0762-PHL | Philippines   | PHL    |     5.583  |    125.022  |   2023 |      11 |    17 |        6.7  |
|      371 | 2023-0791-PHL | Philippines   | PHL    |     8.527  |    126.449  |   2023 |      12 |     2 |        7.6  |
|      372 | 2023-0838-CHN | China         | CHN    |    35.743  |    102.827  |   2023 |      12 |    19 |        5.9  |
|      373 | 2024-0001-JPN | Japan         | JPN    |    37.495  |    137.265  |   2024 |       1 |     1 |        7.5  |
|      374 | 2024-0035-CHN | China         | CHN    |    41.219  |     78.724  |   2024 |       1 |    23 |        5.6  |
|      375 | 2024-0154-IDN | Indonesia     | IDN    |    -5.867  |    112.362  |   2024 |       3 |    22 |        6.4  |
|      376 | 2024-0189-TWN | Taiwan        | TWN    |    23.819  |    121.562  |   2024 |       4 |     3 |        7.4  |
|      377 | 2024-0688-IDN | Indonesia     | IDN    |   nan      |    nan      |   2024 |       9 |    18 |        5.1  |
|      378 | 2025-0004-CHN | China         | CHN    |    28.573  |     87.375  |   2025 |       1 |     7 |        7.1  |
|      379 | 2025-0041-TWN | Taiwan        | TWN    |    23.234  |    120.475  |   2025 |       1 |    21 |        6    |
|      380 | 2025-0293-TUR | Turkey        | TUR    |   nan      |    nan      |   2025 |       4 |    23 |        6.2  |
</details>



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
    <div style="display: flex; align-items: center; gap: 50px;">
        <img src="../World/EN_FundedbytheEU_RGB_NEG.png" alt="EU Funded" width="250" style="border: none; outline: none;"/>
        <img src="../World/Geo-INQUIRE_logo_2_crop.jpg" alt="Geo-INQUIRE" width="150" style="border: none; outline: none;"/>
    </div>
</div>



# 🤔 Frequently asked questions

### Which version am I seeing? How to change the version?

By default, you will see the files in the repository in the `main` branch. Each version of the model that is released can be accessed is marked with a `tag`. By changing the tag version at the top of the repository, you can see the files for a given version.

Note that the `main` branch could contain the work-in-progress of the next version of the model.


# References

1. Brooks, H. E., & Doswell, C. A. (2001). *Normalized Damage from Major Tornadoes in the United States: 1890–1999*. Weather and Forecasting, 16(1), 168-176. Boston, MA, USA: American Meteorological Society. DOI: 10.1175/1520-0434(2001)016<0168:NDFMTI>2.0.CO;2.
2. Daniell, J. E., Wenzel, F., & Khazai, B. (2012). *The normalisation of socio-economic losses from historic worldwide earthquakes*. Center for Disaster Management and Risk Reduction Technology (CEDIM). Retrieved from: https://www.researchgate.net/publication/258434298
3. Delforge, D., Wathelet, V., Below, R., Sofia, C. L., Tonnelier, M., Loenhout, J. V., & Speybroeck, N. (2023). *EM-DAT: The Emergency Events Database*. DOI: 10.21203/rs.3.rs-3807553/v1.
4. Dollet, C., & Guéguen, P. (2022). *Global occurrence models for human and economic losses due to earthquakes (1967-2018) considering exposed GDP and population*. Natural Hazards, 110(1), 349-372. DOI: 10.1007/s11069-021-04950-z.
5. Hadavi, M., Sun, L., & Romanic, D. (2022). *Normalized insured losses caused by windstorms in Quebec and Ontario, Canada, in the period 2008-2021*. International Journal of Disaster Risk Reduction, 80. DOI: 10.1016/j.ijdrr.2022.103222.
6. McAneney, J., Sandercock, B., Crompton, R., Mortlock, T., Musulin, R., Pielke, R., & Gissing, A. (2019). *Normalised insurance losses from Australian natural disasters*. Environmental Hazards, 18(5), 414-433. DOI: 10.1080/17477891.2019.1609406.
7. McAneney, J., Timms, M., Browning, S., Somerville, P., & Crompton, R. (2022). *Normalised New Zealand natural disaster insurance losses: 1968-2019*. Environmental Hazards, 21(1), 58-76. DOI: 10.1080/17477891.2021.1905595.
8. Miller, S., Muir-Wood, R., & Boissonnade, A. (2008). *An exploration of trends in normalized weather-related catastrophe losses*. In H. F. Diaz & R. J. Murnane (Eds.), *Climate Extremes and Society* (pp. 225-247). Cambridge: Cambridge University Press. DOI: 10.1017/CBO9780511535840.015.
9. Neumayer, E., & Barthel, F. (2011). *Normalizing economic loss from natural disasters: A global analysis*. Global Environmental Change, 21(1), 13-24. DOI: 10.1016/j.gloenvcha.2010.10.004.
10. Pielke, R. A., Gratz, J., Landsea, C. W., Collins, D., Saunders, M. A., & Musulin, R. (2008). *Normalized Hurricane Damage in the United States: 1900-2005*. Natural Hazards Review, 9(1), 29-42. DOI: 10.1061/(ASCE)1527-6988(2008)9:1(29).
11. Pielke, R. A., & Landsea, C. W. (1998). *Normalized Hurricane Damages in the United States: 1925-95*.
12. Pielke, R. A., Rubiera, J., Landsea, C., Fernández, M. L., & Klein, R. (2003). *Hurricane Vulnerability in Latin America and the Caribbean: Normalized Damage and Loss Potentials*. Natural Hazards Review, 4(3), 101-114. DOI: 10.1061/(ASCE)1527-6988(2003)4:3(101).
13. Schmidt, S., Kemfert, C., & Höppe, P. (2009). *Tropical cyclone losses in the USA and the impact of climate change: A trend analysis based on data from a new approach to adjusting storm losses*. Environmental Impact Assessment Review, 29(6), 359-369. DOI: 10.1016/j.eiar.2009.03.003.
14. Simmons, K. M., Sutter, D., & Pielke, R. (2013). *Normalized tornado damage in the United States: 1950-2011*. Environmental Hazards, 12(2), 132-147. DOI: 10.1080/17477891.2012.738642.
15. Vranes, K., & Pielke, R. (2009). *Normalized Earthquake Damage and Fatalities in the United States: 1900-2005*. DOI: 10.1061/ASCE1527-6988200910:384.