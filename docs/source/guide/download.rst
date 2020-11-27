Downloading data
================

For all kinds of download use ``acccmip6 -o D`` and then add in the optional arguments.

All arguments listed in **Optional arguments 1** and **Optional arguments 2** are allowed for downloading the data.

Extra arguments
---------------

Use these optional arguments with in addition to **Optional arguments 1** and **Optional arguments 2**.

- ``-dir`` : select directory. If kept blank, ``acccmip6`` will ask for a directory. With no inputs, download will continue in CMIP6 directory.
- ``-rlzn`` : select realization

- ``-skip`` : skip items during download

- ``-yr`` : select data for a specific time period

**General usage** ::

        acccmip6 -o D -e hist-piNTCF -v vas -m MIROC6

**General output** ::

        Finding server . . .

        Current directory:  /mnt/d/Work/acccmip6_download

        Default directory:  /mnt/d/Work/acccmip6_download/CMIP6
        Please specify a directory here:

**with no input:** creates directory/folder if not available ::

        Finding server . . .

        Current directory:  /mnt/d/Work/acccmip6_download

        Default directory:  /mnt/d/Work/acccmip6_download/CMIP6
        Please specify a directory here:

        Selected directory:  /mnt/d/Work/acccmip6_download/CMIP6

        /mnt/d/Work/acccmip6_download/CMIP6 doesn't exist. Creating one...



        vas_Amon_MIROC6_hist-piNTCF_r1i1p1f1_gn_185001-194912.nc is available!

        Downloading  36% |███████████████░░░░░░░░░░░░░░░░░░░░░░░░░| 44/120MB 25.62 MB/s

**with input directory:** creates directory/folder if not available ::

        Finding server . . .

        Current directory:  /mnt/d/Work/acccmip6_download

        Default directory:  /mnt/d/Work/acccmip6_download/CMIP6
        Please specify a directory here:
        /mnt/d/Work/acccmip6_download/download_here
        Selected directory:  /mnt/d/Work/acccmip6_download/download_here

        /mnt/d/Work/acccmip6_download/download_here doesn't exist. Creating one...



        vas_Amon_MIROC6_hist-piNTCF_r1i1p1f1_gn_185001-194912.nc is available!

        Downloading  41% |█████████████████░░░░░░░░░░░░░░░░░░░░░░░| 50/120MB 29.80 MB/s

**with** ``-dir`` **argument** ::

        acccmip6 -o D -e hist-piNTCF -v vas -m MIROC6 -dir /mnt/d/Work/acccmip6_download/download_here

**output** ::

        Finding server . . .
        creating  /mnt/d/Work/acccmip6_download/download_here


        vas_Amon_MIROC6_hist-piNTCF_r1i1p1f1_gn_185001-194912.nc is available!

        Downloading  41% |█████████████████░░░░░░░░░░░░░░░░░░░░░░░| 50/120MB 28.79 MB/s


**selecting specific realization** ::

        acccmip6 -o D -e hist-piNTCF -v vas -m MIROC6 -dir /mnt/d/Work/acccmip6_download/download_here -rlzn 2

**output** ::

        Finding server . . .


        vas_Amon_MIROC6_hist-piNTCF_r2i1p1f1_gn_185001-194912.nc is available!

        Downloading  33% |█████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░| 40/120MB 26.54 MB/s

**skipping items:** skip any item (models/experiments/variables) you don't want to download ::

        acccmip6 -o D -e ssp245-aer,ssp245,hist-aer -MIROC6,CanESM5 -f mon -r atmos -skip hist-aer,ua,va,zg
            
