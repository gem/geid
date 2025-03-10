# GROUND MOTION FIELDS USING OPENQUAKE

This folder includes the OpenQuake input files to generate scenario ground motion 
fields (gmfs) considering different sources of information:

1. From rupture.
1. From rupture and conditioned to recording stations (with only seismic stations or with seismic and macroseismic stations).
1. From ShakeMap.

The following files are available:

- `stationlist_seismic.csv`: OpenQuake input file with past observations, considering only seismic stations. If no seismic stations are available for the event, the file is not reported.
- `stationlist_all.csv`: OpenQuake input file with past observations, considering seismic and macroseismic stations. If no macroseismic stations are available for the event, the file is not reported.
- `site_model_stations.csv`: OpenQuake input file with the site model (Vs30 values) at the location of the observations.
- `site_model.csv`: OpenQuake input file with the site model for which the ground shaking will be estimated.
- `site_model.png`: Figure of the site model (Vs30 based on USGS data).
- `gmpe_logic_tree_*.xml`: OpenQuake input file with a ground motion model logic tree (gmlt).
- `job_stations_none.ini`: A configuration file (`job.ini`) for running OpenQuake scenario calculations without conditioning the ground shaking to given observations.
- `job_stations.ini`: A configuration file (`job.ini`) for running OpenQuake calculations when conditioning the ground shaking to given observations.

_NOTE: the configuration files are examples for a given rupture geometry and a given gmlt. These parameters can be adjusted to the preferred models._
## Median ground motion fields

The following images present the median ground motion field for the combination of rupture and GMPE that generates the lowest `nominal bias` when conditioning the ground shaking to observations. The folder [Sensitivity](./Sensitivity/) provides the summary of the sensitivity analysis carried out with the available ruptures and GMPEs.

<img src="median_gmf_stations_none.png" height="350">
<img src="median_gmf_stations_all.png" height="350">

## Sensitivity analysis

The following information is available in the `Sensitivity` folder :

- `calculation_summary.csv`: Details on the calculations carried out in the sensitivity analysis.
- `log_calc_*.txt`: File with the OpenQuake running information in a _.txt_ format. This file includes the `nominal bias` estimates for each GMPE present in the logic tree model.
- `gmf_median_PGA_*.csv`: Generated ground motion fields for PGA for a given calculation ID.

### Metadata in file `calculation_summary.csv`

- `calc_id`: unique identifier for the calculation.
- `description`: details on the calculation
- `cal_time`: time of the calculation.
- `recording_stations`: "All" stations (seismic + macroseismic), or only "seismic" stations.
- `gmlt`: Ground Motion Logic Tree used in the calculation.
- `rupture`: Rupture model used in the calculation.
- `gmpe`: Ground Motion Prediction Equation (ground motion model).
- `imt`: Intensity measure type.
- `max_gmv`: Maximum ground motion value.
- `nominal_bias_mean`: A single value useful as a measure of the event bias for a given gmpe. It refers to the mean of the between-event residuals after conditioning the shaking to the recording stations.
- `nominal_bias_stdev`: Standard deviation for the `nominal_bias_mean`.
- `abs_bias`: Absolute value of the `nominal_bias_mean`.


## To run an OpenQuake calculation
### 1. From Rupture

Start a calculation from a given rupture in OpenQuake `xml` format and combine it with a 
logic tree for the applicable GMPEs (ground motion prediction equations):

```
rupture + gmpe_logic_tree + job_stations_none.ini
```


### 2. From Rupture and conditional to recording stations

Condition the ground motion fields based on the recording stations available for the event
(`stationlist.csv` files). In this case, the calculation uses a given rupture in 
OpenQuake `xml` format, the observed values in the recording stations, and a given ground
motion model.

The conditioning of the ground motion can consider:
- The recording stations with only seismic stations.
- All recording stations (with seismic and macroseismic values).

```
rupture + gmpe_logic_tree + stationlist_seismic.csv + job_stations_seismic.ini
rupture + gmpe_logic_tree + stationlist_all.csv + job_stations_all.ini
```


### 3. From Shakemap

The gmfs computed from the USGS ShakeMap can be generated with the command

```
oq shakemap2gmfs {shakemap_id} {sites.csv} -n 0 -s 0 -t 0 --spatialcorr yes -c yes

example of shakemap_id: us2000ar20 
```

It is possible to specify the number of ground motion fields, the truncation level,
the spatial correlation, and the cross-correlation.

In OpenQuake, it is also possible to run scenario risk calculations starting from the USGS
ShakeMap.

