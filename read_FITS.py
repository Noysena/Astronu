#! /urs/env python3:
import os
import sys
import glob
import json
import numpy as np
from astropy.io import fits

info = "Read FITS and export dictionary and dump to json format"

folder = os.path.join(sys.argv[1], "*.fits")
filelist = glob.glob(folder)
gws={}
for i in filelist:
    with fits.open(i) as hdul:
        hd = hdul[0].header
        center = {hd["FILENAME"] : {"FOV" : 999,
				    "RA" : np.round(hd["RA"], 4),
				    "DEC" : np.round(hd["DEC"], 4),
				    "SNAME": hd["SNAME"],
				    "DATE-OBS" : hd["DATE-OBS"]}}
    print(center)
    gws.update(center)

#Build JSON and write to file
dumpjs = json.dumps(gws)
textname = os.path.basename(sys.argv[1]) + '.txt'
with open(textname, 'w') as rj:
	rj.write(gws)
