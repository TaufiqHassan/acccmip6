Quickstart guide
================

A basic user guide for minimal usage.

Simply type ``pip install acccmip6`` from your terminal to install the package. 

General usage -

- Type ``acccmip6 -h`` for help.
- Use ``acccmip6 -o S`` to search the database.
- Use ``acccmip6 -o D`` to download from the database.

All usable arguments and their explanations -

**Required Argument**

- ``-o`` : Takes output type. 'S' for searching the database or 'D' for downloading from the database. Use 'M' for using the CMIP6DB module.

**Optional Arguments**
  
- ``-m`` : Model names (multiple comma separated names are allowed)
- ``-e`` : Experiment names
- ``-f`` : CMIP6 output frequency (e.g. mon, day etc.)
- ``-v`` : Variable names
- ``-r`` : Realm name (e.g. atmos, ocean etc.)
- ``-rlzn`` : Select a specified realization
- ``-c`` : 'yes' to use checker when searching or downloading. This helps to find out whether the search items are currently available. If not, it will produce suggestions that matches closely to your search.
- ``-desc`` : 'yes' to get the description of the experiments searched for
- ``-dir`` : Download directory
- ``-skip`` : Skip any item (model/experiment/realizations) from your download
- ``-time`` : 'yes' to print out all available time periods
- ``-yr`` : Select data for a time period (number of years)

Example usage ::

        $ acccmip6 -o S -m MIROC6 -e ssp245 -v zg -f mon -r atmos

Output ::

          TIPS: Use the check (-c) argument to check your inputs.


          Currently available models based on your search:

          ['MIROC6']

          Currently available variables based on your search:

          ['zg']

          Currently available experiments based on your search:

          ['ssp245']

          Number of files: 27

          Available realizations: [1, 2, 3]



 
Helpful demos:

- `installation`_
- `search`_ 
- `download`_

.. _`installation`: https://github.com/TaufiqHassan/acccmip6/blob/master/docs/installation_demo.gif
.. _`search`: https://github.com/TaufiqHassan/acccmip6/blob/master/docs/searching_demo.gif
.. _`download`: https://github.com/TaufiqHassan/acccmip6/blob/master/docs/downloading_demo.gif


