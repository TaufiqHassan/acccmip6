import argparse

from acccmip6.access_cm import SearchCmip6
from acccmip6.download_dat import DownloadCmip6
from acccmip6.utilities.util import _check_list

def main():

    parser = argparse.ArgumentParser()
    
    parser.add_argument("-dir", help="Download directory.", default=None)
    parser.add_argument("-o","--output-options", help="S for 'Searching' or D for 'Downloading'. Use M to initiate the CMIP6DB module.", required=True)
    parser.add_argument("-m", help="Model names", default=None)
    parser.add_argument("-e", help="Experiment names", default=None)
    parser.add_argument("-v", help="Variable names", default=None)
    parser.add_argument("-f", help="Output frequency", default=None)
    parser.add_argument("-r", help="Output realm", default=None)
    parser.add_argument("-rlzn", help="Select realization", default=None)
    parser.add_argument("-yr", help="Select year", default=None)
    parser.add_argument("-c", help="Checker: yes to check inputs", default=None)
    parser.add_argument("-desc", help="Description: yes to print out experiment description", default=None)
    parser.add_argument("-time", help="Description: yes to print out avalable time periods", default=None)
    parser.add_argument("-skip", help="Skip any item in your download", default=None)
	
    args = parser.parse_args()
    model = _check_list(args.m)
    experiment = _check_list(args.e)
    variable = _check_list(args.v)
    frequency = _check_list(args.f)
    realm = _check_list(args.r)
    year = _check_list(args.yr)
    check = args.c
    rlzn = _check_list(args.rlzn)
    desc = args.desc
    time = args.time
    out = args.output_options
    dl_dir = args.dir
    skipped = args.skip
    
    if (out == 'S'):
        SearchCmip6(model=model, experiment=experiment, variable=variable, frequency=frequency, realm=realm, check=check, desc=desc, year=year, time=time)
    elif (out == 'D'):
        DownloadCmip6(model=model, experiment=experiment, variable=variable, frequency=frequency, realm=realm, check=check, path=dl_dir, rlzn=rlzn, skip=skipped, year=year)
    elif (out == 'M'):
        SearchCmip6(module='on', model=model, experiment=experiment, variable=variable, frequency=frequency, realm=realm)
        
