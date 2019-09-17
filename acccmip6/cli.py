import argparse

from acccmip6.access_cm import SearchCmip6
from acccmip6.download_dat import DownloadCmip6

def main():

    parser = argparse.ArgumentParser()
    
    parser.add_argument("-dir", help="Download directory.", default=None)
    parser.add_argument("-o","--output-options", help="S for 'Searching' or D for 'Downloading'.", required=True)
    parser.add_argument("-m", help="Model names", default=None)
    parser.add_argument("-e", help="Experiment names", default=None)
    parser.add_argument("-v", help="Variable names", default=None)
    parser.add_argument("-f", help="Output frequency", default=None)
    parser.add_argument("-r", help="Output realm", default=None)
    parser.add_argument("-rlzn", help="Select realization", default=None)
    parser.add_argument("-c", help="Checker: yes to check inputs", default=None)
    parser.add_argument("-desc", help="Description: yes to print out experiment description", default=None)
	
    args = parser.parse_args()
    model = args.m
    experiment = args.e
    variable = args.v
    frequency = args.f
    realm = args.r
    check = args.c
    rlzn = args.rlzn
    desc = args.desc
    out = args.output_options
    dl_dir = args.dir
    if (out == 'S'):
        SearchCmip6(model=model, experiment=experiment, variable=variable, frequency=frequency, realm=realm, check=check, desc=desc)
    elif (out == 'D'):
        DownloadCmip6(model=model, experiment=experiment, variable=variable, frequency=frequency, realm=realm, check=check, path=dl_dir, rlzn=rlzn)

