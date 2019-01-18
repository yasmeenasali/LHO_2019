#! /usr/bin/env python
# (c) Yasmeen Asali, Ana Lam, Madox McGrae-Menge

import matplotlib
matplotlib.use('agg')
import h5py 
import matplotlib.pyplot as plt
import os, fnmatch
import numpy as np
import json

f = open('filenames.txt')
names = f.readlines()

files = []
for each_line in names:
    order = each_line.replace("\n", "").strip()
    files.append(order)

gps_time = []
suc = []
fail = []
for entry in files:
	gps = entry[0:10]
	gps_time.append(gps)
	f = h5py.File(entry, 'r')
	folder = list(f.keys())[0]
	data = f[folder].value
	num = 1
	dur_suc = []
	dur_fail = []
	size=len(data)-2
	for idx in range(0,size): 
    		val1 = data[idx]
    		val2 = data[idx +1]
    		if val1 == 101 and val2 == 101:
        		num += 1
    		elif val1 == 101 and val2 == 102:
        		num = float(num)
        		time = num/float(16)
        		dur_suc.append(time)
        		num = 1
    		elif val1 == 101 and val2<val1:
        		num = float(num)
        		time = num/float(16)
        		dur_fail.append(time)
			num = 1
	dur_suc = np.array(dur_suc)
	dur_fail = np.array(dur_fail)
	avg_time_suc = np.mean(dur_suc)
	avg_time_fail = np.mean(dur_fail)
	suc.append(avg_time_suc)
	fail.append(avg_time_fail)
	f.close()

with open("durations.json", "r") as f:
    obj=json.load(f)
new = {"time": gps_time, "dur_suc": suc, "dur_fail": fail}
for key in obj:
    obj[key] = obj[key] + new[key]
with open("durations.json", "w") as f:
    json.dump(obj,f)

