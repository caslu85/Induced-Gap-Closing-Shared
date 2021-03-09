For full conductance matrix measurements, grr and glr  share a .dat file as well as gll and grl. 
The underscore denotes the data number referenced in the ppt.
The files have a list of parameters in the first row. Parameters *_set are the parameters swept in the scan.
Other parameters are the parameters measured
The second row of the .dat file contains the labels for the parameters in the first row.
The third row specifices the number of points for each _set parameter.
Starting from row four the data begins.
Note that gll corresponds to 'Conductance dIL/dVL'
Note that grr corresponds to 'Conductance dIR/dVR'
Note that grl corresponds to 'Conductance dIR/dVL'
Note that glr corresponds to 'Conductance dIL/dVR'
*important* while every file contains all conductance matrix entries. 
*important* The data shown in the main text shows grr and glr for the case the right bias has been sweept and 
*important* gll and grl for sweeping the left bias. So to replot the main text data (or data as presented in the ppt), 
*important* one needs to combine data from two .dat files
