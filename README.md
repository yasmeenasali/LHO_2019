# DRMI Lock Analysis

Scripts for downloading large chunks of data and plotting durations of DRMI locking attempts.

## Downloading Data

Large chunks of data can be downloaded with `geco_gwpy_dump.py` by running it in terminal. We recommended to run this on the cluster. The time window can be set in `jobspec.json` which is a file called by `geco_gwpy_dump.py` to specify the parameters of your desired data download. The `geco_gwpy_dump.py` script outputs a series of `HDF5` files with a max chunk length that determines how much data (in seconds) should be downloaded at once. For trends, you can specify second or minute trends.

The `jobspec.json` file already specifies the ISC\_LOCK channel and a max chunk length of 3600 seconds. 

To run the script:

`nohup ./geco_gwpy_dump.py &` 

To check on the progress of the download:

`./geco_gwpy_dump.py -p`

## Calculating Durations

Once all the `HDF5` files have been downloaded, you can generate a JSON file containing the durations and outcome of each locking attempt. Start by running the following to generate a list of filenames. 

`ls *.hdf5 > filenames.txt`

You will also need a JSON file called `durations.json` where the data will be appended. The contents of the file should be:

`{"time": [], "dur_suc": [], "dur_fail": []}`

Note that since data is appended to the JSON file, running the code more than once on the same `HDF5` files will create duplicate entries. Once you have `filenames.txt` and `durations.json` you can run the following script: 

`./get_DRMI_lock_stats.py`

## Plotting DRMI attempts

Using `durations.json`, you can generate plots with the `plot_DRMI_stats.ipynb` notebook. 








