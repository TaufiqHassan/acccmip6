===============================
Access Cmip6
===============================

.. image:: https://img.shields.io/travis/TaufiqHassan/acccmip6.svg
        :target: https://travis-ci.org/TaufiqHassan/acccmip6

.. image:: https://img.shields.io/pypi/v/acccmip6.svg
        :target: https://pypi.python.org/pypi/acccmip6



``acccmip6`` package can access CMIP6 database in real-time.

* GitHub repo: https://github.com/TaufiqHassan/acccmip6
* Documentation: https://acccmip6.readthedocs.org.

Features
--------

- Real-time search and download from continuously updating CMIP6 database
- Find data for any specific items (e.g. model, experiment, variable, frequency, realm)
- Search and download any combination of the above items
- Validate your search items
- Get suggestions if necessary
- Access definition of the experiments
- Skips already existing files

Installation
------------

``pip install acccmip6``

Usage
-----

``acccmip6`` searches the live CMIP6 database and spits out currently available models, experiments and variables that satisfies your search criteria. It will also output the number of available files. 
``acccmip6`` also tries to be a good command-line interface (CLI). Run `acccmip6 -h` to see a help message with all the arguments you can pass.

Required Arguments
------------------

- ``-o`` : Takes output type. 'S' for searching the database or 'D' for downloading from the database.

Optional Arguments
------------------

- ``-m`` : Model names (multiple comma separated names are allowed)
- ``-e`` : Experiment names
- ``-f`` : CMIP6 output frequency (e.g. mon, day etc.)
- ``-v`` : Variable names
- ``-r`` : Realm name (e.g. atmos, ocean etc.)
- ``-c`` : 'yes' to use checker when searching or downloading. This helps to find out whether the search items are currently available. If not, it will produce suggestions that matches closely to your search.
- ``-desc`` : 'yes' to get the description of the experiments searched for
- ``-dir`` : Download directory

License
-------

This code is licensed under the `MIT License`_.

.. _`MIT License`: https://opensource.org/licenses/MIT
