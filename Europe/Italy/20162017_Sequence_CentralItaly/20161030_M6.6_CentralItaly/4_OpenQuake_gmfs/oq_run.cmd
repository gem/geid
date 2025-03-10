oq engine --run job_no_stations.ini 
oq engine --sl -1 > log_calc_no_stations.txt
oq engine --run job_with_stations_all.ini
oq engine --sl -1 > log_calc_with_stations_all.txt
oq engine --run job_with_stations_seismic.ini
oq engine --sl -1 > log_calc_with_stations_seismic.txt
