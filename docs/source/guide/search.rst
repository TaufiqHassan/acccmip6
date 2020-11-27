Searching the database
======================

For all kinds of searches use ``acccmip6 -o S`` and then add in the optional arguments according to your need. 

Optinal arguments 1
-------------------

Use these arguments with **any combination** and in **any sequence**.

- ``-m`` : takes model names
- ``-e`` : takes experiment names
- ``-v`` : takes variable names
- ``-f`` : takes frequency
- ``-r`` : takes realm name

**General usage** ::

        acccmip6 -o S -m MIROC6 -v vas -f mon -r atmos

**General output** ::

        TIPS: Use the check (-c) argument to check your inputs.


        Currently available models based on your search:

        ['MIROC6']

        Currently available variables based on your search:

        ['vas']

        Currently available experiments based on your search:

        ['hist-piAer', 'ssp119', 'ssp585', 'piClim-NTCF', 'piClim-histall', 'hist-stratO3', 'piClim-OC', 'ssp534-over', 
        'hist-piNTCF', 'abrupt-4xCO2', 'piClim-anthro', 'piClim-2xfire', 'amip-p4K', 'amip-4xCO2', 'histSST-piAer', 
        'piClim-lu', 'historical', 'piControl', 'faf-stress', 'piClim-SO2', 'faf-all', 'piClim-control', 'amip-hist', 
        'ssp370SST-lowBC', 'hist-GHG', 'piClim-2xdust', 'dcppA-hindcast', 'ssp245-stratO3', 'ssp245-aer', 'dcppA-assim', 
        'ssp460', 'faf-passiveheat', 'amip', 'amip-future4K', 'hist-CO2', 'ssp245', 'ssp370', 'ssp370SST', 'hist-aer', 
        'ssp434', '1pctCO2', 'ssp245-GHG', 'piClim-aer', 'piClim-histghg', 'ssp126', 'histSST-piNTCF', 'piClim-4xCO2', 
        'piClim-2xss', 'abrupt-0p5xCO2', 'piClim-BC', 'faf-heat', 'ssp370-lowNTCF', 'abrupt-2xCO2', 'histSST', 'piClim-ghg', 
        'piClim-histaer', 'faf-water', 'ssp370SST-lowAer']


        Number of files: 782


        Available realizations: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

                         <===============Exiting now!================>


**Allows multiple inputs:** takes comma (,) separated multiple items ::

        acccmip6 -o S -m MIROC6,CanESM,CNRM-CM6-1-HR -v va,ua -e ssp245-aer,hist-piAer

**Allows list inputs:** this is useful since the ``acccmip6`` outputs in list format ::

        acccmip6 -o S -e ['ssp245-GHG','historical'] -v ['hfls','hfss'] -f mon

**Recommended:** Use inputs within a ' ' ::

        acccmip6 -o S -m 'MIROC6, CanESM, CNRM-CM6-1-HR' -e '['ssp245-GHG', 'historical']' -f mon


Optional arguments 2
--------------------

- ``-c`` : 'yes' to check the inputs under optional argumetns 1. Searches through the servers and checks whether the input items are available or not.

**General usage** ::

        acccmip6 -o S -m MIROC6 -v vas -f mon -r atmos -c yes

**General output** ::

        TIPS: If you are not sure about what you are looking for use CMIP6DB module
              to look for currently available models/experiments/variables and so on . . .

        Checking for MIROC6 model in CMIP6 database . . .
        Found: MIROC6 model.

        Checking for vas variable in CMIP6 database . . .
        Found: vas variable.

        Checking for mon frequency in CMIP6 database . . .
        Found: mon frequency.

        Checking for atmos realm in CMIP6 database . . .
        Found: atmos realm.


        Currently available models based on your search:

        ['MIROC6']

        Currently available variables based on your search:

        ['vas']

        Currently available experiments based on your search:

        ['ssp370SST-lowBC', 'amip-future4K', 'abrupt-4xCO2', 'piClim-aer', 'piClim-histall', 'dcppA-hindcast', 'faf-all', 
        'amip-4xCO2', 'hist-CO2', 'histSST-piNTCF', 'piClim-histaer', 'piClim-2xdust', '1pctCO2', 'histSST-piAer', 'ssp245', 
        'piClim-2xfire', 'faf-water', 'piClim-histghg', 'piClim-2xss', 'ssp245-stratO3', 'amip', 'hist-aer', 'ssp245-GHG', 
        'piClim-OC', 'ssp370', 'faf-heat', 'piClim-NTCF', 'ssp370SST-lowAer', 'amip-hist', 'piClim-4xCO2', 'piClim-control', 
        'hist-stratO3', 'piClim-ghg', 'piClim-lu', 'histSST', 'faf-stress', 'ssp585', 'abrupt-0p5xCO2', 'ssp370-lowNTCF', 
        'ssp119', 'piClim-BC', 'amip-p4K', 'ssp245-aer', 'ssp370SST', 'abrupt-2xCO2', 'hist-GHG', 'dcppA-assim', 'hist-piNTCF', 
        'faf-passiveheat', 'piControl', 'ssp534-over', 'ssp126', 'hist-piAer', 'piClim-anthro', 'ssp460', 'historical', 
        'piClim-SO2', 'ssp434']



        Number of files: 782



        Available realizations: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]




                   <===============Exiting now!================>


**Get suggestions:** use the ``-c`` argument when in doubts whether any input item is available in the current database. ::

        acccmip6 -o S -m IPSL -c yes

**Output with suggestions** ::

        TIPS: If you are not sure about what you are looking for use CMIP6DB module
              to look for currently available models/experiments/variables and so on . . .

        Checking for IPSL model in CMIP6 database . . .

        Cannot find model.
        Looking for other options . . .

        Option  1 IPSL-CM6A-ATM-HR

        Option  2 IPSL-CM6A-LR

        Did you mean any of the above?


Optional arguments 3
--------------------

- ``-desc`` : 'yes' to get the description of the experiments searched with ``-e`` argument. The descriptions comes at the end of the general search results.

**general usage** ::

       acccmip6 -o S -e hist-piNTCF,hist-piAer -v vas -m MIROC6 -desc yes

**General output** ::

        TIPS: Use the check (-c) argument to check your inputs.


        Currently available models based on your search:

        ['MIROC6']

        Currently available variables based on your search:

        ['vas']

        Currently available experiments based on your search:

        ['hist-piNTCF', 'hist-piAer']



        Number of files: 12



        Available realizations: [1, 2, 3]

        < < < Here are the experiment descriptions > > >


        hist-piNTCF:
        Impose historical WMGHG and halocarbon concentrations. Near Term Climate Forcers 
        (NTCFs: methane, tropospheric ozone and aerosols, and their precursors), to be 
        fixed at 1850 emission levels. These simulations parallel the "CMIP6 historical", 
        and differ only by fixing the anthropogenic emissions or concentrations of a 
        specified class of species.   All other forcing agents must evolve as in "CMIP6 historical".


        hist-piAer:
        Historical WMGHG and Halocarbon concentrations.  Historical ozone precursor emissions 
        (e.g. NOx).  Aerosols and aerosol precursors fixed at 1850 emission levels.

Extra arguments
---------------

Use these optional arguments with in addition to **Optional arguments**.

- ``-rlzn`` : select a realization

- ``-skip`` : skip items during download


- ``-time`` : 'yes' print out all available time periods

**general usage** ::

    acccmip6.py -o S -v pr -e historical -f mon -m NorESM2-LM -time yes

**general output:** Avalable time periods are 1850-1859, 1860-1869 and so on until 2010-2014. ::

        TIPS: Use the check (-c) argument to check your inputs.


        Currently available models based on your search:

        ['NorESM2-LM']

        Currently available variables based on your search:

        ['pr']

        Currently available experiments based on your search:

        ['historical']



        Number of files: 51



        Available realizations: [1, 2, 3]


        < < < Data available for these time periods > > >

        ['1850', '1860', '1870', '1880', '1890', '1900', '1910', '1920', '1930', '1940', '1950', '1960', '1970', '1980', '1990', '2000', '2010']

- ``-yr`` : select data for a specific time period

**general usage:** To download only the first 10 years (e.g. 1850-1859), use ``-yr 10`` or the last 5 years (e.g. 2010-2014), use ``-yr -5``. ::

    python acccmip6.py -o S -v pr -e historical -f mon -m NorESM2-LM -yr -5 -time yes

**general output:** Note that the number of files is reduced from 51 to 3! This is very useful if the the data are as frequently chunked as this particular example. ``-yr 11`` will download the 1850-1859 and 1860-1869 chunks. So, even though the user needs only the first 11 years of data, the package is limited to download whatever chunk is available to fullfill that 11 years of time period. ::

        TIPS: Use the check (-c) argument to check your inputs.


        Currently available models based on your search:

        ['NorESM2-LM']

        Currently available variables based on your search:

        ['pr']

        Currently available experiments based on your search:

        ['historical']



        Number of files: 3



        Available realizations: [1, 2, 3]


        < < < Data available for these time periods > > >

        ['2010']
        

**acccmip6** package accesses all publicly available CMIP6 data servers. Currently available servers -

- `USA`_, PCMDI/LLNL (California)
- `France`_, IPSL
- `Germany`_, DKRZ
- `UK`_, CEDA

.. _`USA`: https://esgf-node.llnl.gov/search/cmip6/
.. _`France`: https://esgf-node.ipsl.upmc.fr/search/cmip6-ipsl/
.. _`Germany`: https://esgf-data.dkrz.de/search/cmip6-dkrz/
.. _`UK`: https://esgf-index1.ceda.ac.uk/search/cmip6-ceda/
